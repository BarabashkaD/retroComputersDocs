# retroComputersDocs

Documents of retro computers as boards: the board records (how the chips are wired and what that
gives at the machine level), and the sources they rest on (schematics, magazine scans, board
makers' notes, data sheets of the board's glue parts), each with its provenance and licence check.
Only our own documents are stored here (the records, indexes, crops and extractions made while
working on the projects, and files we changed, such as a PDF with its metadata rewritten); a
third-party file that is a plain copy is read from a submodule pinned at the commit it was copied
from (`sources/`).
The chips' own data sheet records live in `retroICs` (the RK86 clock chips' with their machine in
`retroMachines`); the models that build a machine live in `retroMachines`; a platform keeps its
own material. The record IDs and source IDs of this repo are
registered in its own `docs/record-ids.md` and `docs/sources.md`.

## Layout

| Path | Content |
|---|---|
| `index.md` | the computers of this repo |
| `computers/<name>/index.md` | every source document of the computer: ID, title, issue, pages, provenance, licence check, SHA-256; the `## Files` table |
| `computers/<name>/board.md` | the board record of the original board |
| `computers/<name>/<module>.md` | the record of an add-on module (`romdisk-module.md`) |
| `computers/<name>/schematics/`, `magazines/` | the stored sources: our crops and net list, a schematic PDF with its metadata rewritten |
| `computers/<name>/datasheets/` | stored data sheets of the board's parts; for the RK86 also the clock chips' (8224, 7492 / К155ИЕ4): they have no model in retroICs (it holds only the ICs it implements) and are modelled inside the RK86 clock block in retroMachines (records in its `machines/rk86/ics/`), so their sheets stay here until the clock chips get models, and records, in retroICs |
| `sources/radio-86rk/` | submodule: the fork `BarabashkaD/radio-86rk` of Sergey Kiselev's repository at c5e9cb7 (the magazine scans, the KiCad sheets, his notes), cited by path from the index; clone with `--recursive`, or `git submodule update --init` |
| `docs/record-ids.md` | the record ID prefixes: defined here, or in `retroICs` / `retroMachines` |
| `docs/sources.md` | every bracket source ID the records cite, with its home index and kind |
| `tools/check_index.py` | every source file listed with its size and SHA-256 (stored here, or in the submodule at its pinned commit); LF rule |
| `AGENTS.md` | rules for coding agents in this repo |
| `LICENSE`, `NOTICE`, `LICENSES/` | the owner's licence, the attribution line, the licence texts |

## Computers

| Computer | Folder | Content |
|---|---|---|
| Radio-86RK | `computers/rk86/` | board record (`board.md`), the ROM disk module of Радио 1987 No. 3 (`romdisk-module.md`); crops of the Радио 1986 No. 5 schematic, Sergey Kiselev's rev. 1.4 schematic PDF and its net list; the Радио 1986-1987 scans and the KiCad sheets in `sources/radio-86rk/` |

## Checks

```text
python -B -m unittest discover -s tools/tests -v
python -B tools/check_index.py
python -B ../retroICs/tools/check_records.py --repo . --records computers --external retroICs=../retroICs
python -B ../retroICs/tools/check_privacy.py --repo . --all
```

## Licences

- `LICENSE` (BSD-3-Clause, the owner's copyright line) covers the owner's files only.
- The owner's code (`tools/`, `.github/`): BSD-3-Clause (`LICENSES/BSD-3-Clause.txt`).
- The owner's docs (this file, `AGENTS.md`, `CHANGELOG.md`, the indexes and records): CC BY 4.0
  (`LICENSES/CC-BY-4.0.txt`).
- Third-party documents keep their own terms, stated per file in the computer's `index.md`
  (`NOTICE` names them); they are not relicensed. A crop of a magazine page keeps the magazine's
  status (the owner claims no rights in it). The submodule's files are under the terms of their
  own repository (`sources/radio-86rk/LICENSE` and the notices in the files).
- Credit to Dmitry Veremeev (BarabashkaD) must be kept in copies and derived works (`NOTICE`).
