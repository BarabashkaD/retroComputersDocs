# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: 2026 Dmitry Veremeev (BarabashkaD), https://github.com/BarabashkaD
"""check_index.py on small repositories, and on this one."""
import hashlib
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_index as ci  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent

# a JPEG walked by the checker: SOI, APP0 JFIF, DQT, SOF0, DHT, SOS with entropy data (a stuffed
# FF00 and an RST0 inside), EOI. The segment bodies are filler: the checker reads the structure only
JFIF = b"\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"
JPEG_BODY = (b"\xff\xdb\x00\x04\x00\x01" + b"\xff\xc0\x00\x05\x08\x00\x01" + b"\xff\xc4\x00\x03\x00"
             + b"\xff\xda\x00\x03\x01" + b"\x12\xff\x00\x34\xff\xd0\x56")


def jpeg(*segments, tail=b""):
    return b"\xff\xd8" + JFIF + b"".join(segments) + JPEG_BODY + b"\xff\xd9" + tail


def chunk(typ, body=b""):
    return len(body).to_bytes(4, "big") + typ + body + b"\0\0\0\0"


def png(*chunks, tail=b""):
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", b"\0" * 13) + b"".join(chunks)
            + chunk(b"IDAT", b"x") + chunk(b"IEND") + tail)


def make_repo(d, files, index_rows):
    root = Path(d)
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    for name, data in files.items():
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    rows = "".join("| `%s` | [X] | %d | %s | x |\n" % r for r in index_rows)
    idx = root / "computers" / "m" / "index.md"
    idx.parent.mkdir(parents=True, exist_ok=True)
    idx.write_bytes(("# m\n\n## Files\n\n| File | ID | Size | SHA-256 | Licence |\n"
                     "|---|---|---|---|---|\n" + rows).encode())
    return root


def sha(data):
    return hashlib.sha256(data).hexdigest()


# a fixed identity for the test commits (no email-shaped text in this file)
GIT_ID = {"GIT_AUTHOR_NAME": "test", "GIT_AUTHOR_EMAIL": "test", "GIT_COMMITTER_NAME": "test",
          "GIT_COMMITTER_EMAIL": "test"}


def add_submodule(root, path, files):
    """A nested repository at root/path with files committed, and its gitlink in root's index (as
    `git submodule add` leaves it). Returns the commit."""
    sub = Path(root) / path
    sub.mkdir(parents=True)
    env = dict(os.environ, **GIT_ID)
    subprocess.run(["git", "init", "-q", str(sub)], check=True)
    subprocess.run(["git", "-C", str(sub), "config", "core.autocrlf", "false"], check=True)
    for name, data in files.items():
        p = sub / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    subprocess.run(["git", "-C", str(sub), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(sub), "commit", "-q", "-m", "files"], check=True, env=env)
    commit = subprocess.run(["git", "-C", str(sub), "rev-parse", "HEAD"], capture_output=True,
                            check=True).stdout.decode().strip()
    subprocess.run(["git", "-C", str(root), "update-index", "--add", "--cacheinfo",
                    "160000,%s,%s" % (commit, path)], check=True)
    return commit


def rmtree_force(path):
    """shutil.rmtree that also removes git's read-only object files (Windows)."""
    def retry(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(path, onexc=retry)


def listed(files):
    return [(n[len("computers/m/"):], len(b), sha(b)) for n, b in files.items()]


class CheckIndex(unittest.TestCase):
    def check_files(self, files):
        with tempfile.TemporaryDirectory() as d:
            return ci.check(make_repo(d, files, listed(files)))

    def test_listed_file_passes(self):
        self.assertEqual(self.check_files({"computers/m/scans/a.png": png(),
                                           "computers/m/scans/b.jpg": jpeg(),
                                           "computers/m/notes/c.bin": b"\x01\x02"}), [])

    def test_unlisted_file_fails(self):
        with tempfile.TemporaryDirectory() as d:
            root = make_repo(d, {"computers/m/scans/a.bin": b"x"}, [])
            self.assertEqual(ci.check(root),
                             ["computers/m/index.md: no '## Files' table",
                              "computers/m/scans/a.bin: stored but not listed in computers/m/index.md"])

    def test_wrong_hash_and_missing_fail(self):
        with tempfile.TemporaryDirectory() as d:
            root = make_repo(d, {"computers/m/scans/a.bin": b"x"},
                             [("scans/a.bin", 1, "0" * 64), ("scans/b.bin", 1, "0" * 64)])
            out = ci.check(root)
            self.assertEqual(len(out), 2, out)
            self.assertTrue(out[0].startswith("computers/m/scans/a.bin: SHA-256"), out)
            self.assertEqual(out[1], "computers/m/scans/b.bin: listed but missing")

    def test_crlf_owner_file_fails_listed_passes(self):
        data = b"third party\r\n"
        with tempfile.TemporaryDirectory() as d:
            root = make_repo(d, {"README.md": b"x\r\n", "computers/m/notes/n.md": data},
                             [("notes/n.md", len(data), sha(data))])
            self.assertEqual(ci.check(root), ["README.md: CR in line ends"])

    def test_jpeg_metadata_segments_fail(self):
        files = {"computers/m/s/a.jpg": jpeg(b"\xff\xe1\x00\x08Exif\x00\x00"),
                 "computers/m/s/b.jpg": jpeg(b"\xff\xfe\x00\x05abc"),
                 "computers/m/s/c.jpeg": jpeg(b"\xff\xed\x00\x04ab")}
        self.assertEqual(self.check_files(files),
                         ["computers/m/s/a.jpg: image metadata APP1",
                          "computers/m/s/b.jpg: image metadata COM",
                          "computers/m/s/c.jpeg: image metadata APP13"])

    def test_jpeg_metadata_after_the_first_scan_fails(self):
        # a second frame part after the entropy data of the first scan
        late = (b"\xff\xd8" + JFIF + JPEG_BODY + b"\xff\xe1\x00\x04ab" + b"\xff\xd9")
        self.assertEqual(self.check_files({"computers/m/s/a.jpg": late}),
                         ["computers/m/s/a.jpg: image metadata APP1"])

    def test_bytes_after_end_marker_fail(self):
        files = {"computers/m/s/a.jpg": jpeg(tail=b"hidden"),
                 "computers/m/s/b.png": png(tail=b"hidden!")}
        self.assertEqual(self.check_files(files),
                         ["computers/m/s/a.jpg: 6 bytes after EOI",
                          "computers/m/s/b.png: 7 bytes after IEND"])

    def test_png_chunks_allow_list(self):
        ok = png(chunk(b"gAMA", b"\0" * 4), chunk(b"pHYs", b"\0" * 9), chunk(b"sRGB", b"\0"),
                 chunk(b"PLTE", b"\0" * 3), chunk(b"tRNS", b"\0"), chunk(b"bKGD", b"\0"),
                 chunk(b"cHRM", b"\0" * 32))
        files = {"computers/m/s/ok.png": ok,
                 "computers/m/s/t.png": png(chunk(b"tEXt", b"a\0b")),
                 "computers/m/s/i.png": png(chunk(b"iCCP", b"p\0\0x")),
                 "computers/m/s/x.png": png(chunk(b"eXIf", b"MM")),
                 "computers/m/s/v.png": png(chunk(b"vpAg", b"\0" * 9))}
        self.assertEqual(self.check_files(files),
                         ["computers/m/s/i.png: image metadata iCCP",
                          "computers/m/s/t.png: image metadata tEXt",
                          "computers/m/s/v.png: image metadata vpAg",
                          "computers/m/s/x.png: image metadata eXIf"])

    def test_truncated_images_fail(self):
        files = {"computers/m/s/a.jpg": jpeg()[:-2], "computers/m/s/b.png": png()[:-8]}
        out = self.check_files(files)
        self.assertEqual(len(out), 2, out)
        self.assertTrue(out[0].startswith("computers/m/s/a.jpg: truncated"), out)
        self.assertTrue(out[1].startswith("computers/m/s/b.png: truncated"), out)

    def test_extension_must_match_magic(self):
        files = {"computers/m/s/a.png": jpeg(), "computers/m/s/b.jpg": png(),
                 "computers/m/s/c.bin": jpeg(), "computers/m/s/d.dat": png(),
                 "computers/m/s/e.jpg": b"not an image"}
        self.assertEqual(self.check_files(files),
                         ["computers/m/s/a.png: extension .png but not a PNG",
                          "computers/m/s/b.jpg: extension .jpg but not a JPEG",
                          "computers/m/s/c.bin: a JPEG with extension .bin",
                          "computers/m/s/d.dat: a PNG with extension .dat",
                          "computers/m/s/e.jpg: extension .jpg but not a JPEG"])

    def test_submodule_file_hashed_at_the_pinned_commit(self):
        data = b"third party\r\n"
        with tempfile.TemporaryDirectory() as d:
            # the File cell of a submodule file is relative to the repo root
            root = make_repo(d, {}, [("src/x/doc/a.md", len(data), sha(data))])
            add_submodule(root, "src/x", {"doc/a.md": data})
            # the checkout's bytes do not count (line-end conversion, local edits): the blob does
            (root / "src" / "x" / "doc" / "a.md").write_bytes(b"third party\n")
            self.assertEqual(ci.check(root), [])

    def test_submodule_wrong_hash_and_missing_fail(self):
        with tempfile.TemporaryDirectory() as d:
            root = make_repo(d, {}, [("src/x/a.bin", 1, "0" * 64), ("src/x/b.bin", 1, "0" * 64)])
            commit = add_submodule(root, "src/x", {"a.bin": b"x"})
            out = ci.check(root)
            self.assertEqual(len(out), 2, out)
            self.assertTrue(out[0].startswith("src/x/a.bin: SHA-256"), out)
            self.assertEqual(out[1], "src/x/b.bin: listed but missing in the submodule at %s"
                             % commit[:7])

    def test_submodule_not_checked_out_one_problem(self):
        with tempfile.TemporaryDirectory() as d:
            root = make_repo(d, {}, [("src/x/a.bin", 1, sha(b"x")), ("src/x/b.bin", 1, sha(b"y"))])
            add_submodule(root, "src/x", {"a.bin": b"x", "b.bin": b"y"})
            self.assertEqual(ci.check(root), [])
            # as after a clone without --recurse-submodules: an empty folder at the gitlink
            rmtree_force(root / "src" / "x")
            (root / "src" / "x").mkdir()
            self.assertEqual(ci.check(root), ["src/x: submodule not checked out (run git "
                                              "submodule update --init)"])

    def test_this_repository(self):
        self.assertEqual(ci.check(ROOT), [])


if __name__ == "__main__":
    unittest.main()
