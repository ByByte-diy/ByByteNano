# Bill of Materials (BOM)

**ByByte Nano** — main board (`Board1_main`)

Full component list for robot assembly. Tables are grouped by part type.

---

## PCB, power & protection

| # | Designator | Qty | Description | Value / model | Image |
|:--:|------------|:-----:|-------------|---------------|:-----:|
| 1 | `BAT1` | 1 | Battery holder | BH9VPC | <img src="hardware/bom/img/01_bat1.png" alt="Battery holder" width="80" /> |
| 2 | `Li-ion Battery` | 1 | 9V Li-ion rechargeable battery (PP3 / “Krona” form factor) | BAT-6F22 | <img src="hardware/bom/img/02_li-ion-battery.png" alt="9V Li-ion rechargeable battery" width="80" /> |
| 3 | `C1,C4,C17` | 2 | Electrolytic capacitor, low ESR | 470uF 16v | <img src="hardware/bom/img/03_c1.png" alt="Electrolytic capacitor, low ESR" width="80" /> |
| 4 | `C3,C5` | 3 | Electrolytic capacitor, low ESR | 470uF 6.3v | <img src="hardware/bom/img/04_c3.png" alt="Electrolytic capacitor, low ESR" width="80" /> |
| 5 | `D4` | 1 | Schottky diode | 1N5822 | <img src="hardware/bom/img/05_d4.png" alt="Schottky diode" width="80" /> |
| 6 | `D5` | 1 | Schottky diode | 1N5817 | <img src="hardware/bom/img/d5-1n5817.png" alt="Schottky diode" width="80" /> |
| 7 | `F1` | 1 | Fuse (optional) | TRF250-1000 (optional) | <img src="hardware/bom/img/06_f1.png" alt="Fuse (optional)" width="80" /> |
| 8 | `L1,L2` | 2 | Leaded EMI ferrite bead | R6H-3.0T | <img src="hardware/bom/img/07_l1.png" alt="Leaded EMI ferrite bead" width="80" /> |
| 9 | `U3,U4` | 2 | DC-DC buck module | MH-MINI-361 (or HW-613) | <img src="hardware/bom/img/08_u3.png" alt="DC-DC buck module" width="80" /> |
| 10 | `pcb` | 1 | Main ByByte nano board | PCB | <img src="hardware/bom/img/pcb.png" alt="Main ByByte nano board" width="80" /> |

## Passive components

| # | Designator | Qty | Description | Value / model | Image |
|:--:|------------|:-----:|-------------|---------------|:-----:|
| 11 | `C2,C6,C7,C9,C11,C12,C13,C14,C18` | 9 | Ceramic capacitor | 1uF 50v | <img src="hardware/bom/img/09_c2.png" alt="Ceramic capacitor" width="80" /> |
| 12 | `C8,C10,C19` | 3 | Ceramic capacitor | 0.1uF 50v | <img src="hardware/bom/img/10_c8.png" alt="Ceramic capacitor (100 nF)" width="80" /> |
| 13 | `C15,C16` | 2 | Ceramic capacitor | 10nF 50v | <img src="hardware/bom/img/11_c15.png" alt="Ceramic capacitor" width="80" /> |
| 14 | `R1,R2` | 2 | 1/8 W resistor | 1kΩ | <img src="hardware/bom/img/12_r1.png" alt="1/8 W resistor" width="80" /> |
| 15 | `R3,R6,R9,R10,R14` | 5 | 1/8 W resistor | 10kΩ | <img src="hardware/bom/img/13_r3.png" alt="1/8 W resistor" width="80" /> |
| 16 | `R4,R5` | 2 | 1/4 W resistor | 39Ω | <img src="hardware/bom/img/14_r4.png" alt="1/2 W resistor" width="80" /> |
| 17 | `R7,R8` | 2 | 1/8 W resistor | 1.8kΩ | <img src="hardware/bom/img/15_r7.png" alt="1/8 W resistor" width="80" /> |
| 18 | `R11,R12` | 2 | 1/8 W resistor | 100kΩ | <img src="hardware/bom/img/16_r11.png" alt="1/8 W resistor" width="80" /> |
| 19 | `R13` | 1 | 1/8 W resistor | 330Ω | <img src="hardware/bom/img/17_r13.png" alt="1/8 W resistor" width="80" /> |
| 20 | `R15` | 1 | 1/8 W resistor | 100Ω | <img src="hardware/bom/img/18_r15.png" alt="1/8 W resistor" width="80" /> |

## Semiconductors & diodes

| # | Designator | Qty | Description | Value / model | Image |
|:--:|------------|:-----:|-------------|---------------|:-----:|
| 21 | `D1,D2` | 2 | IR LED | SFH4545 | <img src="hardware/bom/img/19_d1.png" alt="IR LED" width="80" /> |
| 22 | `D3` | 1 | Diode | 1N4148 | <img src="hardware/bom/img/20_d3.png" alt="Diode" width="80" /> |
| 23 | `LED1` | 1 | Green LED 3 mm | FYL-3004GD | <img src="hardware/bom/img/21_led1.png" alt="Green LED 3 mm" width="80" /> |
| 24 | `LED2,LED3` | 2 | 5 mm addressable RGB LED (WS2812) | WS2812B-TH | <img src="hardware/bom/img/22_led2.png" alt="5 mm addressable RGB LED (WS2812)" width="80" /> |
| 25 | `Q1` | 1 | NPN transistor | 9014-C | <img src="hardware/bom/img/23_q1.png" alt="NPN transistor" width="80" /> |
| 26 | `Q2,Q3` | 2 | IR phototransistor | TEFT4300 | <img src="hardware/bom/img/24_q2.png" alt="IR phototransistor" width="80" /> |
| 27 | `Q4` | 1 | HEXFET / MOSFET transistor | BS170 | <img src="hardware/bom/img/25_q4.png" alt="HEXFET / MOSFET transistor" width="80" /> |
| 28 | `U9` | 1 | Operational amplifier | LM358AP | <img src="hardware/bom/img/26_u9.png" alt="Operational amplifier" width="80" /> |
| 29 | `U9` | 1 | DIP-8 IC socket | GOLD-8P | <img src="hardware/bom/img/27_u9.png" alt="DIP-8 IC socket" width="80" /> |

## Modules & controllers

| # | Designator | Qty | Description | Value / model | Image |
|:--:|------------|:-----:|-------------|---------------|:-----:|
| 30 | `BLUETOOTH1` | 1 | Bluetooth module (HC-02 / HC-05 / HC-06) | HC-06 | <img src="hardware/bom/img/28_bluetooth1.png" alt="Bluetooth module" width="80" /> |
| 31 | `BUZZER1` | 1 | Passive buzzer 5V | buzzer-12X9 | <img src="hardware/bom/img/29_buzzer1.png" alt="Passive buzzer 5V" width="80" /> |
| 32 | `LDR1` | 1 | Photo-resistor (LDR) | 10k | <img src="hardware/bom/img/30_ldr1.png" alt="Photo-resistor (LDR)" width="80" /> |
| 33 | `U1` | 1 | Arduino Nano (ATmega328) | Arduino nano v3 (old) | <img src="hardware/bom/img/31_u1.png" alt="Arduino Nano (ATmega328)" width="80" /> |
| 34 | `U2` | 1 | Motor driver module | DRV8833 | <img src="hardware/bom/img/32_u2.png" alt="Motor driver module" width="80" /> |
| 35 | `U5` | 1 | Ultrasonic distance sensor | HC-SR04 | <img src="hardware/bom/img/33_u5.png" alt="Ultrasonic distance sensor" width="80" /> |
| 36 | `U6` | 1 | Line tracker module (5 channels) | TRCT5000 5way module | <img src="hardware/bom/img/34_u6.png" alt="Line tracker module (5 channels)" width="80" /> |
| 37 | `U7` | 1 | IR receiver IC | VS1838B | <img src="hardware/bom/img/35_u7.png" alt="IR receiver IC" width="80" /> |
| 38 | `U8` | 1 | ESP32-CAM module with 120° camera | ESP32-CAM | <img src="hardware/bom/img/36_u8.png" alt="ESP32-CAM module with 120° camera" width="80" /> |

## Connectors, switches & buttons

| # | Designator | Qty | Description | Value / model | Image |
|:--:|------------|:-----:|-------------|---------------|:-----:|
| 39 | `H1,H2,H5,H6,J1,J2,J3` | 1 | 1×40 pin header, 2.54 mm pitch | ZL201-40G | <img src="hardware/bom/img/37_h1.jpg" alt="1×40 pin header, 2.54 mm pitch" width="80" /> |
| 40 | `H3,H4` | 2 | 2×1 female header, 2.54 mm, 90° | ZL263-2SG | <img src="hardware/bom/img/38_h3.png" alt="2×1 female header, 2.54 mm, 90°" width="80" /> |
| 41 | `XP3,XP4` | 1 | 1×40 pin header, 2.54 mm pitch, 90° | ZL211-40KG-S | <img src="hardware/bom/img/39_xp3.jpg" alt="1×40 pin header, 2.54 mm pitch, 90°" width="80" /> |
| 42 | `KEY1,KEY2` | 2 | 6 mm tactile button, 4 pins | 1301.9301 | <img src="hardware/bom/img/40_key1.png" alt="6 mm tactile button, 4 pins" width="80" /> |
| 43 | `SW1` | 1 | Slider switch, 90° | SS-12D | <img src="hardware/bom/img/41_sw1.png" alt="Slider switch, 90°" width="80" /> |
| 44 | `U1 holder` | 2 | 1×15 female header, 2.54 mm (for Nano) | PBS-15 | <img src="hardware/bom/img/42_u1-holder.png" alt="1×15 female header" width="80" /> |
| 45 | `U8 holder` | 2 | 1×8 female header, 2.54 mm (for ESP32-CAM) | ZL262-8SG | <img src="hardware/bom/img/43_u8-holder.png" alt="1×8 female header, 2.54 mm (for ESP32-CAM)" width="80" /> |
| 46 | `U6 holder` | 1 | 1×7 female header, 2.54 mm (for line trackers) | PBS-07R | <img src="hardware/bom/img/u6-holder.png" alt="1×7 female header, 2.54 mm" width="80" /> |
| 47 | `U2 holder` | 2 | 1×6 female header, 2.54 mm | PBS-06 | <img src="hardware/bom/img/pbs-06-zl262-6sg.png" alt="1×6 female header, 2.54 mm" width="80" /> |

## Mechanics & drive

| # | Designator | Qty | Description | Value / model | Image |
|:--:|------------|:-----:|-------------|---------------|:-----:|
| 48 | `M1,M2` | 2 | DC geared motor N20, 6V | N20 motor 500-1000 rpm | <img src="hardware/bom/img/44_m1.png" alt="DC geared motor N20, 6V" width="80" /> |
| 49 | `Mount,Mount1` | 2 | N20 ABS motor mount with screw | N20 mount | <img src="hardware/bom/img/45_mount.png" alt="N20 ABS motor mount with screw" width="80" /> |
| 50 | `Ball wheel` | 2 | N20 mini caster / ball wheel | Ball wheel mini | <img src="hardware/bom/img/46_ball-wheel.png" alt="N20 mini caster / ball wheel" width="80" /> |
| 51 | `Wheel` | 2 | N20 wheel, 44 mm, 3 mm shaft | N20 44mm | <img src="hardware/bom/img/47_wheel.png" alt="N20 wheel, 44 mm, 3 mm shaft" width="80" /> |
| 52 | `M2 x 8mm screw` | 3 | M2 screw 8mm length | M2x8mm | <img src="hardware/bom/img/m2x6-screw.png" alt="M2 screw 8mm length" width="80" /> |
| 53 | `M3 x 12mm screw` | 4 | M3 screw 12mm length | M3x12mm | <img src="hardware/bom/img/m3x12-screw.jpg" alt="M3 screw 12mm length" width="80" /> |
| 54 | `HTP-320` | 2 | Plastic standoff 20mm M3 double-sided | HTP-320 | <img src="hardware/bom/img/standoff-m3x20.png" alt="Plastic standoff 20mm M3 double-sided" width="80" /> |
| 55 | `HTP-305` | 2 | Plastic standoff 5mm M3 double-sided | HTP-305 | <img src="hardware/bom/img/standoff-m3x5.jpg" alt="Plastic standoff 5mm M3 double-sided" width="80" /> |
| 56 | `M3 DIN 985` | 2 | M3 self-locking nut | M3 DIN985 | <img src="hardware/bom/img/m3-din985.png" alt="M3 self-locking nut" width="80" /> |
| 57 | `M2 DIN 985` | 3 | M2 self-locking nut | M2 DIN985 | <img src="hardware/bom/img/m2-din985.png" alt="M2 self-locking nut" width="80" /> |


## Consumables

Materials used during assembly; not included in the robot BOM line count above.

| # | Qty | Description | Notes | Image |
|:--:|:-----:|-------------|-------|-------|
| 1 | 1 | Solder wire, 0.8–1.0 mm | Sn60/Pb40 (Cynel recommended); for through-hole components and headers | <img src="hardware/bom/img/solder-cynel.png" alt="Solder wire" width="80" /> |
| 2 | 1 | Flux paste or rosin flux | (Optional) makes soldering easier on pads and pin headers | <img src="hardware/bom/img/flux-amtech.png" alt="Flux paste or rosin flux" width="80" /> |
| 3 | 1 | Isopropyl alcohol (IPA), 99% | (Optional) flux residue cleaning after soldering | <img src="hardware/bom/img/ipa-99.png" alt="Isopropyl alcohol (IPA), 99%" width="80" /> |
| 4 | 1 | Heat shrink tubing 8mm diameter **BLACK!** | for isolating IR LEDs | <img src="hardware/bom/img/hs-8mm.png" alt="Heat shrink tubing" width="80" /> |

## Required tools

| # | Tool | Purpose | Image |
|:--:|------|---------|-------|
| 1 | Soldering iron (25–60 W, temperature-controlled) | Soldering passives, semiconductors, connectors, and modules | <img src="hardware/bom/img/iron-25w.png" alt="Soldering iron" width="80" /> |
| 2 | Side / flush cutters | Trimming component leads; cutting pin headers to length | <img src="hardware/bom/img/cutters.png" alt="Side / flush cutters" width="80" /> |
| 3 | Multimeter | Setting DC-DC outputs to 5 V and 3.3 V; polarity and rail checks before first power-up | <img src="hardware/bom/img/multimeter.png" alt="Multimeter" width="80" /> |
| 4 | Small Phillips screwdriver | M2/M3 assembly; adjusting DC-DC module trim pots | <img src="hardware/bom/img/screwdriver.png" alt="Small Phillips screwdriver" width="80" /> |
| 5 | USB cable (Mini-B or Micro-B or Type-C, per Nano revision) | Uploading firmware to Arduino Nano | <img src="hardware/bom/img/usb-cable.png" alt="USB cable" width="80" /> |
| 6 | PC with Arduino IDE | Programming and testing | <img src="hardware/bom/img/laptop.png" alt="PC with Arduino IDE" width="80" /> |

**Optional:** helping hands / PCB holder, magnifying lamp.

---

## Summary

| Parameter | Value |
|-----------|-------|
| Unique line items | 57 |
| Optional parts | F1 (fuse) |
| Bluetooth | HC-02 / HC-05 / HC-06 |
| DC-DC modules | MH-MINI-361 or HW-613 (recommended) |
| Controller | Arduino Nano v3 (ATmega328) |
