# Record ID registry

Every record ID prefix that the records of this repo define or cite, and where its items are.
Checked by `tools/check_records.py` of `retroICs` (`--repo . --records computers --external
retroICs=<checkout>`; the command is in `AGENTS.md`).

- Status `here`: defined in this repo, by the first cell of a table row of the row's Home file.
  `external`: defined in another repo, the first segment of the Home; checked only with
  `--external <repo>=<checkout>`, else one NOTE per repo. `retired` (Home `-`): defined nowhere
  here any more; never defined again, references allowed.
- IDs: empty for a whole prefix. A list when the items of one prefix are split over several homes;
  that row then covers only the listed IDs.
- Existing IDs keep their prefix and number forever; a moved item keeps its ID in its new home. A
  new board item takes the next free number of the board prefix of its section (wiring: GLUE,
  memory: MEM, sound: SND, ...); the board half of a chip's item names the item it comes from
  ("From CPU-1"), whose data sheet half keeps that ID in the chip's record.
- ID pattern: `[A-Z][A-Z0-9]{1,9}(?:-DEV)?-[DEM]?\d+`.
- The board items of the clock chips (CLK-11, IE4-4, IE4-5) and the two CPU items that are board
  wiring only (CPU-5, CPU-7) are defined in the RK86 board record; the other items of those
  prefixes are in the chips' records.

| Prefix | Home | Status | IDs |
|---|---|---|---|
| VID | retroComputersDocs/computers/rk86/board.md | here | |
| GLUE | retroComputersDocs/computers/rk86/board.md | here | |
| MEM | retroComputersDocs/computers/rk86/board.md | here | |
| TAPE | retroComputersDocs/computers/rk86/board.md | here | |
| SND | retroComputersDocs/computers/rk86/board.md | here | |
| ROMD | retroComputersDocs/computers/rk86/romdisk-module.md | here | |
| CLK | retroComputersDocs/computers/rk86/board.md | here | CLK-11 |
| IE4 | retroComputersDocs/computers/rk86/board.md | here | IE4-4, IE4-5 |
| CPU | retroComputersDocs/computers/rk86/board.md | here | CPU-5, CPU-7 |
| CPU | retroICs/ics/intel/8080a/record.md | external | |
| PPI | retroICs/ics/intel/8255a/record.md | external | |
| DMA | retroICs/ics/intel/8257/record.md | external | |
| CRT | retroICs/ics/intel/8275/record.md | external | |
| CLK | retroMachines/machines/rk86/ics/intel-8224/record.md | external | |
| IE4 | retroMachines/machines/rk86/ics/ti-sn7492/record.md | external | |
