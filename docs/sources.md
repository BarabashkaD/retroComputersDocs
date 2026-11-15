# Sources

Each bracket source ID used under `computers/`, once. Checked by `tools/check_records.py` of
`retroICs`: every bracket ID (Latin or Cyrillic capital first, or four digits first) in any markdown
file under `computers/` must be listed here. Rules for adding a source: `AGENTS.md`, "Adding a
source", and `retroICs/docs/sources-policy.md`.

- Home: the index that describes the document (provenance, licence check, SHA-256). The board
  sources of a computer and the data sheets of its board parts live in `computers/<name>/index.md`;
  the data sheets of the large chips (8080A, 8255A, 8257, 8275) live in the `datasheets/index.md`
  of their IC folder in `retroICs`. Every ID of the top table of a `computers/<name>/index.md` is
  listed here (`tools/tests/test_sources.py`).
- Kind: `vendor` (a data sheet, data book, user's manual or application note of the maker, Soviet
  reference sheets included), `board` (a schematic, PCB or magazine article of a board), `listing`
  (a ROM image or its listing, read as code), `comparison-only` (an emulator or another core: shows
  how others read a point, never a source of behaviour).

| ID | Home | Kind | Document |
|---|---|---|---|
| [R86] | computers/rk86/index.md | board | Радио 1986 No. 5, pp. 31-34: text and the main board schematic, Fig. 3 |
| [R86-4] | computers/rk86/index.md | board | Радио 1986 No. 4, pp. 24-26: architecture, memory map |
| [R86-6] | computers/rk86/index.md | board | Радио 1986 No. 6: the main board PCB insert |
| [R87-3] | computers/rk86/index.md | board | Радио 1987 No. 3, p. 32: the ROM module "ПЗУ для Бейсика" |
| [R87-5] | computers/rk86/index.md | board | Радио 1987 No. 5: the КР580ВГ75 replacement, reference tables |
| [K14] | computers/rk86/index.md | board | S. Kiselev, Radio-86RK re-make rev. 1.4: schematic and KiCad nets |
| [2716] | computers/rk86/index.md | vendor | Intel 2716 EPROM data sheet |
| [7474] | computers/rk86/index.md | vendor | TI SN7474 data sheet |
| [74198] | computers/rk86/index.md | vendor | TI SN74198 data sheet |
| [ИР13] | computers/rk86/index.md | vendor | К155ИР13 reference sheet |
| [ТМ2] | computers/rk86/index.md | vendor | К155ТМ2 reference sheet |
| [D8224] | computers/rk86/index.md | vendor | Intel 8224 clock generator data sheet, order 231464-001, November 1992 |
| [ГФ24] | computers/rk86/index.md | vendor | КР580ГФ24 reference sheet |
| [7490] | computers/rk86/index.md | vendor | TI SN7490A, SN7492A, SN7493A data sheet, SDLS940A |
| [ИЕ4] | computers/rk86/index.md | vendor | К155ИЕ4 reference sheet |
| [MON] | computers/rk86/index.md | listing | The RK86 monitor ROM `BIOS.BIN` (F800-FFFF) |
| [APG] | computers/rk86/index.md | comparison-only | MiSTer-devel/Apogee_MiSTer at `4b37da2`: `k580vt57.v`, `k580vg75.sv` |
| [MAME] | computers/rk86/index.md | comparison-only | mamedev/mame at `d077ea2`: `i8275.cpp`, `i8257.cpp`, `radio86.cpp` |
| [EMU] | computers/rk86/index.md | comparison-only | vpyk/emu80v4 at `a243b8e`: `Crt8275.cpp`, `Dma8257.cpp` |
| [C78] | retroICs/ics/intel/8080a/datasheets/index.md | vendor | Intel Component Data Catalog 1978: the 8080A, 8255A and 8257 data sheets; board parts 8212, 2708, 2716, 2116 |
| [D8255] | retroICs/ics/intel/8255a/datasheets/index.md | vendor | Intel 8255A data sheet |
| [D79] | retroICs/ics/intel/8275/datasheets/index.md | vendor | Intel 8275 data sheet 1979, 00224A, preliminary |
| [D84] | retroICs/ics/intel/8275/datasheets/index.md | vendor | Intel 8275 data sheet 1984, AFN-00224B/C |
