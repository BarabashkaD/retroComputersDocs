# Changelog

Features, changes, fixes and known issues of each dated release (`vYYYY.MM.DD`).

## Unreleased

- Repo skeleton: `README.md`, `AGENTS.md`, `NOTICE`, `LICENSE`, licence texts in `LICENSES/`,
  `tools/check_index.py` (every stored source listed with its size and SHA-256; whole-file image
  checks: no metadata, nothing after the end marker, the extension matches the format; LF rule),
  lint workflow with the retroICs record and privacy checkers.
- Radio-86RK: the board record `computers/rk86/board.md` (VID, GLUE, MEM, TAPE, SND, the board
  items CLK-11, IE4-4, IE4-5 and the 8275 pins on the boards) and the ROM disk module record
  `computers/rk86/romdisk-module.md` (ROMD), with their source index.
- Radio-86RK sources: Радио 1986 No. 4, 5, 6 and 1987 No. 3, 5 scans; Sergey Kiselev's rev. 1.4
  KiCad sheets, schematic PDF, notes and their net list. The vendor sheets of the board parts are
  listed in the index without their files.
- Own registries: `docs/record-ids.md` (the prefixes defined here, and the `retroICs` and
  `retroMachines` prefixes the records cite) and `docs/sources.md` (every cited source ID with its
  home and kind), with a test that every ID of a computer index's top table is registered; the
  record check runs on them with the `retroICs` checkout as the external repo.
- Radio-86RK board record: the board use of the 8080A, 8255A, 8257 and 8275 (from their data sheet
  records): CPU-5 and CPU-7, GLUE-14..GLUE-19, MEM-8, the 8257 on the board, the 8275's clock and
  attribute pins, the monitor's programming of the chips.
- Radio-86RK sources: the 8224 data sheet [D8224] (stored), the КР580ГФ24, 7490 and К155ИЕ4 sheets
  ([ГФ24], [7490], [ИЕ4], listed) now indexed here.
- Only our own documents stored: the plain copies of Sergey Kiselev's repository (the Радио
  1986-1987 scans, the KiCad sheets, his notes) come from the submodule `sources/radio-86rk`, the
  fork `BarabashkaD/radio-86rk` pinned at c5e9cb7; the index lists them by their submodule paths
  with the same hashes, and `tools/check_index.py` hashes them at the pinned commit. Kept here: the
  crops, the net list, and the schematic and 8224 PDFs with their metadata rewritten. The GPL-3.0
  text is no longer needed here.
- The schematic PDF of Kiselev's rev. 1.4 [K14] and the 8224 data sheet [D8224] are no longer stored
  (only our own documents here): the index reads the originals from the submodule
  `sources/radio-86rk`, with their hashes as copied.
