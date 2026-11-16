# AGENTS.md

Instructions for coding agents in `retroComputersDocs`. The family rules of `retroICs`
(`docs/agents/global.md`, `docs/agents/review-checklist.md`, `docs/sources-policy.md` of a sibling
checkout `../retroICs`) apply here too.

## Repository

- Board records and their sources, one folder per computer: `computers/<name>/`.
- Record IDs: the prefixes this repo defines and the ones its records cite are registered in
  `docs/record-ids.md` (`here`: defined in a record of this repo; `external`: defined in
  `retroICs` or `retroMachines`); a board item is defined by the first cell of a table row of the
  record named as its Home. IDs keep their prefix and number forever; a moved item keeps its ID; a
  new board item takes the next free number of the board prefix of its section (GLUE, MEM, ...).
- Source IDs (`[R86]`, `[K14]`) cited under `computers/` are registered once in `docs/sources.md`
  (Home: the index that describes the document; the board sources and the clock chips' sheets live
  in `computers/<name>/index.md`, the large chips' sheets in `retroICs`).
- Not a submodule of anything. The records cite `retroICs` and `retroMachines` IDs; the record check
  takes a `retroICs` and a `retroMachines` checkout (`--external retroICs=<dir> --external
  retroMachines=<dir>`).
- Only our own documents are stored (records, indexes, the crops and extractions we made). A
  third-party file found in a repository comes from a submodule under `sources/`: `sources/radio-86rk` is the fork `BarabashkaD/radio-86rk` of
  skiselev/radio-86rk, pinned at c5e9cb7 (the commit the files were copied from). Clone with
  `--recursive`, or run `git submodule update --init`; `tools/check_index.py` stops with one
  problem naming that command when the submodule is not checked out. Never edit the submodule's
  files; a new pin is a reviewed change of the gitlink, with the hashes of the index re-checked.
- Platform material (an FPGA core's address map, its emulation of an add-on, its own cards) stays
  in the platform repo. A board record describes the original board only.

## Commands

From the repo root, in PowerShell 7 (`pwsh`); never `bash`, `sh` or Linux utilities. Python 3,
standard library only, always with `-B`.

```text
python -B -m unittest discover -s tools/tests -v                    the tools' tests
python -B tools/check_index.py                                      index and LF rule
python -B ../retroICs/tools/check_records.py --repo . --records computers --external retroICs=../retroICs --external retroMachines=../retroMachines
                                                                    record IDs and source IDs
python -B ../retroICs/tools/check_privacy.py --repo . --all         privacy, every commit
```

CI (`.github/workflows/checks.yml`, job `lint`) runs the same, with the retroICs tools at a pinned
commit (`RETROICS_REF`, checked out at `build/retroICs`) and the retroMachines registries at the
head of its branch (`RETROMACHINES_REF`, a branch name, `build/retroMachines`; retroMachines' CI
pins this repo by commit, so this side cannot pin retroMachines by commit too): the `retroMachines`
IDs (CLK, IE4) are checked too (`--external retroMachines=build/retroMachines`).

## Adding a source

1. Follow the checklist of `retroICs/docs/sources-policy.md`: provenance, licence check written
   down, metadata stripped (the PDF rewrite there; images: no EXIF, XMP, comment or text chunks),
   SHA-256 of the stored file and of the file as copied.
2. The entry in `computers/<name>/index.md` with the fields of the policy, and one row per file in
   its `## Files` table (`tools/check_index.py`); the ID's row in `docs/sources.md` (Home, kind;
   `tools/tests/test_sources.py`). A file that would be stored unchanged and lives in a repository
   is not copied: a submodule of a fork of that repository, pinned at the commit, and its row gives
   the repo-root path in the submodule (`sources/<repo>/...`); `tools/check_index.py` hashes the
   blob at the pinned commit.
3. An explicit ban, an unclear status or a file above 50 MB: listed with its hash and link, not
   stored.
4. A stored file is never edited after its first push; a better copy is a new file with its own
   entry.
5. A line in `CHANGELOG.md` under `## Unreleased`.

## Rules

- No absolute local paths, user or host names, IPs or emails in committed files, file metadata or
  commit messages, except the exact lines of `privacy-allow.txt` (each with its reason).
- Records: no plan or task history in the wording; sources cited by bracket ID, page and figure.
- The owner's files use LF and a final newline; stored sources keep their bytes (after the
  metadata strip) and are exempt.
- Commit or push only when the maintainer asks. `main` changes by pull request ("Rebase and
  merge"); the maintainer merges and tags (`vYYYY.MM.DD`) by hand. An agent never creates a tag or
  a release.
