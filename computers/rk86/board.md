# Radio-86RK main board: board record

The board items of the Radio-86RK: how the chips of the Радио 1986 board (and of Sergey Kiselev's
rev. 1.4 re-make, for comparison) are wired, and what that wiring gives at the machine level. The
data sheet items of the 8080A, 8255A, 8257 and 8275 are in `retroICs` (`ics/intel/<part>/record.md`:
CPU, PPI, DMA, CRT); those of the clock chips, the 8224 and the К155ИЕ4 / 7492, are in
`retroMachines` (`machines/rk86/ics/intel-8224/record.md`, `machines/rk86/ics/ti-sn7492/record.md`:
CLK, IE4). This record holds the board items with their IDs: VID, GLUE, MEM, TAPE, SND; the board
items of the clock chips (CLK-11, IE4-4, IE4-5); the CPU pins whose items are board wiring only
(CPU-5, CPU-7); and the board halves of the chips' items (each says which item it comes from, "From
CPU-1"). The ROM module of Радио 1987 No. 3 is in `romdisk-module.md`. This record describes the
original boards only; an FPGA platform's address map or its emulation of add-ons is platform
material.

## Sources

- The original: Радио 1986 No. 5, pp. 32-33, Fig. 3 (the main board schematic and its parts list)
  [R86]; the text pp. 31-34. The 1986 text uses the early names КР580ИК80А, ИК57, ИК55 (later sold as
  КР580ВМ80А, ВТ57, ВВ55А). The architecture: Радио 1986 No. 4, pp. 24-26 [R86-4]. The PCB insert of
  Радио 1986 No. 6 [R86-6] (kept, not traced track by track).
- Kiselev's board 1.4 [K14]: the Bill of Materials in `README.md` of skiselev/radio-86rk
  (`sources/radio-86rk/README.md`, the submodule), `KiCad/Radio-86RK-Schematic-1.4.pdf` and the
  nets of the KiCad sheets (`netlist-extracted.txt`).
- Радио 1987 No. 5 [R87-5]: the КР580ВГ75 replacement article (not a source of 8275 behaviour; it
  confirms VSP to the font ROM enable and the DRAM refresh by the 8275's DMA).
- Vendor data sheets of the board parts: [C78] (2708 4-40, PDF 232; 2716 4-46, PDF 238; 2116 3-109,
  PDF 141; 8212, PDF 526), [2716], [7474], [74198], [ИР13], [ТМ2]; of the clock chips: [D8224],
  [ГФ24], [7490], [ИЕ4] (indexed here; their records:
  `retroMachines/machines/rk86/ics/intel-8224/record.md`,
  `retroMachines/machines/rk86/ics/ti-sn7492/record.md`); of the large chips, where a board half
  cites them: [C78], [D8255], [D79], [D84] (indexed in `retroICs`).
- The monitor ROM [MON].

Not sources of behaviour: emulators and other FPGA cores ([MAME], [EMU], [APG]: comparison-only).

The documents, their provenance and licence checks: `index.md` of this folder; the source IDs are
registered in `docs/sources.md` of this repository.

## Notation

The original IDs are kept; new functions are numbered after them. The board half of a chip's item
takes the next free number of the board prefix and names the item it comes from ("From CPU-1"); the
data sheet half keeps that ID in the chip's record. IDs of other prefixes: CPU-n, PPI-n, DMA-n,
CRT-n are defined in the `retroICs` records (`ics/intel/8080a/record.md`, `8255a/`, `8257/`,
`8275/`), CLK-n and IE4-n in the `retroMachines` records named under Sources; CPU-5, CPU-7, CLK-11,
IE4-4 and IE4-5 here. The timing sections of the chips' records are cited by their headings: the
8257 record's "Timing (data sheet)" ("Transfer states", "HOLD overhead with an 8080A") and the
8275 record's "Timing (data sheet)". An oscillator period is one period of the 16 MHz crystal of
the 8224 (62.5 ns, CLK-11); a Φ cycle is 9 of them ([D8224]; [ГФ24] p. 2, "phase period 9/fOP");
ИЕ4 counts 0..11 as in IE4-1. Researched 2026-11-10.

Renders cited by name are page crops of the scans (in the submodule `sources/radio-86rk`, see
`index.md`), kept with the maintainer's source collection, not in this repository; each can be cut
again from the scan it names
(`<scan>_pNN` = page NN of the scan; `_cA_B_C_D` = a crop in percent of the page: left, top, right,
bottom; `...` stands for `Radio_Magazine-1986-05-page-32-33-Schematic_p01`).

## Parts

| Function | Original (1986) | Kiselev 1.4 |
|---|---|---|
| CPU | D6 КР580ИК80А | U1 8080A / КР580ВМ80А |
| Clock generator | D1 КР580ГФ24 | U2 8224 / КР580ГФ24 |
| DMA controller | D2 КР580ИК57 | U7 8257 / КР580ВТ57 |
| CRT controller | D8 КР580ВГ75 | U8 8275 / КР580ВГ75 |
| PPI, keyboard and tape | D14 КР580ИК55 | U5 8255A / КР580ВВ55А |
| PPI, expansion port (ROM disk) | D20 КР580ИК55 | U6 8255A / КР580ВВ55А |
| Monitor ROM, 2 KB | D17 К573РФ5 (2716) | U10 2716 / КР573РФ5 |
| Font ROM | D12 К573РФ1 (1 KB, 2708) | U11 2716 (2 KB: two fonts, switched by GPA0) |
| RAM | D22-D29 К565РУ3, 8 DRAM 16K x 1 = 16 KB (16 chips for 32 KB) | U9 AS6C62256, one SRAM 32K x 8 |
| DRAM address multiplexers | D18, D19 К555КП11 | not needed |
| DRAM RAS/CAS sequencer | D16 К155ИР1 | not needed |
| DMA high-address latch | D7 К589ИР12 | U12 74LS373 / К555ИР22 |
| Address decoder | D11 К555ИД7 | U14 74LS138 / К555ИД7 |
| Video shift register | D15 К155ИР13 | U13 74198 / К155ИР13 |
| Dot-clock divider | D3 К155ИЕ4 | U15 7492 / К155ИЕ4 |
| D flip-flops (start-up block and others) | D13 К155ТМ2 | U17 7474 / К155ТМ2 |
| XOR (ЧТЕНИЕ = DBIN XOR MEMW) | D5 К155ЛП5 | U16 7486 / К155ЛП5 |
| AND | D4 К155ЛИ1 | U18 7408 / К155ЛИ1 |
| Inverters | D9 К155ЛН1 | U19 7404 / К155ЛН1 |
| NAND | D10 К155ЛА3 | U20 7400 / К155ЛА3 |
| Op-amp (tape input) | D21 К140УД6 | U21 TL071 / К140УД6 |
| USART (serial) | none (a separate board, Радио 1989 No. 6-7) | U3 8251A / КР580ВВ51А |
| Timer (sound, serial clock) | none (a separate article, Радио 1987 No. 11) | U4 8253 / КР580ВИ53 |
| RS-232 receiver, drivers | none | U22 SN75154 / К170УП2; U23, U24 SN75150 / К170АП2 |
| Power | an external -5 / +12 V supply | U25 LM7905 regulator; U26 DC-DC converter for +12 / -5 / -12 V |

The original has 29 chips with 16 KB of DRAM and no serial port or timer. Kiselev's board has 26:
one SRAM replaces the DRAM, its multiplexers and its sequencer; the font ROM is doubled; the serial
port, the timer and the power converters are on the board.

Corrections to this table (the rows are kept as first written):

- The two PPI rows of the original are swapped: on the Радио 1986 board the keyboard / tape PPI is
  D20 (8000-9FFF; its PC0 drives the tape output, its PC4 takes the tape comparator D21) and the
  interface PPI is D14 (A000-BFFF; the ROM module of [R87-3] is wired to "PPA D14"): [R86] p. 32
  ("outputs 4-7 of D11 select D20, D14, D8 or D2"), crops `..._c66_40_90_82.png`,
  `..._c50_36_70_66.png`; the Fig. 3 table names "PA0 (D14)" on the connector lines 1-24 and
  "PA0 (D20)" on line 45.
- Power on [K14]: U26 gives +12 V and -12 V, and U25 (LM7905) makes -5 V from -12 V (nets `+12V`:
  U26.6 +VOUT; `-12V`: U26.8 -VOUT, U25.2 VI; `-5V`: U25.3 VO).

The CPU and DMA bus logic is the same on both boards: DMA HRQ (pin 10) goes straight to CPU HOLD
(pin 13), CPU HLDA (pin 21) goes straight to DMA HLDA (pin 7); no 8228 bus controller; the memory
read strobe ЧТЕНИЕ is DBIN XOR MEMW of the DMA, the memory write strobe is the CPU's WR alone (Радио
1986 No. 4 p. 26, No. 5 pp. 32-34; Kiselev 1.4 sheet 1/5). The 8080 takes HOLD only in T2 and gives
the bus away after T3 of a write, so a CPU write always ends before the DMA's first read (INS8080A
datasheet p. 5).

## CPU: the 8080A pins on the board

Two CPU items are board wiring only and keep their IDs here (CPU-5, CPU-7); the data sheet items of
the 8080A are in `retroICs/ics/intel/8080a/record.md`. The board halves of CPU-1, CPU-2, CPU-3,
CPU-4 and CPU-6 are GLUE-14..GLUE-18, that of CPU-8 is MEM-8.

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| CPU-5 | SYNC (19) | → 8224 SYNC (pin 5) (STSTB unused) | [K14] netlist; [R86] crop `..._c34_13_55_50.png` |
| CPU-7 | WR (18) | ЗАПИСЬ: memory write (DRAM / SRAM WE), PPI WR, 8257 IOW (pin 2), the 8275 WR gate (GLUE-6), [R86] the DRAM sequencer start (D4.4). Memory write strobe = the CPU WR alone | [R86-4] p. 26; [R86] p. 34 text; [K14] ~WR net |

## The 8275 pins on the boards

| 8275 pin | Радио 1986 No. 5 Fig. 3, D8 КР580ВГ75 [R86] | Kiselev 1.4, U8 [K14] |
|---|---|---|
| LA0 (39) | not connected (not drawn on D8) | not connected (no-connect flag) |
| LA1 (38) | not connected | not connected |
| HGLT (32) | not connected | not connected |
| GPA0 (33) | not connected | U11 (font EPROM) A10: second font |
| GPA1 (34) | not connected | JP2 pin 4 (font EPROM type jumper) |
| VSP (35) | D12 К573РФ1 (font ROM) CS, pin 20: dots all dark | U11 ~CE, pin 20 |
| LTEN (37) | D13.1 К155ТМ2 D, pin 12, clocked with the shift register load strobe; its output clears D15 К155ИР13 (R, pin 13): the whole cell line lit, re-timed to the dots | U17A D, pin 2, clears U13 74198 (CLR, pin 13) |
| RVV (36) | not connected | U16D 7486 pin 13: XOR with the inverted shift register output, to the video |
| WR (10) | D4.1 К155ЛИ1 output, pin 3; its inputs (pins 1, 2) cannot be traced at the scan resolution | U18D 7408 pin 11 = CPU ~WR AND 8257 ~IOR (U7 pin 1) |
| DACK (6) | D2 КР580ИК57 DACK2, pin 14 | U7 DACK2, pin 14 |
| RD (9) | the system read line ЧТЕНИЕ (D5.1, DBIN XOR 8257 MEMW; text p. 32) | ~RD = U16A pin 3 (DBIN XOR ~MEMW) |
| CS (22) | the address decoder (D11 К555ИД7 with D5.3, D10.4, D4.3, A13-A15; text p. 32); the exact output not traced | U14 74LS138 O4 (A15 = 1, A14..A12 = 100) |
| HRTC (7) | D5.2 К155ЛП5 pin 5: XOR with VRTC, then D9.3, R16 to the video transistor V2 (composite sync); not re-timed | U16B pin 5, U19 inverter, R5 to Q1 |
| VRTC (8) | D5.2 pin 4 | U16B pin 4 |
| also | DRQ (5) to D2 DRQ2 (17); CCLK (30) from D3 К155ИЕ4 pin 8 (16 MHz / 12); IRQ (31), LPEN (11), LC3 (1) not connected | the same nets on U7, U15; IRQ, LPEN, LC3 not connected |

Video path [R86]: D12 D0-D5 (pull-ups R6-R11) to D15 D0-D5; D15 shifts at 8 MHz (D3 pin 12 to C,
pin 11) and Q5 (pin 16) goes through D9.4 and R15 to V2. [K14] is the same with RVV XORed in (U16D)
and the font bank on GPA0. The dots of a character leave D15 one character time after its code (ROM
access, then the load at the next character boundary); LTEN (D13.1) and VSP (ROM CS) follow the
dots, HRTC and VRTC do not.

Corrections to this section (researched 2026-11-10, with the full board items below): the 8275 CS
on [R86] is D11 Y6 (C000-DFFF) (GLUE-1, GLUE-7), and the inputs of the WR gate D4.1 are the CPU WR
(ЗАПИСЬ) and the 8257 IOR ([R86] p. 34 text; GLUE-6).

The 8275 on the board, against its data sheet items (`retroICs/ics/intel/8275/record.md`):

- CCLK: the RK86 CCLK (16 MHz / 12 = 750 ns) is within both (tCLK ≥ 480 ns for the 8275, ≥ 320 ns
  for the 8275-2). From CRT-54.
- The plain 8275's tHR, tLC, tAT, tVR (200, 400, 275, 275 ns) against the 8275-2's (150, 250, 250,
  250): no effect at the RK86 CCLK of 750 ns. From CRT-53.
- On the RK86 LA0 and LA1 are not connected, so only the VSP and LTEN columns of the character
  attribute table reach the dots (the table: the 8275 record, "Timing (data sheet)").

## Clock chips on the board (CLK, IE4)

The data sheet items CLK-1..CLK-10 and IE4-1..IE4-3 are in
`retroMachines/machines/rk86/ics/intel-8224/record.md` and
`retroMachines/machines/rk86/ics/ti-sn7492/record.md`.

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| CLK-11 | Board use | [R86] D1 КР580ГФ24 and [K14] U2 8224, Z1 / Y1 16 MHz: Φ1, Φ2 → 8080; Φ2 (TTL) → 8257 CLK (pin 12) (and on [K14] the 8251 and 8253 clocks); OSC → ИЕ4 CKA (pin 14) and on [R86] the DRAM sequencer D16 (C1, C2); READY → 8080 READY (23) and 8257 READY (6); RESET → 8080 RESET (12), 8257 RESET (13), the PPIs (35), the start-up flip-flop (GLUE-12); SYNC ← 8080 SYNC (19); RDYIN pulled high ([R86] R3 1 kΩ, [K14] R6), so READY is always high; RESIN from an RC network with a diode ([R86] R1, C2, V1 КД503А; [K14] SW68, C43, U27 supervisor); STSTB not connected (R86: a stub at pin 7; K14: U2.7 no net) | [R86] crop `..._c34_13_55_50.png`, `..._c36_8_60_19.png`; [K14] netlist (OSC, TTL_CLK, READY, RESET nets) |
| IE4-4 | Board wiring | CKA (pin 14) ← 8224 OSC (16 MHz); CKB (pin 1) ← QA (pin 12); QA → ИР13 / 74198 clock (pin 11): 8 MHz; QD (pin 8) → 8275 CCLK (pin 30): 1.333 MHz, high in counts 6-11, CCLK↓ at 11→0; QC (pin 9) and QD → AND [R86] D4.2 (К155ЛИ1, pins 5 and 4 → 6) / [K14] U18C (7408, pins 10 and 9 → 8) = the shift register mode input S1 and the ТМ2 clock (VID-2, VID-4): high in counts 10 and 11; QB (pin 11) not connected | [R86] D3, D4.2 (crop `..._c35_63_60_95.png`); [K14] U15, U18C (netlist; render `Schematic-1.4_p04_c38_50_98_86.png`) |
| IE4-5 | Load strobe states | S1 = QD·QC is high in counts 10, 11; the only QA↑ (CKA↓ that makes QA 0→1) with S1 high is the transition 10 → 11, one oscillator period before CCLK↓ (11 → 0). The planned model's `LOAD_STATE = 10` (the count before that `ce16`) | IE4-1, IE4-4 |

## VID: the video path up to the composite mixer

The record ends at the digital inputs of the composite mixer: the analogue mixer and the monitor
are named, not traced.

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| VID-1 | Font ROM address | [R86] D12 К573РФ1 (1K × 8, 2708 type): A0 (8) ← LC0 (8275 pin 4), A1 (7) ← LC1 (3), A2 (6) ← LC2 (2), A3..A9 (5, 4, 3, 2, 1, 23, 22) ← CC0..CC6 (23..29); LC3 (1) not connected. [K14] U11 (2716 / 2732 / 2764 by JP2): A0-A2 ← LC0-LC2, A3-A9 ← CC0-CC6, A10 ← GPA0 (second font), A11 via JP2, A12 = GND, ~OE = GND. Font address = {CC6..CC0, LC2..LC0} (GPA0 = 0 selects the first font on [K14]) | [R86] crop `..._c35_63_60_95.png`; [K14] netlist (U11) |
| VID-2 | Shift register load (`LOAD_STATE`) | [R86] D15 К155ИР13 / [K14] U13 74198: CLK (11) ← ИЕ4 QA, positive edge; S0 (1) high (R12 20 kΩ / RN1), S1 (23) = QD·QC (IE4-4). S0 S1 = H H: synchronous parallel load at CLK↑; H L (S0 high, S1 low): shift right (QA→QH) at CLK↑. So the register loads at the QA↑ of the transition 10 → 11 (one oscillator period before CCLK↓) and shifts at the other five QA↑ (0→1, 2→3, 4→5, 6→7, 8→9): `LOAD_STATE = 10`. The load takes the ROM data of the character output at the CCLK↓ 11 oscillator periods earlier (687.5 ns: CCLK↓ ≤ 50 ns after the oscillator edge, tCC ≤ 150 ns, ROM tACC ≤ 450 ns, '198 data setup 20 ns: 670 ns), so the dots leave one character after the code (the 8275 pins on the boards, video path). The '198 requires S0 / S1 changes "only while the clock input is high"; S1 changes ripple-late after QA↓ (IE4-2): a board timing property, not modelled | [ИР13] pp. 1-2; [74198] `sn74198.md` (function table, "mode controls should be changed only while the clock input is high", tsu 20 / 30 ns); IE4-1, IE4-4; [R86] p. 34 text ("the output signal of D4.2 switches the register from shift to load") |
| VID-3 | VSP blanking | VSP (8275 pin 35) → font ROM select: [R86] D12 CS (20, active low; PGM 18 to ground), [K14] U11 ~CE (20). VSP high → the ROM outputs float → pull-ups ([R86] R6-R11 10 kΩ, [K14] RN1) → all six data bits 1 = dark in the board's polarity (VID-5). 2708 tCO ≤ 120 ns, 2716 tCE ≤ 450 ns | [R86] crop `..._c35_63_60_95.png`; [K14] netlist; [C78] 2708 4-40 (PDF 232), 2716 4-46 (PDF 238); [R87-5] p. 27 text (VSP disables the ROM, "the register inputs ... high level ... blanking") |
| VID-4 | LTEN through the ТМ2 | [R86] D13.1 К155ТМ2 (second flip-flop: C 11, D 12, R̄ 13, Q̄ 8; S̄ 10 not drawn) / [K14] U17A 7474 (C 3, D 2, R̄ 1, Q̄ 6, S̄ 4 = VCC): D ← LTEN (8275 pin 37); clock ← S1 = QD·QC (rises at the transition 9 → 10); Q̄ → shift register CLR (13, active low, asynchronous, overrides); R̄ ← shift register QH (Q7, pin 20). A latched LTEN = 1 clears the register (all outputs 0 = lit, VID-5); the clear makes QH = 0, which resets the flip-flop and ends the clear (a self-ending pulse, '198 clear→QH ≤ 35 ns, 7474 R̄→Q̄); afterwards ones shift in from SR (pulled up), so QF (the output used) stays 0 for the 6 dots up to the next load: the whole character line lit. In logic without delays S1↑ comes one oscillator period before the load edge; with the data sheet delays (QA↓→QC ≤ 34 ns, 7408, 7474 CLK→Q̄, then the clear pulse) the clear overlaps or follows the load edge (10→11 QA↑ at +62.5 ns + 16 ns), and the text says the flip-flop switches "at the moment the display of the marked character starts": the function is LTEN of the loaded character, latched at the load (the planned model's `lt <= lten` at the load) | [R86] crop `..._c35_63_60_95.png`, p. 34 text (render `..._page-34_p01_c48_0_100_50.png`); [K14] netlist U17A, U13; [ТМ2] `k155tm2.pdf`; [7474] `sn74ls74a.pdf` p. 1 function table; [74198] clear tw ≥ 20 ns, tPHL ≤ 35 ns; IE4-2 delays |
| VID-5 | Shift order, serial input, output | D0-D5 of the register ← ROM D0-D5 ([R86] D12 pins 9, 10, 11, 13, 14, 15 → D15 3, 5, 7, 9, 15, 17; [K14] DQ0-DQ5 → A-F) with pull-ups; D6, D7 (G, H) and the serial inputs SR (2), SL (22) pulled up; ROM D6, D7 not connected. Shift right, output QF (= Q5, pin 16): the dots are ROM bit 5 first, then 4 ... 0; bit 5 shows from the load (10→11) to the next QA↑, each dot 2 oscillator periods. QF → inverter ([R86] D9.4 → R15 1 kΩ, [K14] U19B) → the video transistor ([R86] V2, [K14] Q1 via U16D and R9). A ROM bit 0 is a lit dot (the inverter makes it high at the mixer); the planned model's `pix` = 1 for lit with the font file inverted accordingly: equal at the screen | [R86] crop `..._c35_63_60_95.png`; [K14] netlist U13, U19, U16; [74198] function table |
| VID-6 | RVV ([K14] only) | [K14] U16D 7486: pin 13 ← 8275 RVV (pin 36) directly (net `U16.13 U8.36`, no flip-flop), pin 12 ← U19B (inverted QF) → pin 11 → R9 → Q1: RVV is XORed at the output without re-timing, so it changes at CCLK↓ + tAT while the previous character's dots are still shifting (it leads its own dots by 11 oscillator periods). [R86]: RVV not connected (the 8275 pins on the boards) | [K14] netlist, render `Schematic-1.4_p04_c38_50_98_86.png` |
| VID-7 | HRTC, VRTC | To the sync mixer only (named, not traced): [R86] D5.2 (XOR, pins 4, 5) → D9.3 → R16 680 Ω → V2; [K14] U16B → U19D → R5 → Q1. Not re-timed (the 8275 pins on the boards) | [R86] crop `..._c35_63_60_95.png`; [K14] netlist |
| VID-8 | Other video outputs | LA0, LA1, HGLT not connected on both boards; GPA0 → font A10, GPA1 → JP2 on [K14] only; IRQ, LPEN, LC3 not connected (the 8275 pins on the boards). No other digital video signal on either board | the 8275 pins on the boards; [K14] netlist |

### Assumptions checked (VID)

Model assumptions (VID):

- `LOAD_STATE = 10` (the ИР13 loads at the QA↑ just before CCLK↓): confirmed (VID-2; both boards).
- Font address `{CC6..CC0, LC2..LC0}`: confirmed (VID-1; [K14] adds GPA0 as A10, 0 for the RK86 font).
- VSP blanking through the ROM select: confirmed (VID-3).
- LTEN re-timed by the ТМ2 at the load: confirmed as a function (VID-4), with a timing note: the ТМ2
  clock edge is S1↑ (transition 9 → 10), nominally one oscillator period before the load edge; the
  clear acts on the loaded character only through the gate and flip-flop delays ([R86] p. 34 text
  confirms the intent). The ТМ2 R̄ input is fed back from QH (a self-ending clear pulse); the model's
  latch-until-next-load is equal at the dots.
- RVV not re-timed on [K14]: confirmed (VID-6).

### SILENT (VID)

- VID-1: the К573РФ1 data sheet is not in the collection; its access time is taken from the Intel
  2708 ([C78] 4-40: tACC ≤ 450 ns, tCO ≤ 120 ns). Searched: skiselev/radio-86rk `Documentation/` (no
  К573РФ1 sheet), the maintainer's source collection.
- VID-4: the minimum delays of the 7492, 7408 / К155ЛИ1 and 7474 (only typical / maximum are given),
  so the overlap of the clear with the load edge is shown for typical / maximum values only.

## GLUE: the board glue

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| GLUE-1 | Address decoder [R86] | D11 К555ИД7 (74LS138): A (1) ← A13, B (2) ← A14, C (3) ← A15; G1 (6) ← the start-up flip-flop Q (D13.2 pin 5); G2A, G2B (4, 5) grounded. Eight 8 KB blocks: Y0, Y1 (0000-3FFF) → D5.3 (XOR) → 1 for RAM bank 0; Y2, Y3 (4000-7FFF) → D10.4 (NAND) → 1 for RAM bank 1 (32 KB version); Y4 (8000-9FFF) → D20 CS (keyboard / tape PPI); Y5 (A000-BFFF) → D14 CS (interface PPI); Y6 (C000-DFFF) → D8 CS (8275); Y7 (E000-FFFF) → D2 CS (8257, written only) and, through D4.3, the monitor ROM CE (read only): "one signal selects both the DMA controller and the ROM, because the ROM is only read and the DMA controller only written". Mirrors: the PPIs (A1, A0) every 4 bytes over 8 KB; the 8275 (A0) every 2 bytes; the 8257 (A3-A0) every 16 bytes over E000-FFFF; the 2 KB monitor 4 times (E000, E800, F000, F800) | [R86] p. 32 text (render `..._c0_45_50_100.png`), crop `..._c49_10_69_38.png`; [R86-4] p. 26 Fig. 2 (memory map) |
| GLUE-2 | Address decoder [K14] | U14 74LS138: A0-A2 ← A12-A14, E3 ← A15, E1, E2 = GND: 4 KB blocks in 8000-FFFF: O0 8000 PPI1 (keyboard), O1 9000 8253, O2 A000 PPI2, O3 B000 8251, O4 C000 8275, O5 D000 EXT_CS, O6 E000-EFFF 8257 CS; ROM ~CE = (O6 AND O7) AND start-up Q (U18A, U18B): E000-FFFF; RAM ~CE = NAND (Q, NOT A15) (U20B): 0000-7FFF | [K14] netlist (U14, U18, U20) |
| GLUE-3 | ЧТЕНИЕ | [R86] D5.1 (К155ЛП5) = DBIN XOR the 8257 MEMW; R5 10 kΩ pulls the MEMW input high while the 8257 floats it ("Resistor R5 holds logic 1 on pin 2 of D5.1 while MEMW is in the high-impedance state"). ЧТЕНИЕ is active low: DBIN = 1 (CPU read) or MEMW = 0 (DMA) → 0. [K14] U16A: ~RD = DBIN XOR ~MEMW, RN1 pull-up on ~MEMW. ЧТЕНИЕ goes to the memories' read enable, the PPI RD, the 8275 RD ([R86] D17 OE 20, D14 RD 5; [K14] ~RD net) | [R86] p. 32 text (render `..._c0_0_50_55.png`), crop `..._c50_36_70_66.png`; [R86-4] p. 26; [K14] netlist |
| GLUE-4 | 8257 in slave mode | CS ← Y7 / O6; IOW (2) ← CPU WR ("When writing control words into the DMA controller, IOWR gets logic 0 from the WR output of the microprocessor"); A0-A3 ← A0-A3; IOR (1) pulled up ([R86] R4 10 kΩ "performs the same function as R5"; [K14] RN1) and taken only by the 8275 WR gate: the CPU cannot read the 8257; MEMR (3) not connected; TC (36), MARK (5), DACK0, 1, 3 not connected | [R86-4] p. 26; [R86] p. 34 text, crop `..._c35_48_50_64.png`; [K14] netlist |
| GLUE-5 | 8257 requests and control | DRQ2 (17) ← 8275 DRQ (5); DACK2 (14) → 8275 DACK (6); DRQ0, DRQ1, DRQ3 (19, 18, 16) to ground ([R86] DRQ1, DRQ3 drawn to a ground symbol, DRQ0 joined to them; [K14] GND); READY (6) ← 8224 READY; CLK (12) ← Φ2 (TTL); RESET (13) ← 8224 RESET; HRQ / HLDA: GLUE-16 | [R86] crops `..._c34_13_55_50.png`, `..._c35_48_50_64.png`; [K14] netlist |
| GLUE-6 | 8275 WR gate | [R86] D4.1 (К155ЛИ1, AND): inputs ЗАПИСЬ (CPU WR) and the 8257 IOR; output 3 → 8275 WR (10): "A low level appears at its output with the same level on the line ЗАПИСЬ during the initialization of the display controller, or with a low level on the IOR output of the DMA controller while a byte is transferred from the screen area of the RAM". [K14] U18D: ~CRT_WR = ~WR AND ~IOR. Re-check on [R86-6] not needed (the text states it; the scan inputs of D4.1 are not traceable) | [R86] p. 34 text (render `..._page-34_p01_c48_0_100_50.png`); [R86-4] p. 26 ("In DMA mode the IORD output gives the WR signal of the КР580ВГ75, the MEMW output the ЧТЕНИЕ signal of the memories"); [K14] netlist |
| GLUE-7 | 8275 other pins | CS ← Y6 / O4; RD ← ЧТЕНИЕ; A0 ← A0; CCLK ← ИЕ4 QD; DRQ / DACK: GLUE-5; LPEN, IRQ not connected (LPEN floats on both boards) | [R86] crop `..._c35_63_60_95.png`; [K14] netlist |
| GLUE-8 | CPU INT, READY | INT grounded; READY always high: GLUE-14, GLUE-17 | GLUE-14, GLUE-17 |
| GLUE-9 | RESET net | The 8224 RESET → 8080 RESET, 8257 RESET, both PPIs (pin 35), the start-up flip-flop (through an inverter: [R86] D9.2, [K14] U19E pins 11 → 10); [K14] also the 8251. The 8275 has no reset pin. [R86-4] p. 26: the RESET pulse must not exceed 1-1.5 ms, or the DRAM loses its contents (MEM-3) | [R86] crop `..._c36_8_60_19.png`; [K14] RESET net; [R86-4] p. 26 |
| GLUE-10 | Upper address latch | [R86] D7 К589ИР12 (8212): MD (2) and DS̄1 (1) grounded (input mode), DS2 (13) ← 8257 AEN (9): outputs enabled while AEN; STB (11) ← ADSTB (8): "the data latch follows D while the clock is high, latching occurs when the clock returns low"; CLR̄ (14) high; D0-D7 → A8-A15. [K14] U12 74LS373: LE ← ADSTB, OE̅ ← NOT AEN (U19F), D0-D7 → A8-A15 | [R86] p. 34 text (render `..._page-34_p01_c0_50_52_100.png`), crop `..._c35_48_50_64.png`; [C78] 8212 functional description (PDF 526); [K14] netlist |
| GLUE-11 | Start-up mapping [R86] | D13.2 (К155ТМ2 first flip-flop): R̄ (1) ← D9.2 (NOT RESET), S̄ (4) ← D10.1 (NAND, inputs A15 and one signal not traceable at the scan resolution), C (3) and D (2) tied together (level not legible). Text: "after reset the CPU starts at 0000H, the monitor ROM is at F800H: on СБРОС the output of D13.2 becomes 0, which disables the decoder D11 and, through D4.3, goes to the CS input of the ROM D17 and ensures the reading of the first instruction from the ROM, an unconditional jump to the start of the monitor. After it, the address bus carries the address of the next instruction, whose MSB is 1. The high level on A15 returns D13.2 to the initial state". While Q = 0: ROM CE active for every address (A0-A10 → the ROM), D11 disabled, so no RAM CAS, no PPI, 8275 or 8257 select. D4.3 (AND): Q AND Y7 → ROM CE̅ (pin 18) | [R86] p. 32 text (render `..._c0_0_50_55.png`), crops `..._c36_8_60_19.png`, `..._c49_10_69_38.png`, `..._c50_36_70_66.png` |
| GLUE-12 | Start-up mapping [K14] | U17B 7474: R̄ (13) ← NOT RESET (U19), S̄ (10) ← NAND (DBIN, A15) (U20A), C (11) and D (12) grounded, Q (9) → the ROM and RAM selects (GLUE-2). Set (start-up over) asynchronously by the first CPU read with A15 = 1 (DBIN↑ in T2 of that read); while Q = 0 the ROM answers every read, the RAM is off, the U14 devices still decode (not gated) | [K14] netlist (U17B, U19, U20) |
| GLUE-13 | Bus during HOLD | During AEN the address is the 8257's (A0-A7 from the 8257, A8-A15 from the latch); ЧТЕНИЕ = the 8257 MEMW; the decoder decodes the DMA address, so only RAM answers (screen area); the CPU's WR is inactive (the 8080 holds no write across HLDA) | GLUE-1, GLUE-3, GLUE-10; `retroICs/ics/intel/8257/record.md`, "HOLD overhead with an 8080A" |
| GLUE-14 | CPU READY (23) | From the 8224 READY; RDYIN tied high on both boards, so no wait states. WAIT (24) not used ([K14] U1.24 no net). From CPU-1 (the data sheet half stays in retroICs). | [R86], [K14] (CLK-11) |
| GLUE-15 | CPU RESET (12) | From the 8224 RESET. From CPU-2. | [R86], [K14] |
| GLUE-16 | CPU HOLD (13) / HLDA (21) | HOLD ← 8257 HRQ (pin 10), HLDA → 8257 HLDA (pin 7), directly on both boards. From CPU-3 (timing: retroICs ics/intel/8257/record.md, "HOLD overhead with an 8080A"). | [C78] 11-12, 11-15 |
| GLUE-17 | CPU INT (14), INTE (16) | INT tied to ground on both boards ([R86] symbol at pin 14; [K14] U1.14 GND), so interrupts never occur; INTE drives the sound (SND-1). From CPU-4. | [R86] crop `..._c34_13_55_50.png`; [K14] netlist; [C78] 11-12 |
| GLUE-18 | CPU DBIN (17) | → ЧТЕНИЕ XOR (GLUE-3); on [K14] also the start-up NAND (GLUE-12). From CPU-6. | [K14] U16.2, U20.1 |
| GLUE-19 | The monitor's 8255 control words | The monitor writes 8Ah to 8003h (keyboard / tape PPI) at F836 (`3E 8A 32 03 80`) and 90h to A003h (ROM disk PPI) at FA68 (`3E 90 32 03 A0`, followed by `22 01 A0` SHLD A001h, a byte write of port B and port C, and `3A 00 A0` LDA A000h, a read of port A); it also writes a BSR word to 8003h at FE84..FE8B (`3A 06 76 E6 01 F6 06 32 03 80`: 06h or 07h, reset / set PC3). The decoding of 8Ah and 90h: retroICs PPI-10. From PPI-10. | [MON] `BIOS.BIN` offsets 0036, 0268, 0684; [C78] 12-81 |

### The 8257 on the board (GLUE)

The board's use of the 8257, against its data sheet record (`retroICs/ics/intel/8257/record.md`,
"Timing (data sheet)"):

- READY is tied high on both boards (8224 RDYIN pulled up), so SW never occurs (GLUE-5, GLUE-14).
- The RK86 programs a DMA write cycle (count bits 15:14 = 01, [C78] 12-100): the 8257 drives IOR
  (8275 WR) and MEMW (memory read strobe ЧТЕНИЕ); MEMR and IOW stay inactive ([C78] 12-105).
- The memory-mapped wiring of the data sheet (Fig. 7, Fig. 8, [C78] 12-106) is not the RK86's: the
  RK86 takes the 8257 MEMW pin as the memory read strobe (ЧТЕНИЕ = DBIN XOR MEMW, D5.1 [R86] /
  U16A [K14]) and the IOR pin as the 8275 WR (D4.1 [R86] / U18D [K14], an AND with the CPU WR);
  MEMR is not connected; IOW is the programming input from the CPU WR (GLUE-3, GLUE-4, GLUE-6).
- ЧТЕНИЕ: with A4h (extended write, the monitor's mode) the memory read strobe of the board is
  S2-S4, 1125 ns.
- The upper address byte goes out on D0-D7 with ADSTB in every S1 ([C78] 12-100), latched by D7
  К589ИР12 [R86] / U12 74LS373 [K14] (GLUE-10).
- TC: 0923h gives TC on transfer 2340. TC and MARK are not connected on either board (GLUE-4).
- The DMA cadence. The RK86 case: the 8275 drops DRQ at each DMA WR↓ (tRQ ≤ 200 ns [D79], 250 ns
  [D84]) and raises it again tWQ ≤ 250 / 275 ns after WR↑ while the burst lasts ([D79] Fig. 30
  p. 1-184, table p. 1-182). Its WR is the 8257 IOR, low from θ↑(S2) to θ↓ of the next state. So
  DRQ is low when the 8257 samples it at θ↓(S4) of every transfer: HRQ falls after every character
  and the 8257 returns to SI. The DRQ comes back ≤ 450 / 475 ns after that SI starts and is
  normally taken at the next θ↓ (562.5 ns later; it misses only with both TDCT and tWQ near their
  maxima). Within an 8275 burst each character is then its own HOLD period: SI, SI, S0, S0, S1-S4
  = 8 Φ per character when the 8080's resumed machine cycle is read-type (HOLD is sampled at its
  T2), 9 Φ when it is write-type, 11-14 Φ when the DRQ misses the SI sample (one more machine
  cycle). The 8080 runs one machine cycle between two characters. The first character of a burst
  follows the latency row of the 8257 record's table "HOLD overhead with an 8080A".

### Assumptions checked (GLUE)

Model assumptions (GLUE):

- The decoder ranges of the planned model (8000-9FFF keyboard PPI, A000-BFFF window, C000-DFFF
  CRT, E000-FFFF DMA write / monitor read): confirmed for [R86] (GLUE-1; [R86-4] Fig. 2). [K14]
  decodes 4 KB blocks with extra devices (GLUE-2); the RK86 machine follows [R86].
- ЧТЕНИЕ = DBIN XOR MEMW: confirmed (GLUE-3).
- The 8275 WR = CPU WR AND the 8257 IOR: confirmed (GLUE-6, [R86] text and [K14] net).
- LPEN, INT, DRQ0, DRQ1, DRQ3 tied inactive: INT and DRQ0/1/3 confirmed (grounded); LPEN: silent on
  the level (not connected, floating, on both boards); a constant level gives no rising edge, as the
  planned model assumes.
- The 8257 slave IOR inactive: confirmed (pull-up; GLUE-4).
- The start-up mapping: confirmed with a detail: [K14] ends it at the first *read* with A15 = 1
  (DBIN AND A15); [R86] text: "the high level on A15", the second NAND input not traceable. For the
  monitor (JMP at 0000) both give the same moment. While it lasts [R86] disables every other device
  and the RAM; the monitor answers every address (not only 0000-7FFF).
- Board use, input pins (keyboard / tape PPI 8Ah, ROM disk PPI 90h): an input-mode pin is high
  impedance with ±10 µA input load current; no internal pull-up is specified; what a read of an
  undriven input returns (the ROM disk port A with no pull-ups) is silent ([C78] 12-79, 12-92;
  [D8255] pp. 5, 19).

### SILENT (GLUE)

- GLUE-11: the second input of [R86] D10.1 and the level on D13.2 C / D (scan resolution; the PCB
  insert [R86-6] was not traced track by track).
- GLUE-7: the LPEN level (floating input).

## MEM: RAM and ROM

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| MEM-1 | RAM type | [R86]: D22-D29 К565РУ3, dynamic 16K × 1 (16 KB at 0000-3FFF; 16 chips for 32 KB, the second bank at 4000-7FFF with its CAS from D10.3). [K14]: U9 AS6C62256, static 32K × 8 at 0000-7FFF (~CE = RAM_CS, ~OE = ~RD, ~WE = ~WR) | [R86] pp. 32, 34 text; [R86-4] p. 25 Fig. 1; [K14] netlist |
| MEM-2 | DRAM control [R86] | D16 К155ИР1 shift register clocked by OSC (C1, C2): with no ЧТЕНИЕ and no ЗАПИСЬ, D4.4 holds V2 high (parallel load); on ЧТЕНИЕ or ЗАПИСЬ, D4.4 goes low and the outputs go low one after another, 62.5 ns apart: Q1 → RAS, Q2 → the multiplexer select V of D18, D19 (К555КП11: A0-A6, then A7-A13), Q3 → CAS through D10.2 (bank 0) / D10.3 (bank 1) only with the RAM select. So every ЧТЕНИЕ / ЗАПИСЬ makes a RAS cycle, whatever the address; R14, R20-R28 damp the address lines | [R86] p. 32 text (render `..._c0_45_50_100.png`), p. 34 text (render `..._page-34_p01_c0_0_52_50.png`) |
| MEM-3 | Refresh | "Since the transfer of the screen area to the display controller is regular and the period of the accesses does not exceed 2 ms, the DMA cycles could be used to refresh the RAM, without a special refresh controller. The RESET pulse must then not exceed 1-1.5 ms, or the RAM contents are lost." No refresh cycle is added: no CPU or DMA time is taken (READY is constant high; GLUE-5). Invisible at the level of the mixer's digital inputs: no model. 2116 (the Intel 16K × 1 equivalent): 128 RAS cycles on A0-A6 every 2 ms | [R86-4] p. 26 (render `..._p01_c48_50_100_100.png`); [R87-5] p. 27 (the 8275's DMA "ensures the regeneration"); [C78] 2116 3-109 (PDF 141) |
| MEM-4 | Monitor ROM | [R86] D17 К573РФ5 (2716, 2K × 8): A0-A10 ← A0-A10, CE̅ (18) ← D4.3 (GLUE-11), OE̅ (20) ← ЧТЕНИЕ, VPP (21) +5 V. [K14] U10 2716 (or 2732 / 2764 by JP1), ~CE = ROM_CS, ~OE = ~RD. 2716: tACC ≤ 450 ns, tCE ≤ 450 ns, tOE ≤ 120 ns, tDF ≤ 100 ns, tOH ≥ 0. Against the 8080 read window (MEM-8: about 800 ns from address to the T3 sample; OE̅ from DBIN↑ in T2 ≥ 300 ns before it): no wait states needed (and READY is tied high) | [2716] p. 5-4 (render `Intel_-_2716_p04.png`); [C78] 4-46 (PDF 238); [R86] crop `..._c50_36_70_66.png` |
| MEM-5 | Font ROM | [R86] D12 К573РФ1 (2708 type, 1K × 8): 2708 tACC ≤ 450 ns, tCO ≤ 120 ns, tDF ≤ 120 ns. [K14] U11 2716 (MEM-4 values). Use: VID-1..VID-3 | [C78] 4-40 (PDF 232) |
| MEM-6 | Memory output after ЧТЕНИЕ ends | The 8275 takes the DMA byte at WR↑, 5 oscillator periods (Tθ, the Φ2 high time) after ЧТЕНИЕ (MEMW) ends (the 8257 record, "Transfer states"). [R86] DRAM: the Intel 2116 data sheet: "Output is three-state ... Data is latched and valid into next cycle" (the output is turned off only by a CAS-only or CAS-before-RAS cycle), so the byte stays on the bus after CAS rises. [K14] SRAM: ~OE follows ~RD, so its output turns off when ~RD rises; the byte at WR↑ is then held only by the bus capacitance (no bus holder). The planned memory model (the memory output follows `bus_a`, not `mem_rd`) matches the working boards | [C78] 2116 3-109; `retroICs/ics/intel/8257/record.md`, "Transfer states" |
| MEM-7 | Address multiplexing | [R86] D18, D19 К555КП11: the 14 address bits as 7 + 7 for RAS / CAS (MEM-2). [K14] none. Invisible at the machine level | [R86] p. 32 text |
| MEM-8 | CPU read window on the board | At 1.778 MHz: about 800 ns from a valid address to the T3 sample, against the ROM's tACC 450 ns (MEM-4): no wait states needed. From CPU-8 (the data sheet timings stay in retroICs). | [C78] 11-14, 11-15 |

### Assumptions checked (MEM)

Model assumptions (MEM):

- RAM refresh that steals no cycle (no model): confirmed (MEM-3).
- The monitor ROM needs no wait states: confirmed (MEM-4).

### SILENT (MEM)

- MEM-6: the К565РУ3 data sheet is not in the collection (the 2116 is used as its equivalent; the
  К565РУ3 is usually given as the 4116 equivalent, whose data-out behaviour after CAS↑ may differ
  from the 2116's latched output); the AS6C62256 data sheet is not in the collection. Searched:
  skiselev/radio-86rk `Documentation/`, the maintainer's source collection, [C78] (2116, 2117 only).

## TAPE, SND: tape and sound

| ID | Function | Data sheet behaviour (pins, edges, values) | Source (document, page / figure) |
|---|---|---|---|
| TAPE-1 | Tape output | [R86] D20 (keyboard PPI, 8000) PC0 (14) → R32 1 kΩ → C7 0.1 µF, R33 1 kΩ, C8 0.1 µF → connector contact 46 (to the recorder; analogue, named only). [K14] U5 PC0 → R7 → C31, C32, R8 → J4 (tape out) | [R86] crop `..._c66_40_90_82.png`; [K14] netlist (TAPE_OUT) |
| TAPE-2 | Tape input | [R86] connector line 26 = contact А8 (Fig. 3 table; line 25 = Б13 is the video output, not tape; corrected 2026-11-11 in a review of the board's block list) → C5 0.22 µF, R29 12 kΩ, R30 2.4 kΩ, C6 2200 pF → D21 К140УД6 (comparator) → R31 330 Ω, clamp V3 КД503А → D20 PC4 (13). [K14] J4 → C39 → R15, R14 → U21 TL071 → R4, clamp D1 → U5 PC4. Only the digital level at PC4 is visible to the machine | [R86] crop `..._c66_40_90_82.png`; [K14] netlist (TAPE_IN) |
| SND-1 | Sound [R86] | CPU INTE (16) → D9.1 (inverter) → C26 10 µF → H1 (capsule) to +5 V: "The INTE output is used as a one-bit output port: with EI and DI and delay routines sound frequencies can be produced; through D9.1 they reach the capsule H1". PC0 does not reach the sound | [R86] p. 34 text (render `..._page-34_p01_c48_50_100_100.png`), crop `..._c49_10_69_38.png` |
| SND-2 | Sound [K14] | SPKR = U16C XOR (NOT INTE (U20C), NAND (PPI1 PC1, 8253 OUT2) (U20D)) → R11 → Q2 → SP1: INTE, optionally XORed with the timer gated by PC1. PC0 does not reach the speaker | [K14] netlist (INTE, SPKR, SPKR_ENA nets) |

### Assumptions checked (TAPE / SND)

Model assumptions (SND):

- A sound output of PC0 XOR INTE: differs: on both boards the sound is INTE only ([K14]: INTE XOR
  the gated 8253); PC0 drives only the tape output (SND-1, SND-2, TAPE-1).

### SILENT (TAPE / SND)

- TAPE-1: [R86] D9.6 (an inverter between a D20 port C pin and connector contact 47) is not traced
  (probably the РУС/ЛАТ indicator, as [K14] PC3 → U19 → LED): named only.

## The monitor's programming of the chips

What the monitor ROM [MON] writes to the board's chips, against their data sheet records in
`retroICs` (`ics/intel/8255a/record.md`, `8257/record.md`, `8275/record.md`). The 8255 control
words: GLUE-19.

The 8257:

- Mode A4h: autoload, TC stop off, extended write, fixed priority, channel 2 only. Mode 80h
  (written first by the monitor) sets autoload with all channels off, so the channel 2 bytes
  written next are copied into channel 3. After the TC cycle the channel 3 values (address, count,
  mode bits) go to channel 2 "at the beginning of the next channel 2 DMA cycle"; TC stop has no
  effect on channel 2 with autoload ([C78] 12-103, 12-104). The CPU cannot read the 8257 on the
  RK86 (its IOR pin is not on the CPU read path), so the status and update flags are invisible.
- The Mode Set register: the RK86 writes 80h first so that channel 2's bytes go into channel 3.
  From DMA-22.
- The count 0923h gives TC on transfer 2340 (the 8257 on the board, above).

The 8275:

- The monitor programs the 8275 with 4Dh (78 characters per row), 1Dh, 99h, 93h and Start Display
  27h ([MON]): HRTC (93h) 8 CCLK, a line 78 + 8 = 86 CCLK; VRTC (1Dh) 1 row = 10 lines; underline
  line 9 (99h), so lines 0 and 9 are blank; line counter mode 1 (93h): line 0 outputs LC = 9;
  bursts of 8 characters with a burst space of 7 CCLK (27h). From the 8275 record's timing table.
- The monitor waits for IR before it programs the 8257 (0x2E0-0x2E6: `MOV A,M; MOV A,M; ANI 20h;
  JZ`) ([MON]). From the 8275 record (IRQ and IR).
- [MON]: F806 (tape byte in) and F80C (tape byte out) write 8257 mode 80h on entry (FB9C, FC4A) and
  channel 2, 27h, E0h, A4h on exit (FC0F-FC27, FC86-FC9E). Every F809 character output returns
  through FD85 (pushed at FCC1), which sends Load Cursor: 80h to C001 (FD8C), then two parameters.
- After Preset Counters (E0h): the counters stop at E0h until the next command (the 8275 record's
  decision). This does not leave the RK86 display stopped: the monitor's next console output sends
  Load Cursor, which restarts the counters. During tape I/O the display stays stopped from the
  first byte until that output ([MON]).

## Missing documents

| Part | Searched | Used instead / effect |
|---|---|---|
| К573РФ1 (font ROM, [R86] D12) | skiselev/radio-86rk `Documentation/`, the maintainer's source collection | the Intel 2708 ([C78] 4-40): access times only (VID-1, MEM-5) |
| К565РУ3 (DRAM, [R86]) | as above; [C78] has only the Intel 2116 / 2117 | the 2116 ([C78] 3-109); the data-out behaviour after CAS↑ is open (MEM-6); the refresh is invisible (MEM-3) |
| AS6C62256 (SRAM, [K14]) | as above | none; its output follows ~OE (MEM-6) |
| К555ИД7 / 74LS138, К155ЛИ1 / 7408, К155ЛП5 / 7486, К155ЛН1 / 7404, К155ЛА3 / 7400 | as above | combinational gates, written as expressions from the schematics; delays only where VID-4 needs them (typical / maximum not available for these: SILENT) |
| К155ИР1 (the DRAM sequencer D16), К555КП11 (the DRAM address multiplexers) | as above | not modelled: the DRAM cycle is invisible at the machine level (MEM-2, MEM-7) |
| К589ИР12 | as above | the Intel 8212 ([C78], PDF 526) (GLUE-10) |

## Hardware checks

None planned.
