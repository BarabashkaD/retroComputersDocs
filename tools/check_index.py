# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: 2026 Dmitry Veremeev (BarabashkaD), https://github.com/BarabashkaD
"""Index checker: every stored source file is listed with its size and SHA-256; LF rule.

Usage: python -B tools/check_index.py [--repo DIR]

- computers/<name>/index.md has a section "## Files" with a table
  | File | ID | Size | SHA-256 | Licence |   (File: a path relative to computers/<name>/, in backticks)
- Every file in a subfolder of computers/<name>/ is listed there, and every listed file exists with
  that size and SHA-256. The markdown files directly in computers/<name>/ are the owner's records.
- A File that starts with the path of a submodule of this repository (a gitlink in the index, such
  as sources/radio-86rk/) is relative to the repository root: a third-party file, not stored here.
  Its size and SHA-256 are those of the blob at the pinned commit (the gitlink), read with git from
  the submodule's checkout, so the line-end settings of that checkout do not matter. A submodule
  that is not checked out gives one problem naming `git submodule update --init`.
- Every text file of the repository that is not listed (the owner's files) has LF line ends and
  ends with one newline. Listed files are kept as they were found and are exempt.
- Images, walked whole (check_privacy.py cannot read compressed image data, so the image files
  are on its path list; this check stands in for it):
  - the extension matches the magic number (.jpg / .jpeg: FF D8 FF; .png: the PNG signature), and
    a file with either magic number has the matching extension;
  - JPEG: every segment of the file, scans included, is walked; only APP0, DQT, DHT, DRI, DAC,
    SOFn, SOS, RSTn and EOI occur (no APP1..APP15 such as EXIF, XMP, IPTC, no COM, no unknown
    marker), and nothing follows EOI;
  - PNG: only the chunks IHDR, PLTE, IDAT, IEND, pHYs, gAMA, cHRM, sRGB, tRNS, bKGD occur, the file
    is not truncated, and nothing follows IEND.

Output: one line per problem, or PASS index.
"""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path

BINARY_EXT = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".djvu", ".bin"}


JPEG_MAGIC = b"\xff\xd8\xff"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_EXT = {".jpg", ".jpeg"}
PNG_ALLOWED = {b"IHDR", b"PLTE", b"IDAT", b"IEND", b"pHYs", b"gAMA", b"cHRM", b"sRGB", b"tRNS",
               b"bKGD"}
# JPEG segments with a length field that may occur: APP0, DQT, DHT, DRI, DAC, SOF0..SOF15 but
# DHT (C4), JPG (C8) and DAC (CC) which are listed on their own
JPEG_ALLOWED = ({0xE0, 0xDB, 0xC4, 0xDD, 0xCC}
                | {m for m in range(0xC0, 0xD0) if m not in (0xC4, 0xC8, 0xCC)})


def _marker_name(m: int) -> str:
    if 0xE0 <= m <= 0xEF:
        return "APP%d" % (m - 0xE0)
    return "COM" if m == 0xFE else "marker %02X" % m


def jpeg_problems(data: bytes) -> list[str]:
    """Walk every segment of a JPEG file (scans included)."""
    i = 2
    n = len(data)
    while True:
        if i + 2 > n or data[i] != 0xFF:
            return ["truncated or corrupt JPEG at byte %d" % i]
        while i + 1 < n and data[i + 1] == 0xFF:  # fill bytes before a marker
            i += 1
        m = data[i + 1]
        if m == 0xD9:
            rest = n - (i + 2)
            return ["%d bytes after EOI" % rest] if rest else []
        if 0xD0 <= m <= 0xD7:
            i += 2
            continue
        if i + 4 > n:
            return ["truncated JPEG at byte %d" % i]
        length = int.from_bytes(data[i + 2:i + 4], "big")
        if m != 0xDA and m not in JPEG_ALLOWED:
            return ["image metadata %s" % _marker_name(m)]
        i += 2 + length
        if m == 0xDA:  # entropy-coded data up to the next marker other than RSTn or FF00
            while True:
                j = data.find(b"\xff", i)
                if j < 0 or j + 1 >= n:
                    return ["truncated JPEG scan"]
                nxt = data[j + 1]
                if nxt == 0x00 or 0xD0 <= nxt <= 0xD7 or nxt == 0xFF:
                    i = j + (1 if nxt == 0xFF else 2)
                    continue
                i = j
                break


def png_problems(data: bytes) -> list[str]:
    """Walk every chunk of a PNG file."""
    i = 8
    n = len(data)
    while True:
        if i + 12 > n:
            return ["truncated PNG at byte %d" % i]
        length = int.from_bytes(data[i:i + 4], "big")
        typ = data[i + 4:i + 8]
        if typ not in PNG_ALLOWED:
            return ["image metadata %s" % typ.decode("latin1")]
        i += 12 + length
        if i > n:
            return ["truncated PNG chunk %s" % typ.decode("latin1")]
        if typ == b"IEND":
            rest = n - i
            return ["%d bytes after IEND" % rest] if rest else []


def image_problems(name: str, data: bytes) -> list[str]:
    """Extension against magic number, then the whole-file walk of a JPEG or PNG."""
    ext = Path(name).suffix.lower()
    is_jpeg, is_png = data.startswith(JPEG_MAGIC), data.startswith(PNG_MAGIC)
    if ext in JPEG_EXT and not is_jpeg:
        return ["extension %s but not a JPEG" % ext]
    if ext == ".png" and not is_png:
        return ["extension .png but not a PNG"]
    if is_jpeg and ext not in JPEG_EXT:
        return ["a JPEG with extension %s" % (ext or "(none)")]
    if is_png and ext != ".png":
        return ["a PNG with extension %s" % (ext or "(none)")]
    if is_jpeg:
        return jpeg_problems(data)
    if is_png:
        return png_problems(data)
    return []


def repo_files(root: Path) -> list[str]:
    """Tracked and untracked-not-ignored files, repo-relative with '/'."""
    r = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--cached", "--others",
                        "--exclude-standard"], capture_output=True, check=True)
    names = [n for n in r.stdout.decode("utf-8").split("\0") if n]
    return sorted(n for n in set(names) if (root / n).is_file())


def submodules(root: Path) -> dict[str, str]:
    """{path: pinned commit} of the gitlinks in the index of the repository."""
    r = subprocess.run(["git", "-C", str(root), "ls-files", "-s", "-z"], capture_output=True,
                       check=True)
    out: dict[str, str] = {}
    for entry in r.stdout.decode("utf-8").split("\0"):
        meta, _, path = entry.partition("\t")
        fields = meta.split()
        if len(fields) == 3 and fields[0] == "160000":
            out[path] = fields[1]
    return out


def submodule_of(name: str, subs: dict[str, str]) -> str | None:
    """The submodule path that a root-relative name lies in, or None."""
    for sub in subs:
        if name.startswith(sub + "/"):
            return sub
    return None


def submodule_blob(root: Path, sub: str, commit: str, rel: str) -> bytes | None:
    """The blob rel at the pinned commit of submodule sub, or None when it is not there."""
    r = subprocess.run(["git", "-C", str(root / sub), "cat-file", "blob", "%s:%s" % (commit, rel)],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def checked_out(root: Path, sub: str) -> bool:
    """The submodule has its own checkout (a .git file or folder), so git does not fall back to the
    superproject."""
    return (root / sub / ".git").exists()


def files_table(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line.strip() == "## Files"
            continue
        if not inside or not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] in ("File", "") or set(cells[0]) <= set("-: "):
            continue
        rows.append(cells)
    return rows


def check(root: Path) -> list[str]:
    root = Path(root)
    problems: list[str] = []
    files = repo_files(root)
    subs = submodules(root)
    missing_subs: set[str] = set()
    listed: set[str] = set()
    comps = root / "computers"
    for comp in sorted(p for p in comps.iterdir() if p.is_dir()) if comps.is_dir() else []:
        rel_comp = comp.relative_to(root).as_posix()
        index = comp / "index.md"
        if not index.is_file():
            problems.append("%s: index.md missing" % rel_comp)
            continue
        rows = files_table(index.read_text(encoding="utf-8"))
        if not rows:
            problems.append("%s/index.md: no '## Files' table" % rel_comp)
        seen: set[str] = set()
        for cells in rows:
            if len(cells) < 5:
                problems.append("%s/index.md: Files row with %d cells: %s"
                                % (rel_comp, len(cells), cells[0]))
                continue
            name = cells[0].strip("`")
            full = "%s/%s" % (rel_comp, name)
            if name in seen:
                problems.append("%s/index.md: %s listed twice" % (rel_comp, name))
            seen.add(name)
            sub = submodule_of(name, subs)
            if sub is not None:
                full = name
                if not checked_out(root, sub):
                    if sub not in missing_subs:
                        missing_subs.add(sub)
                        problems.append("%s: submodule not checked out (run git submodule update "
                                        "--init)" % sub)
                    continue
                data = submodule_blob(root, sub, subs[sub], name[len(sub) + 1:])
                if data is None:
                    problems.append("%s: listed but missing in the submodule at %s"
                                    % (full, subs[sub][:7]))
                    continue
            else:
                listed.add(full)
                p = root / full
                if not p.is_file():
                    problems.append("%s: listed but missing" % full)
                    continue
                data = p.read_bytes()
            if cells[2] != str(len(data)):
                problems.append("%s: size %d, index says %s" % (full, len(data), cells[2]))
            digest = hashlib.sha256(data).hexdigest()
            if cells[3].strip("`") != digest:
                problems.append("%s: SHA-256 %s, index says %s" % (full, digest, cells[3]))
        for f in files:
            if f.startswith(rel_comp + "/") and "/" in f[len(rel_comp) + 1:] and f not in listed:
                problems.append("%s: stored but not listed in %s/index.md" % (f, rel_comp))
    for f in files:
        for p in image_problems(f, (root / f).read_bytes()):
            problems.append("%s: %s" % (f, p))
        if f in listed or Path(f).suffix.lower() in BINARY_EXT:
            continue
        data = (root / f).read_bytes()
        if b"\0" in data[:8192]:
            continue
        if b"\r" in data:
            problems.append("%s: CR in line ends" % f)
        if data and (not data.endswith(b"\n") or data.endswith(b"\n\n")):
            problems.append("%s: must end with exactly one newline" % f)
    return problems


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    args = ap.parse_args(argv)
    out = check(args.repo)
    for line in out:
        print(line)
    if out:
        return 1
    print("PASS index")
    return 0


if __name__ == "__main__":
    sys.exit(main())
