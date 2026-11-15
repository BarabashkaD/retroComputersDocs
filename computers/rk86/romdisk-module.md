# Radio-86RK ROM module of Радио 1987 No. 3: board record

The ROM module ("ПЗУ для Бейсика") that Радио 1987 No. 3 connects to the interface PPI D14 of the
main board (A000-BFFF, `board.md` GLUE-1), with its IDs (ROMD). It describes the published module
only; other ROM disk wirings (Kiselev's cartridge, an FPGA platform's emulation) are not this
record's.

## Sources

Source: [R87-3] p. 32, "ПЗУ для Бейсика" (S. Popov), schematic and text (render
`Radio_Magazine-1987-03-page-32-Games-ROM_Module_p01_c36_30_97_60.png`); the main board [R86].

Not sources of behaviour: emulators and other FPGA cores ([MAME], [EMU], [APG]: comparison-only).

The documents, their provenance and licence checks: `index.md` of this folder; the source IDs are
registered in `docs/sources.md` of this repository.

## Notation

The original IDs are kept; new functions are numbered after them. GLUE-n are defined in `board.md`,
PPI-n in `retroICs/ics/intel/8255a/record.md`. Renders cited by name are page crops of the scans
(in the submodule `sources/radio-86rk`, see `index.md`), kept with the maintainer's source
collection, not in this repository (`<scan>_pNN` = page NN
of the scan; `_cA_B_C_D` = a crop in percent of the page: left, top, right, bottom; `...` stands for
`Radio_Magazine-1986-05-page-32-33-Schematic_p01`). Researched 2026-11-10.

## Items (ROMD-n)

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| ROMD-1 | The PPI | The interface PPI D14 (A000-BFFF, GLUE-1), its ports to the external connector: "Channel A of PPA D14 serves for data input, channels B and C for the output of the ROM address and for the read signal" | [R87-3] text; [R86] crop `..._c50_36_70_66.png` (D14 ports to the connector lines 1-24) |
| ROMD-2 | Address | PB0-PB7 → A0-A7 of every ROM; PC0-PC2 → A8-A10; PC3-PC5 → DD9 К555ИД7 A0-A2 (pins 1-3); DD9 Y0-Y7 → CS̄1-CS̄8 → the CE̅ (pin 18) of DD1-DD8 (К573РФ5, 2K × 8 each; К573РФ2, РФ4, К556РТ5, РТ7 also allowed "with their particulars and pinouts"): 16 KB = PC5..PC3 : PC2..PC0 : PB as A13..A0 | [R87-3] schematic |
| ROMD-3 | Select | DD9 G1 (6) at +5 V, G2A and G2B (4, 5) ← PC6: a ROM is selected only while PC6 = 0 (PC6 acts as A14 = 0; with PC6 = 1 no ROM drives the data lines). Not always enabled | [R87-3] schematic |
| ROMD-4 | Read strobe | PC7 → OE̅ (pin 20) of all ROMs: the selected ROM drives PA only while PC7 = 0 | [R87-3] schematic, text ("the read signal") |
| ROMD-5 | Data | ROM D0-D7 → PA0-PA7 (the PPI reads them in mode 0 input) | [R87-3] schematic |
| ROMD-6 | Floating pins | No pull-up or pull-down on any line of the module or of D14's ports. While a port is an input (after RESET, GLUE-9), the ИД7 inputs, the EPROM address / OE̅ inputs and PA float | [R87-3] schematic; [R86] |

## Assumptions checked

Model assumptions (ROMD):

- The planned ROM disk wiring "PB → A0-A7, PC0-PC6 → A8-A14, PA ← D0-D7, PC7": differs in form:
  PC3-PC5 go through a К555ИД7 to eight chip selects and PC6 is the decoder's active-low enable;
  functionally PB / PC0-PC5 form A0-A13, PC6 = 0 is required (no ROM answers with PC6 = 1, i.e.
  A14 = 1 reads a floating port), and PC7 = 0 is the output enable (no ROM drives PA with PC7 = 1).
  A model that answers every address with PC7 ignored differs from the board.
- The level of floating 8255 pins: silent (ROMD-6; the 8255 data sheet: an input pin is high
  impedance, ±10 µA, no pull-up specified, PPI-33).

## SILENT (ROMD)

- ROMD-6: what the PPI reads on PA when no ROM is enabled, and what the TTL / EPROM inputs do while
  the PPI's ports are inputs (no pull-ups; the К555 and К573РФ5 data sheets for floating inputs are
  not in the collection).

## Hardware checks

None planned.
