# Bill of Materials (BOM)

**ByByte Nano** — main board (`Board1_main`)

Full component list for robot assembly. Tables are grouped by part type.

<!--
Tip: the Image column on the right automatically picks up a file
when its name matches the value in the File column.
-->

---

## PCB, power & protection

| # | Designator | Qty | Description | Value / model | Image | File |
|:--:|------------|:-----:|-------------|---------------|:-----:|------|
| 1 | `BAT1` | 1 | Battery holder | BH9VPC | <img src="hardware/bom/img/01_bat1.jpg" alt="Battery holder" width="80" /> | `01_bat1.jpg` |
| 2 | `Li-ion Battery` | 1 | 9V Li-ion rechargeable battery (PP3 / “Krona” form factor) | BAT-6F22 | <img src="hardware/bom/img/02_li-ion-battery.jpg" alt="9V Li-ion rechargeable battery" width="80" /> | `02_li-ion-battery.jpg` |
| 3 | `C1,C4` | 2 | Electrolytic capacitor, low ESR | 470uF 16v | <img src="hardware/bom/img/03_c1.jpg" alt="Electrolytic capacitor, low ESR" width="80" /> | `03_c1.jpg` |
| 4 | `C3,C5,C17` | 3 | Electrolytic capacitor, low ESR | 470uF 10v | <img src="hardware/bom/img/04_c3.jpg" alt="Electrolytic capacitor, low ESR" width="80" /> | `04_c3.jpg` |
| 5 | `D4` | 1 | Schottky diode | 1N5822 | <img src="hardware/bom/img/05_d4.jpg" alt="Schottky diode" width="80" /> | `05_d4.jpg` |
| 6 | `F1` | 1 | Fuse (optional) | TRF250-1000 (optional) | <img src="hardware/bom/img/06_f1.jpg" alt="Fuse (optional)" width="80" /> | `06_f1.jpg` |
| 7 | `L1,L2` | 2 | Leaded EMI ferrite bead | R6H-3.0T | <img src="hardware/bom/img/07_l1.jpg" alt="Leaded EMI ferrite bead" width="80" /> | `07_l1.jpg` |
| 8 | `U3,U4` | 2 | DC-DC buck module | MH-MINI-361 (or HW-613) | <img src="hardware/bom/img/08_u3.jpg" alt="DC-DC buck module" width="80" /> | `08_u3.jpg` |
| 9 | `pcb` | 1 | Main ByByte nano board | PCB | <img src="hardware/bom/img/pcb.png" alt="Main ByByte nano board" width="80" /> | `pcb.png` |

## Passive components

| # | Designator | Qty | Description | Value / model | Image | File |
|:--:|------------|:-----:|-------------|---------------|:-----:|------|
| 10 | `C2,C6,C7,C9,C11,C12,C13,C14,C18` | 9 | Ceramic capacitor | 1uF 50v | <img src="hardware/bom/img/09_c2.png" alt="Ceramic capacitor" width="80" /> | `09_c2.png` |
| 11 | `C8,C10,C19` | 3 | Ceramic capacitor | 0.1uF 50v | <img src="hardware/bom/img/10_c8.png" alt="Ceramic capacitor (100 nF)" width="80" /> | `10_c8.png` |
| 12 | `C15,C16` | 2 | Ceramic capacitor | 10nF 50v | <img src="hardware/bom/img/11_c15.jpg" alt="Ceramic capacitor" width="80" /> | `11_c15.jpg` |
| 13 | `R1,R2` | 2 | 1/8 W resistor | 1kΩ | <img src="hardware/bom/img/12_r1.jpg" alt="1/8 W resistor" width="80" /> | `12_r1.jpg` |
| 14 | `R3,R6,R9,R10,R14` | 5 | 1/8 W resistor | 10kΩ | <img src="hardware/bom/img/13_r3.jpg" alt="1/8 W resistor" width="80" /> | `13_r3.jpg` |
| 15 | `R4,R5` | 2 | 1/2 W resistor | 39Ω | <img src="hardware/bom/img/14_r4.jpg" alt="1/2 W resistor" width="80" /> | `14_r4.jpg` |
| 16 | `R7,R8` | 2 | 1/8 W resistor | 1.8kΩ | <img src="hardware/bom/img/15_r7.png" alt="1/8 W resistor" width="80" /> | `15_r7.png` |
| 17 | `R11,R12` | 2 | 1/8 W resistor | 100kΩ | <img src="hardware/bom/img/16_r11.jpg" alt="1/8 W resistor" width="80" /> | `16_r11.jpg` |
| 18 | `R13` | 1 | 1/8 W resistor | 330Ω | <img src="hardware/bom/img/17_r13.png" alt="1/8 W resistor" width="80" /> | `17_r13.png` |
| 19 | `R15` | 1 | 1/8 W resistor | 100Ω | <img src="hardware/bom/img/18_r15.jpg" alt="1/8 W resistor" width="80" /> | `18_r15.jpg` |

## Semiconductors & diodes

| # | Designator | Qty | Description | Value / model | Image | File |
|:--:|------------|:-----:|-------------|---------------|:-----:|------|
| 20 | `D1,D2` | 2 | IR LED | SFH4545 | <img src="hardware/bom/img/19_d1.png" alt="IR LED" width="80" /> | `19_d1.png` |
| 21 | `D3` | 1 | Diode | 1N4149 | <img src="hardware/bom/img/20_d3.png" alt="Diode" width="80" /> | `20_d3.png` |
| 22 | `LED1` | 1 | Green LED 3 mm | FYL-3004GD | <img src="hardware/bom/img/21_led1.jpg" alt="Green LED 3 mm" width="80" /> | `21_led1.jpg` |
| 23 | `LED2,LED3` | 2 | 5 mm addressable RGB LED (WS2812) | WS2812B-TH | <img src="hardware/bom/img/22_led2.jpg" alt="5 mm addressable RGB LED (WS2812)" width="80" /> | `22_led2.jpg` |
| 24 | `Q1` | 1 | NPN transistor | 9014-C | <img src="hardware/bom/img/23_q1.jpg" alt="NPN transistor" width="80" /> | `23_q1.jpg` |
| 25 | `Q2,Q3` | 2 | IR phototransistor | TEFT4300 | <img src="hardware/bom/img/24_q2.jpg" alt="IR phototransistor" width="80" /> | `24_q2.jpg` |
| 26 | `Q4` | 1 | HEXFET / MOSFET transistor | BS170 | <img src="hardware/bom/img/25_q4.png" alt="HEXFET / MOSFET transistor" width="80" /> | `25_q4.png` |
| 27 | `U9` | 1 | Operational amplifier | LM358AP | <img src="hardware/bom/img/26_u9.jpg" alt="Operational amplifier" width="80" /> | `26_u9.jpg` |
| 28 | `U9` | 1 | DIP-8 IC socket | GOLD-8P | <img src="hardware/bom/img/27_u9.jpg" alt="DIP-8 IC socket" width="80" /> | `27_u9.jpg` |

## Modules & controllers

| # | Designator | Qty | Description | Value / model | Image | File |
|:--:|------------|:-----:|-------------|---------------|:-----:|------|
| 29 | `BLUETOOTH1` | 1 | Bluetooth module (HC-02 / HC-05 / HC-06) | HC-06 | <img src="hardware/bom/img/28_bluetooth1.jpg" alt="Bluetooth module" width="80" /> | `28_bluetooth1.jpg` |
| 30 | `BUZZER1` | 1 | Passive buzzer 5V | buzzer-12X9 | <img src="hardware/bom/img/29_buzzer1.jpg" alt="Passive buzzer 5V" width="80" /> | `29_buzzer1.jpg` |
| 31 | `LDR1` | 1 | Photo-resistor (LDR) | 10k | <img src="hardware/bom/img/30_ldr1.jpg" alt="Photo-resistor (LDR)" width="80" /> | `30_ldr1.jpg` |
| 32 | `U1` | 1 | Arduino Nano (ATmega328) | Arduino nano v3 (old) | <img src="hardware/bom/img/31_u1.png" alt="Arduino Nano (ATmega328)" width="80" /> | `31_u1.png` |
| 33 | `U2` | 1 | Motor driver module | DRV8834 | <img src="hardware/bom/img/32_u2.jpg" alt="Motor driver module" width="80" /> | `32_u2.jpg` |
| 34 | `U5` | 1 | Ultrasonic distance sensor | HC-SR05 | <img src="hardware/bom/img/33_u5.png" alt="Ultrasonic distance sensor" width="80" /> | `33_u5.png` |
| 35 | `U6` | 1 | Line tracker module (5 channels) | TRCT5000 5way module | <img src="hardware/bom/img/34_u6.jpg" alt="Line tracker module (5 channels)" width="80" /> | `34_u6.jpg` |
| 36 | `U7` | 1 | IR receiver IC | VS1838B | <img src="hardware/bom/img/35_u7.jpg" alt="IR receiver IC" width="80" /> | `35_u7.jpg` |
| 37 | `U8` | 1 | ESP32-CAM module with 120° camera | ESP32-CAM | <img src="hardware/bom/img/36_u8.png" alt="ESP32-CAM module with 120° camera" width="80" /> | `36_u8.png` |

## Connectors, switches & buttons

| # | Designator | Qty | Description | Value / model | Image | File |
|:--:|------------|:-----:|-------------|---------------|:-----:|------|
| 38 | `H1,H2, H5,H6,J1,J2,J3` | 1 | 1×40 pin header, 2.54 mm pitch | ZL201-40G | <img src="hardware/bom/img/37_h1.jpg" alt="1×40 pin header, 2.54 mm pitch" width="80" /> | `37_h1.jpg` |
| 39 | `H3,H4` | 2 | 2×1 female header, 2.54 mm, 90° | ZL263-2SG | <img src="hardware/bom/img/38_h3.jpg" alt="2×1 female header, 2.54 mm, 90°" width="80" /> | `38_h3.jpg` |
| 40 | `XP3,XP4` | 1 | 1×40 pin header, 2.54 mm pitch, 90° | ZL211-40KG-S | <img src="hardware/bom/img/39_xp3.jpg" alt="1×40 pin header, 2.54 mm pitch, 90°" width="80" /> | `39_xp3.jpg` |
| 41 | `KEY1,KEY2` | 2 | 6 mm tactile button, 4 pins | 1301.9301 | <img src="hardware/bom/img/40_key1.jpg" alt="6 mm tactile button, 4 pins" width="80" /> | `40_key1.jpg` |
| 42 | `SW1` | 1 | Slider switch, 90° | SS-12D | <img src="hardware/bom/img/41_sw1.jpg" alt="Slider switch, 90°" width="80" /> | `41_sw1.jpg` |
| 43 | `U1 holder` | 1 | 1×40 female header, 2.54 mm (for Nano) | ZL262-40SG | <img src="hardware/bom/img/42_u1-holder.png" alt="1×40 female header, 2.54 mm (for Nano)" width="80" /> | `42_u1-holder.png` |
| 44 | `U8 holder` | 2 | 1×8 female header, 2.54 mm (for ESP32-CAM) | ZL262-8SG | <img src="hardware/bom/img/43_u8-holder.jpg" alt="1×8 female header, 2.54 mm (for ESP32-CAM)" width="80" /> | `43_u8-holder.jpg` |
| 45 | `U6 holder` | 1 | 1×8 female header, 2.54 mm |  | <img src="hardware/bom/img/u6-holder.png" alt="1×8 female header, 2.54 mm" width="80" /> | `u6-holder.png` |

## Mechanics & drive

| # | Designator | Qty | Description | Value / model | Image | File |
|:--:|------------|:-----:|-------------|---------------|:-----:|------|
| 46 | `M1,M2` | 2 | DC geared motor N20, 6V | N20 motor 600-1000 rpm | <img src="hardware/bom/img/44_m1.jpg" alt="DC geared motor N20, 6V" width="80" /> | `44_m1.jpg` |
| 47 | `Mount,Mount1` | 2 | N20 ABS motor mount with screw | N20 mount | <img src="hardware/bom/img/45_mount.jpg" alt="N20 ABS motor mount with screw" width="80" /> | `45_mount.jpg` |
| 48 | `Ball wheel` | 2 | N20 mini caster / ball wheel | Ball wheel mini | <img src="hardware/bom/img/46_ball-wheel.jpg" alt="N20 mini caster / ball wheel" width="80" /> | `46_ball-wheel.jpg` |
| 49 | `Wheel` | 2 | N20 wheel, 44 mm, 3 mm shaft | N20 44mm | <img src="hardware/bom/img/47_wheel.jpg" alt="N20 wheel, 44 mm, 3 mm shaft" width="80" /> | `47_wheel.jpg` |

---

## Summary

| Parameter | Value |
|-----------|-------|
| Unique line items | 49 |
| Optional parts | F1 (fuse) |
| Bluetooth | HC-02 / HC-05 / HC-06 |
| DC-DC modules | MH-MINI-361 or HW-613 (recommended) |
| Controller | Arduino Nano v3 (ATmega328) |
