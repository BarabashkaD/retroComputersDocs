# Radio-86RK: sources

The sources that `board.md` and `romdisk-module.md` cite, and the entries of the documents whose
home is this index (registered in `docs/sources.md` of this repository). Fields and the checks
before a file is stored: `retroICs/docs/sources-policy.md`. Fields not printed in the document or
the record are "not recorded". Licence checks and hashes: 2026-11-15. Every file the entries use,
with its size and SHA-256, is in the table "Files" at the end (`tools/check_index.py`).

Files that are plain copies of Sergey Kiselev's repository are not stored here: they are read from
the submodule `sources/radio-86rk` (the fork `BarabashkaD/radio-86rk` of skiselev/radio-86rk, pinned
at c5e9cb7, the commit they were copied from). Their paths start with `sources/radio-86rk/` and are
relative to the repository root; the other paths are relative to this folder (the files stored
here: our own crops and net list).

| ID | Home | File | SHA-256 |
|---|---|---|---|
| [R86] | this index | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-32-33-Schematic.jpg` (and 2 pages; 6 crops stored here: Files) | 1a6e6b1707f5d9fdcb63c4ab52336fffe1d71e2b9d7141356658392b69daa7b7 |
| [R86-4] | this index | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-04-page-24-Computer_Architecture.jpg` (and 2 pages: Files) | fd1d1236ed34b6753b49397d3999b6616501f97692f2957cb31fc905232e0e83 |
| [R86-6] | this index | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-06-Insert_03-Mainboard_PCB.jpg` | 056249316830e08bb829ae5ab1ef6e0cbdde37cef6a1c3a74a5a268d2a9373cd |
| [R87-3] | this index | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-03-page-32-Games-ROM_Module.jpg` | 6159e3bdf6f84689766d017dd00d9a499650ba50af037a696512d8018008c779 |
| [R87-5] | this index | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-page-27-KR580VG75_Replacement.jpg` (and 2 pages, 2 inserts: Files) | 1b2c3bef6b56b227fb0ea273375e1d5f268af9720ac28507180dbe40ff3d01cc |
| [K14] | this index | `sources/radio-86rk/KiCad/Radio-86RK-Schematic-1.4.pdf` (and the KiCad sheets and notes in `sources/radio-86rk/`, the net list stored here: Files) | 2c0ffda9dd3d6f3ce728d91f4de853c6ea1021b977f8d5003953e02dc0af2e2e |
| [2716] | this index | | 9eb3796d547e99e245885f5b3e4e42f0ef405df1038298315c87e2838ae8820a |
| [7474] | this index | | 9349f8ace5398ec38534223f312a460f3de28f6bd1bf28d663cc01221384cbe9 |
| [74198] | this index | | 35724f70e829c33dee48da020f08a19f2c01b9f991f49931ba4a6ea1edc5972b |
| [ИР13] | this index | | c7f4b1d83e5d768793681f6a6cb16fa7734d1c88dbbdb40961253f54fd6c507c |
| [ТМ2] | this index | | 30fb87e313dcb20bd5775fb998eec5f428b2266e6fbebebfbe8a30bb3bb97564 |
| [D8224] | this index | `sources/radio-86rk/Documentation/Intel - 8224 - Clock Generator.pdf` | 93310c59e601354f9ba1de1c6f0625ba333c6e78d0145cc426be22cf1bb76b8e |
| [ГФ24] | this index | | a01544156fb13c83d2baa1e19a2b80b8c280464209efb31d9498739a0a32b9a2 |
| [7490] | this index | | 74feb14edf36a9cb5d819425b6baf28ea9fd9e88b04eb082a7fb228a209db7ad |
| [ИЕ4] | this index | | 337295e99b5caaa95d20ff53c9eabda50214b04a7bf71851e266c510e7c10ab6 |
| [MON] | this index | | b52bc01ce40fc03e4c6e2369b74e30ef9e9cebc6db73c03988d76587af3eb946 |
| [APG] | this index | | |
| [MAME] | this index | | |
| [EMU] | this index | | |
| [C78] | retroICs/ics/intel/8080a/datasheets/index.md | see home | see home |
| [D8255] | retroICs/ics/intel/8255a/datasheets/index.md | see home | see home |
| [D79] | retroICs/ics/intel/8275/datasheets/index.md | see home | see home |
| [D84] | retroICs/ics/intel/8275/datasheets/index.md | see home | see home |

[C78], the pages used for the board parts (its home lists the pages of the ICs): 8212 (PDF 526),
2708 4-40 (PDF 232), 2716 4-46 (PDF 238), 2116 3-109 (PDF 141); the 8224 11-24..11-27 (PDF
440-443), cited by the 8224 record (`retroMachines/machines/rk86/ics/intel-8224/record.md`).

The clock chips' sheets ([D8224], [ГФ24], [7490], [ИЕ4]): the 8224 and the 7492 / К155ИЕ4 have no
model in retroICs (it holds only the ICs it implements); they are modelled inside the RK86 clock
block in retroMachines, whose `machines/rk86/ics/` holds their records. Their data sheets are kept
here with the board's other source documents; they move to retroICs with their records when the
clock chips get models of their own.

## [R86]

| Field | Value |
|---|---|
| Title | the description of the «Радио-86РК» main board, rubric "Микропроцессорная техника" (the series «Персональный радиолюбительский компьютер «Радио-86РК»» begun in No. 4, [R86-4]); the article heading on p. 31 not recorded |
| Vendor | Радио (magazine), Moscow |
| Authors | Д. Горшков, Г. Зеленко, Ю. Озеров, С. Попов (D. Gorshkov, G. Zelenko, Yu. Ozerov, S. Popov), the series' authors, signed on No. 4 p. 26, No. 5 p. 34, No. 9 p. 28 |
| Document | Радио 1986 No. 5 ("РАДИО № 5, 1986 г." in the page footers) |
| Edition | May 1986 |
| Pages used | p. 31 (the start of the description), pp. 32-33 (Fig. 3, the main board schematic and its parts list, and the text of p. 32), p. 34 (text: DRAM control, the 8257 address latch, the display, LTEN, D4.1, the sound) |
| Origin | scans of the printed magazine; the scanner and date not recorded |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-31.jpg`, `...-page-32-33-Schematic.jpg`, `...-page-34.jpg` (added in ca63b57, 2022-06-15); byte-identical |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-32-33-Schematic.jpg (and the same folder for pp. 31, 34) |
| Licence | No licence or reproduction statement on the scanned pages (pp. 31-34 checked; the footer names the issue only). The repository it was copied from is GPL-3.0 for its own work; a magazine scan found there keeps the publisher's terms, not the GPL. No explicit ban: fit to store, with the issue and pages; not stored here, read from the submodule |
| SHA-256 | the scans are unchanged (JFIF headers only, no EXIF, XMP or comment segments): the hashes in Files are those of the files in the submodule at c5e9cb7, also the hashes as copied |
| File | in the submodule, `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/`: `Radio_Magazine-1986-05-page-31.jpg`, `Radio_Magazine-1986-05-page-32-33-Schematic.jpg`, `Radio_Magazine-1986-05-page-34.jpg` |
| Derived files | `magazines/radio-1986-05/r86_*.png` (6, stored here): crops of the pp. 32-33 scan (`sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-32-33-Schematic.jpg`), cut by the owner on 2026-11-09 (`r86_full.png` the whole spread at 1125 x 736; `r86_d2.png` D2 8257, `r86_d8.png`, `r86_d8b.png` D8 8275, `r86_video.png` the video path, `r86_wr.png` the WR gate D4.1); PNG with IHDR, pHYs, IDAT, IEND only (no text chunks); each is a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |

## [R86-4]

| Field | Value |
|---|---|
| Title | «Персональный радиолюбительский компьютер «Радио-86РК»», section "Архитектура компьютера", rubric "Микропроцессорная техника" (p. 24) |
| Vendor | Радио (magazine), Moscow |
| Document | Радио 1986 No. 4 ("РАДИО № 4, 1986 г.", p. 24 footer) |
| Edition | April 1986 |
| Pages used | p. 25 (block diagram Fig. 1), p. 26 (memory map Fig. 2; the DMA / CRT text; the refresh by the display DMA and the RESET limit; the control bus ЧТЕНИЕ, ЗАПИСЬ; the 8257 IORD → 8275 WR and MEMW → ЧТЕНИЕ); p. 24 (the start of the article) |
| Origin | scans of the printed magazine; the scanner and date not recorded |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-04-page-24-Computer_Architecture.jpg`, `...-page-25-...`, `...-page-26-...` (added in 4560d50, 2022-06-15); byte-identical |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-04-page-26-Computer_Architecture.jpg (and the same folder for pp. 24, 25) |
| Licence | No licence or reproduction statement on pp. 24-26 (checked). As [R86]: no explicit ban; read from the submodule, not stored here |
| SHA-256 | unchanged (JFIF headers only): the hashes in Files (of the files in the submodule) |
| File | in the submodule, `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/` (3 pages: Files) |

## [R86-6]

| Field | Value |
|---|---|
| Title | the main board PCB drawing, insert 3 |
| Vendor | Радио (magazine), Moscow |
| Document | Радио 1986 No. 6, insert |
| Edition | June 1986 |
| Pages used | the whole insert (kept for re-checks; not traced track by track: the facts it was to confirm are stated in the No. 5 text) |
| Origin | a scan of the printed insert; the scanner and date not recorded |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-06-Insert_03-Mainboard_PCB.jpg` (added in ca63b57, 2022-06-15); byte-identical |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-06-Insert_03-Mainboard_PCB.jpg |
| Licence | No licence or reproduction statement on the insert (checked). As [R86]: no explicit ban; read from the submodule, not stored here |
| SHA-256 | unchanged (JFIF headers only): the hash in Files (of the file in the submodule) |
| File | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-06-Insert_03-Mainboard_PCB.jpg` (in the submodule) |

## [R87-3]

| Field | Value |
|---|---|
| Title | "ПЗУ для Бейсика" (S. Popov): the ROM module on the interface PPI D14 |
| Vendor | Радио (magazine), Moscow |
| Document | Радио 1987 No. 3 |
| Edition | March 1987 |
| Pages used | p. 32 (schematic and text) |
| Origin | a scan of the printed page; the scanner and date not recorded |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-03-page-32-Games-ROM_Module.jpg` (added in ca63b57, 2022-06-15); byte-identical |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-03-page-32-Games-ROM_Module.jpg |
| Licence | No licence or reproduction statement on p. 32 (checked). As [R86]: no explicit ban; read from the submodule, not stored here |
| SHA-256 | unchanged (JFIF headers only): the hash in Files (of the file in the submodule) |
| File | `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-03-page-32-Games-ROM_Module.jpg` (in the submodule) |

## [R87-5]

| Field | Value |
|---|---|
| Title | "Если нет КР580ВГ75..." (a TTL replacement of the 8275 that "is not an exact functional analog"; not a source of 8275 behaviour), and the reference inserts 2 and 3 (the КР580ИК80А instruction set, hex tables, character codes) |
| Vendor | Радио (magazine), Moscow |
| Document | Радио 1987 No. 5 |
| Edition | May 1987 |
| Pages used | p. 27 (printed 22): VSP to the font ROM enable, the DRAM refresh by the 8275's DMA; pp. 28, 29 (printed 23, 24) and the inserts kept, not cited by item |
| Origin | scans of the printed pages and inserts; the scanner and date not recorded |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-page-27-KR580VG75_Replacement.jpg`, `...-page-28-...`, `...-page-29-...`, `Radio_Magazine-1987-05-Insert_2-Reference_Tables.jpg`, `...-Insert_3-...` (added in ca63b57, 2022-06-15); byte-identical |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-page-27-KR580VG75_Replacement.jpg (and the same folder for the others) |
| Licence | No licence or reproduction statement on the pages and inserts (checked). As [R86]: no explicit ban; read from the submodule, not stored here |
| SHA-256 | unchanged (JFIF headers only): the hashes in Files (of the files in the submodule) |
| File | in the submodule, `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/` (3 pages, 2 inserts: Files) |

## [K14]

| Field | Value |
|---|---|
| Title | Radio-86RK, rev. 1.4: schematic (5 sheets; sheet 4/5 "CRT_Memory"), KiCad sheets, the repository notes |
| Vendor | Sergey Kiselev ("Designed by Sergey Kiselev"; "Based on the previous work by Alexey Khudyakov and Radio magazine publications", sheet title block) |
| Document | skiselev/radio-86rk, `KiCad/Radio-86RK*.kicad_sch`, `KiCad/Radio-86RK-Schematic-1.4.pdf`, `README.md` (the Bill of Materials, memory map, connectors), `Project_Notes.md`, `Radio-86RK_Publications.md` |
| Edition | rev. 1.4, sheets dated 2023-12-09; the schematic PDF printed 2023-12-13 (its metadata) |
| Pages used | sheet 1/5 (CPU, bus), sheet 4/5 "CRT_Memory"; the nets of all sheets (`netlist-extracted.txt`) |
| Origin | github.com/skiselev/radio-86rk |
| Copied from | skiselev/radio-86rk at c5e9cb7 (2024-01-09): the KiCad sheets (added in 97d124b, 2022-05-13; last changed in 277d8b4, 2024-01-09), the schematic PDF (277d8b4), `README.md` (c5e9cb7), `Project_Notes.md` (cfba265), `Radio-86RK_Publications.md` (3ca358d); all byte-identical, read from the submodule |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/KiCad/Radio-86RK-Schematic-1.4.pdf (and the same tree for the other files) |
| Licence | The KiCad sheets and the schematic PDF state in their title block: "Licensed under CERN-OHL-S: https://cern-ohl.web.cern.ch", "Documentation and design files: https://github.com/skiselev/radio-86rk", "Radio-86RK is an open source hardware project". CERN-OHL-S exists in version 2 only: CERN-OHL-S-2.0 (`LICENSES/CERN-OHL-S-2.0.txt`); the schematic PDF and the KiCad sheets are read from the submodule. The notes (`README.md`, `Project_Notes.md`, `Radio-86RK_Publications.md`) carry no statement of their own; the repository's `LICENSE` is the GNU GPL version 3 text (`sources/radio-86rk/LICENSE`), so they are under GPL-3.0 there; read from the submodule, not stored here |
| SHA-256 | the schematic PDF: 2c0ffda9dd3d6f3ce728d91f4de853c6ea1021b977f8d5003953e02dc0af2e2e (as copied; the file of the submodule). The other files: Files |
| File | in the submodule: the schematic PDF `sources/radio-86rk/KiCad/Radio-86RK-Schematic-1.4.pdf`, the KiCad sheets `sources/radio-86rk/KiCad/*.kicad_sch` and the notes `sources/radio-86rk/README.md`, `Project_Notes.md`, `Radio-86RK_Publications.md`: Files |
| Derived files | `schematics/kiselev-1.4/netlist-extracted.txt` (stored here): the nets of the five KiCad sheets (`sources/radio-86rk/KiCad/*.kicad_sch`; its header's "of this folder" names the folder that held the sheets when it was made), one line per net (name, sheet labels, pins as `Ref.Pin(Name)`), extracted by the owner on 2026-11-08 (tool not recorded); a modified form of the design, so CERN-OHL-S-2.0, with a header naming the source and the change. SHA-256 as extracted (before the header and LF line ends): 4a905e147dca6b531db1766f09aa98386b978d29274fcfea6f8f4b6c38906c34 |

## [2716]

| Field | Value |
|---|---|
| Title | Intel 2716 16K (2K x 8) UV erasable PROM (`Intel - 2716.pdf`, 8 pages); scanned |
| Vendor | Intel |
| Document | not recorded |
| Edition | not recorded |
| Pages used | p. 5-4 (read AC table) |
| Origin | an Intel data book section |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Intel - 2716.pdf` (added in f44a0e3, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Intel%20-%202716.pdf |
| Licence | The PDF is encrypted with an owner password (permissions restricted), and the metadata rewrite would remove that protection. The repository it was copied from is GPL-3.0 for its own work; a vendor PDF found there keeps the vendor's terms, not the GPL. Status unclear: not stored ([C78] 4-46 has the same AC values) |
| SHA-256 | 9eb3796d547e99e245885f5b3e4e42f0ef405df1038298315c87e2838ae8820a (as copied; not stored) |
| File | |

## [7474]

| Field | Value |
|---|---|
| Title | SN5474, SN54LS74A, SN7474, SN74LS74A dual D-type flip-flops (`sn74ls74a.pdf`, 24 pages) |
| Vendor | Texas Instruments |
| Document | SDLS119 |
| Edition | "Copyright © 1988, Texas Instruments Incorporated" (p. 1); the PDF with its package addenda and notice made later |
| Pages used | p. 1 (function table, pinout) |
| Origin | Texas Instruments (ti.com) |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/sn74ls74a.pdf` (added in e90f2d5, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/sn74ls74a.pdf |
| Licence | Explicit ban. The "Important notice and disclaimer" page reads: "Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right." Not stored |
| SHA-256 | 9349f8ace5398ec38534223f312a460f3de28f6bd1bf28d663cc01221384cbe9 (as copied; not stored) |
| File | |

## [74198]

| Field | Value |
|---|---|
| Title | SN54198, SN54199, SN74198, SN74199 8-bit shift registers (`sn74198.pdf`, 11 pages) |
| Vendor | Texas Instruments |
| Document | SDLS078 (the file's metadata, read before the rewrite) |
| Edition | not recorded on the pages read; the notice page: "Copyright © 1998, Texas Instruments Incorporated" |
| Pages used | the function table ("mode controls should be changed only while the clock input is high"), clear and setup times (tw ≥ 20 ns, tPHL ≤ 35 ns, tsu 20 / 30 ns) |
| Origin | Texas Instruments (the PDF was made in December 1998) |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/sn74198.pdf` (added in e90f2d5, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/sn74198.pdf |
| Licence | TI copyright: "Copyright © 1998, Texas Instruments Incorporated" on the "IMPORTANT NOTICE" page, whose text covers product changes, warranty and patent licences only; it gives no permission to reproduce, and TI's later notice on [7474] (the same kind of document) forbids reproduction. Conservative ruling: not stored |
| SHA-256 | 35724f70e829c33dee48da020f08a19f2c01b9f991f49931ba4a6ea1edc5972b (as copied; not stored) |
| File | |
| Derived files | the record also cites `sn74198.md`, a Markdown transcription of this PDF kept with the maintainer's source collection; not stored here |

## [ИР13]

| Field | Value |
|---|---|
| Title | К155ИР13 (74198) (`k155ir13.pdf`, 2 pages) |
| Vendor | not recorded (no publisher named in the file) |
| Document | not recorded |
| Edition | not recorded |
| Pages used | pp. 1-2 (pins, mode table, load / shift text) |
| Origin | a reference sheet compiled from Soviet and Russian reference books; its literature list names А. В. Нефедов, "Интегральные микросхемы и их зарубежные аналоги", vol. 2, РадиоСофт, 1998, and Б. Л. Перельман, В. И. Шевелев, "Отечественные микросхемы и зарубежные аналоги", НТЦ Микротех, 1998 |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/k155ir13.pdf` (added in e90f2d5, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/k155ir13.pdf |
| Licence | No licence or copyright text and no publisher in the file (pp. 1, 2 checked); p. 1 says the sheet is "ознакомительной" (for information) and does not replace the official specification; the text is compiled from the 1998 reference books it lists. Status unclear: not stored |
| SHA-256 | c7f4b1d83e5d768793681f6a6cb16fa7734d1c88dbbdb40961253f54fd6c507c (as copied; not stored) |
| File | |

## [ТМ2]

| Field | Value |
|---|---|
| Title | К155ТМ2 (7474) (`k155tm2.pdf`, 2 pages) |
| Vendor | not recorded |
| Document | not recorded |
| Edition | not recorded |
| Pages used | pins, delays |
| Origin | a reference sheet set (not recorded which) |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/k155tm2.pdf` (added in e90f2d5, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/k155tm2.pdf |
| Licence | The PDF is encrypted with an owner password (permissions restricted), and the metadata rewrite would remove that protection. Status unclear: not stored |
| SHA-256 | 30fb87e313dcb20bd5775fb998eec5f428b2266e6fbebebfbe8a30bb3bb97564 (as copied; not stored) |
| File | |

## [D8224]

| Field | Value |
|---|---|
| Title | 8224 Clock Generator and Driver for 8080A CPU (`Intel - 8224 - Clock Generator.pdf`) |
| Vendor | Intel |
| Document | order number 231464-001 |
| Edition | November 1992 |
| Pages used | pp. 1-50..1-54 (PDF 1-5); scanned, no text layer |
| Origin | Intel (a data book section; the PDF was made in 2000 with Adobe Acrobat) |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/Intel - 8224 - Clock Generator.pdf` (added in f44a0e3, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/Intel%20-%208224%20-%20Clock%20Generator.pdf |
| Licence | No copyright notice and no statement on reproduction on the pages checked (1, 5); the copyright of the data book it comes from is not in the file. The repository it was copied from is GPL-3.0 for its own work; a vendor document found there keeps the vendor's terms, not the GPL. Not stored: read from the submodule |
| SHA-256 | 93310c59e601354f9ba1de1c6f0625ba333c6e78d0145cc426be22cf1bb76b8e (as copied; the file of the submodule) |
| File | `sources/radio-86rk/Documentation/Intel - 8224 - Clock Generator.pdf` (in the submodule) |

## [ГФ24]

| Field | Value |
|---|---|
| Title | КР580ГФ24 - Микросхема (`kr580gf24.pdf`, 2 pages) |
| Vendor | not recorded (a reference sheet set by ООО компания "Электроника и Связь", eandc.ru) |
| Document | not recorded |
| Edition | not recorded (the PDF was made in 2017) |
| Pages used | p. 2 (pin list, 27 MHz maximum, "phase period 9/fOP") |
| Origin | eandc.ru (its name, telephone and site in the page footer; checked on p. 1) |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/kr580gf24.pdf` (added in f44a0e3, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/kr580gf24.pdf |
| Licence | No licence text on p. 1 (checked), which carries the footer of ООО компания "Электроника и Связь" (eandc.ru). The PDF is encrypted with an owner password that forbids changes and text extraction, and the metadata rewrite would remove that protection. Status unclear: not stored |
| SHA-256 | a01544156fb13c83d2baa1e19a2b80b8c280464209efb31d9498739a0a32b9a2 (as copied; not stored) |
| File | |

## [7490]

| Field | Value |
|---|---|
| Title | "Decade, Divide-by-Twelve and Binary Counters": SN7490A, SN7492A, SN7493A, SN74LS90, SN74LS92, SN74LS93 (`sn74ls90.pdf`, 25 pages) |
| Vendor | Texas Instruments |
| Document | SDLS940A |
| Edition | "March 1974, revised March 1988" (page header); the PDF with its package addenda and notice was made in 2018 |
| Pages used | pp. 1-3, 7 (SN7492A) |
| Origin | Texas Instruments (ti.com, product page of the SN74LS90); TI's link serves a newer file today |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/sn74ls90.pdf` (added in f44a0e3, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/sn74ls90.pdf |
| Licence | Explicit ban. The "Important notice and disclaimer" page reads: "TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited." ("Copyright © 2018, Texas Instruments Incorporated"; p. 1: "Copyright © 1988, Texas Instruments Incorporated"). Not stored |
| SHA-256 | 74feb14edf36a9cb5d819425b6baf28ea9fd9e88b04eb082a7fb228a209db7ad (as copied; not stored) |
| File | |

## [ИЕ4]

| Field | Value |
|---|---|
| Title | К155ИЕ4, КМ155ИЕ4 (`k155ie4.pdf`, 2 pages) |
| Vendor | not recorded (a reference sheet set by ООО компания "Электроника и Связь", eandc.ru, from a scanned Soviet reference book) |
| Document | not recorded |
| Edition | not recorded (the PDF was made in 2017) |
| Pages used | p. 1 (truth table, notes 2, 3), p. 2 (delays) |
| Origin | eandc.ru (its name, telephone and site in the footer of pp. 1, 2) |
| Copied from | skiselev/radio-86rk at c5e9cb7, `Documentation/k155ie4.pdf` (added in f44a0e3, 2022-06-14) |
| Download | https://github.com/skiselev/radio-86rk/raw/c5e9cb7/Documentation/k155ie4.pdf |
| Licence | No licence text on pp. 1, 2 (both checked); each carries the footer of ООО компания "Электроника и Связь" (eandc.ru). The PDF is encrypted with an owner password that forbids changes and text extraction, and the metadata rewrite would remove that protection. Status unclear: not stored |
| SHA-256 | 337295e99b5caaa95d20ff53c9eabda50214b04a7bf71851e266c510e7c10ab6 (as copied; not stored) |
| File | |

## [MON]

| Field | Value |
|---|---|
| Title | the Radio-86RK monitor ROM, 2 KB (F800-FFFF; mirrored through E000-FFFF on the board, GLUE-1) |
| Vendor | the monitor of the Радио 1986 publication |
| Authors | Д. Горшков, Г. Зеленко, Ю. Озеров, С. Попов (D. Gorshkov, G. Zelenko, Yu. Ozerov, S. Popov): see [R86] and `retroMachines/machines/rk86/roms/PROVENANCE.md` |
| Document | `BIOS.BIN` of the Karabas fork; read as code (offsets are file offsets, addresses F800 + offset) |
| Edition | not checked yet against the published listing or a dump of an original ROM |
| Pages used | the routines the records cite by address |
| Origin | karabas-go-core-rk86 (`andykarpov/karabas-go-core-rk86`), `src/roms/BIOS.BIN`, unchanged since the first commit 75c091b (2024-09-14) |
| Copied from | `retroMachines/machines/rk86/roms/monitor.bin` (its `PROVENANCE.md`); the fork `BarabashkaD/karabas-go-core-rk86` at 35e86e7 (the commit `PROVENANCE.md` names), `src/roms/BIOS.BIN`, byte-identical; the same bytes at d995355 |
| Download | https://github.com/BarabashkaD/karabas-go-core-rk86/raw/35e86e7dfdeae112873a5d727bdd5f5bd67e0e97/src/roms/BIOS.BIN |
| Licence | Not checked yet (`retroMachines/machines/rk86/roms/PROVENANCE.md`): the fork names its repository licence for it; the status of the original publication's code is open. Listed, not stored here: its home as a file is `retroMachines` |
| SHA-256 | b52bc01ce40fc03e4c6e2369b74e30ef9e9cebc6db73c03988d76587af3eb946 (2048 bytes) |
| File | |

## [APG]

| Field | Value |
|---|---|
| Title | Apogee BK-01 core for MiSTer: `rtl/k580vt57.v`, `rtl/k580vg75.sv` |
| Vendor | MiSTer-devel/Apogee_MiSTer |
| Document | commit `4b37da2` |
| Edition | `4b37da2` |
| Pages used | the line numbers the records cite |
| Origin | https://github.com/MiSTer-devel/Apogee_MiSTer |
| Copied from | not copied (comparison-only: re-fetchable by commit) |
| Download | https://github.com/MiSTer-devel/Apogee_MiSTer/tree/4b37da2 |
| Licence | not checked: not stored. comparison-only, never a source of behaviour |
| SHA-256 | none (not stored) |
| File | |

## [MAME]

| Field | Value |
|---|---|
| Title | MAME: `src/devices/video/i8275.cpp`, `i8275.h`, `src/devices/machine/i8257.cpp`, `src/mame/ussr/radio86.cpp`, `radio86_m.cpp` |
| Vendor | mamedev/mame |
| Document | master at `d077ea2` (`i8275.cpp` last changed in `ef548b3`, 2026-08-07) |
| Edition | `d077ea2` |
| Pages used | the line numbers the records cite |
| Origin | https://github.com/mamedev/mame |
| Copied from | not copied (comparison-only: re-fetchable by commit) |
| Download | https://github.com/mamedev/mame/tree/d077ea2 |
| Licence | not checked: not stored. comparison-only, never a source of behaviour |
| SHA-256 | none (not stored) |
| File | |

## [EMU]

| Field | Value |
|---|---|
| Title | Emu80 v4: `src/Crt8275.cpp`, `src/Dma8257.cpp` |
| Vendor | vpyk/emu80v4 |
| Document | commit `a243b8e` (2026-11-04) |
| Edition | `a243b8e` |
| Pages used | the line numbers the records cite |
| Origin | https://github.com/vpyk/emu80v4 |
| Copied from | not copied (comparison-only: re-fetchable by commit) |
| Download | https://github.com/vpyk/emu80v4/tree/a243b8e |
| Licence | not checked: not stored. comparison-only, never a source of behaviour |
| SHA-256 | none (not stored) |
| File | |

## Files

Every file the entries use. A path relative to this folder: stored here. A path starting with
`sources/radio-86rk/`: relative to the repository root, a file of the submodule at its pinned
commit, not stored here (`tools/check_index.py` hashes the blob at that commit). Licence: the terms
each file is under (texts in `LICENSES/` of the repository root, or, for the submodule's GPL-3.0
notes, `sources/radio-86rk/LICENSE`); "magazine" and "vendor" = no licence stated, per the entry
above.

| File | ID | Size | SHA-256 | Licence |
|---|---|---|---|---|
| `magazines/radio-1986-05/r86_d2.png` | [R86] (derived) | 478579 | ca79bc82698567a24f9fa568a0a2d78b728b846bca6a7f7f7e8bdcfe4791914f | a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |
| `magazines/radio-1986-05/r86_d8.png` | [R86] (derived) | 582668 | c54fb563d3432520c8af5780b040f6a997b8be05fb0328fbc7f6592c2a16a3b5 | a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |
| `magazines/radio-1986-05/r86_d8b.png` | [R86] (derived) | 85177 | b5eff53f7d76e99f6aeeb17d3c23c53287bb3617e6d2cc42c022799232a8c60d | a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |
| `magazines/radio-1986-05/r86_full.png` | [R86] (derived) | 597463 | 20a8eaf24467caadee73f4888d6356b06bbb2b820ffe6e3a127eb9ecfa881491 | a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |
| `magazines/radio-1986-05/r86_video.png` | [R86] (derived) | 676228 | 9a07cabe47f3cbd6e1fe6779dcfe1a5adc4cf0c58d60d51d253a1d43917760b6 | a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |
| `magazines/radio-1986-05/r86_wr.png` | [R86] (derived) | 404978 | 1e8f3bbee0c3e45080b25c426283d17fe4f9501bf9a9bb95b22c61d42d8b6ca6 | a crop of the magazine page; it keeps the magazine's status (the owner claims no rights in it) |
| `schematics/kiselev-1.4/netlist-extracted.txt` | [K14] (derived) | 15612 | 704e5a8db5e3863b09c1dd5f308ac2483682def7de0e6ffd2aadd493094e042b | CERN-OHL-S-2.0 (the owner's extraction) |
| `sources/radio-86rk/Documentation/Intel - 8224 - Clock Generator.pdf` | [D8224] | 228195 | 93310c59e601354f9ba1de1c6f0625ba333c6e78d0145cc426be22cf1bb76b8e | vendor |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-04-page-24-Computer_Architecture.jpg` | [R86-4] | 1614256 | fd1d1236ed34b6753b49397d3999b6616501f97692f2957cb31fc905232e0e83 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-04-page-25-Computer_Architecture.jpg` | [R86-4] | 1283295 | b8b1687ddcaa7af2087046b660daa2a0ad1941bcd2c092b2eb48394c26e1cdb9 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-04-page-26-Computer_Architecture.jpg` | [R86-4] | 1380782 | 9cb7138b80c14b5b78f6688c12f703ba2f2b13e16747bb09c72846fdd58032a0 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-31.jpg` | [R86] | 1612841 | f6d05b5c6d49da3c46e32e8b73ec51c252124a72ad51625d24f63e07977b0434 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-32-33-Schematic.jpg` | [R86] | 1166041 | 1a6e6b1707f5d9fdcb63c4ab52336fffe1d71e2b9d7141356658392b69daa7b7 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-05-page-34.jpg` | [R86] | 1769088 | 0f59e7fa3fd91b24f4d8ef5417dd59232cf323850f276a82adfa69b796460472 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1986-06-Insert_03-Mainboard_PCB.jpg` | [R86-6] | 2441361 | 056249316830e08bb829ae5ab1ef6e0cbdde37cef6a1c3a74a5a268d2a9373cd | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-03-page-32-Games-ROM_Module.jpg` | [R87-3] | 1727989 | 6159e3bdf6f84689766d017dd00d9a499650ba50af037a696512d8018008c779 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-Insert_2-Reference_Tables.jpg` | [R87-5] | 1803147 | ef47f095d4884f68edeb908b0bd9a203dbad7e090082bafcd83b0c31f6b275f7 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-Insert_3-Reference_Tables.jpg` | [R87-5] | 2158791 | d5fb256c323a32ce245796ad7a33fce425ea110eadbe4bb61fd1cc93dcfa3bf6 | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-page-27-KR580VG75_Replacement.jpg` | [R87-5] | 1941171 | 1b2c3bef6b56b227fb0ea273375e1d5f268af9720ac28507180dbe40ff3d01cc | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-page-28-KR580VG75_Replacement.jpg` | [R87-5] | 1709841 | 10e08cb7f7b1c7fa09651da5e6f3a49527f58d4823f4c7b73fea1b4d55d277da | magazine |
| `sources/radio-86rk/Documentation/Radio_Magazine-Radio-86RK/Radio_Magazine-1987-05-page-29-KR580VG75_Replacement.jpg` | [R87-5] | 1764890 | 8ca386910584063c9e3eb53ae0fb10eef3962118c73d157feb1c2393c65cd367 | magazine |
| `sources/radio-86rk/KiCad/Radio-86RK-CRT-Mem.kicad_sch` | [K14] | 232896 | 250f53216db91ca023d180294919d0473cfb0d4fa66afd66eb9853d2bcebc780 | CERN-OHL-S-2.0 |
| `sources/radio-86rk/KiCad/Radio-86RK-IO.kicad_sch` | [K14] | 206261 | c55745f25320dde27cdefa02dd61817ed97a01da20ef61b1179bd1fb0c6ce2ad | CERN-OHL-S-2.0 |
| `sources/radio-86rk/KiCad/Radio-86RK-Keyboard.kicad_sch` | [K14] | 214736 | 797f9714d659aac979560118cf841270f49583c1f94d67688a67b836f4ad5b1d | CERN-OHL-S-2.0 |
| `sources/radio-86rk/KiCad/Radio-86RK-Power.kicad_sch` | [K14] | 197055 | 59a4a006febb97ac48c22e15fa48984f4730c4de337fe401efa2c607cab86eb7 | CERN-OHL-S-2.0 |
| `sources/radio-86rk/KiCad/Radio-86RK-Schematic-1.4.pdf` | [K14] | 838783 | 2c0ffda9dd3d6f3ce728d91f4de853c6ea1021b977f8d5003953e02dc0af2e2e | CERN-OHL-S-2.0 |
| `sources/radio-86rk/KiCad/Radio-86RK.kicad_sch` | [K14] | 316170 | bc43d48db84dcd35d120df84318a783464f743b2d6f9d8f89634e89eeef4023b | CERN-OHL-S-2.0 |
| `sources/radio-86rk/Project_Notes.md` | [K14] | 5028 | 4e4396364621a26013389ca8dcf75d4d6c267f43d877b15df94c168d0ad0362e | GPL-3.0 |
| `sources/radio-86rk/Radio-86RK_Publications.md` | [K14] | 16594 | dea2142794a688d71558c2768cd26442e29bf255402e25de02ebd8f3b3c1b10c | GPL-3.0 |
| `sources/radio-86rk/README.md` | [K14] | 26546 | a298698198ff28fe9ddf9f20b5fde2a6e86ec44031c0e2caeebc43bc485b5bc4 | GPL-3.0 |
