# AI_CONTEXT.md — ByByte Nano (LLM / RAG Context)

> **Purpose:** structured technical context for the `ByByte-diy/ByByteNano` repository, intended for large language models, RAG pipelines, and coding agents.  
> **Project version:** 1.1.0 · **License:** CERN-OHL-S v2 · **Ecosystem:** ByByte.DIY™  
> **Last context sync:** 2026 (aligned with `README.md`, `BOM.md`, `hardware/`, `source/ByByte_nano.epro`)

---

## 1. Project Summary

**ByByte Nano** (also known as *Babai Nano* / *Бабай Nano* in Ukrainian materials) is a compact **open-hardware educational robotics platform**. It is designed for teaching electronics, sensors, motor control, and embedded programming in classrooms and workshops.

Key properties:
- beginner-friendly assembly (through-hole soldering + off-the-shelf modules);
- main controller: **Arduino Nano (ATmega328)**;
- differential drive (2× N20 geared motors);
- built-in sensor set: line tracking, distance, ambient light, IR remote;
- optional side IR sensors (mainly for maze navigation — may be omitted if not needed);
- optional **ESP32-CAM** (Wi-Fi / video);
- Bluetooth (**HC-02 / HC-05 / HC-06**);
- 2.54 mm expansion headers.

**Related platform:** [ByByte Mega](https://github.com/ByByte-diy/ByByteMega) — a more feature-rich sibling in the same product line.

**What this repository contains today:** hardware documentation, BOM, schematic, Gerber files, CAD images, and an EasyEDA project. **Firmware and example sketches are not included** in the repo (mentioned in README as external / planned).

---

## 2. Repository Map (Key Files)

| Path | Description |
|------|-------------|
| `README.md` / `README.uk.md` | Project overview (English / Ukrainian) |
| `BOM.md` | Full bill of materials (57 line items + consumables + tools) |
| `AI_CONTEXT.md` | This file — AI / RAG context |
| `LICENSE.md` / `LICENSE-CERN.txt` | CERN-OHL-S v2 |
| `hardware/schematics/SCH_ByByte_nano.pdf` | Schematic (PDF) |
| `hardware/pcb/ByByte_nano_pcb.pdf` | PCB layout preview (PDF) |
| `hardware/pcb/Gerber_pcb_ByByte_nano.zip` | Gerber package for PCB fabrication |
| `hardware/bom/BOM_ByByte_Nano.xlsx` | BOM spreadsheet |
| `hardware/bom/img/` | Component photos / renders |
| `cad/img/3D_PCB_main.png` | 3D board render |
| `cad/img/2D_pcb_top.png` | Top view (2D) — note lowercase `pcb` in filename |
| `cad/img/2D_pcb_bottom.png` | Bottom view (2D) |
| `source/ByByte_nano.epro` | EasyEDA project (ZIP archive: schematic + PCB) |

---

## 3. System Architecture (Functional Blocks)

On the main schematic (`main` sheet in EasyEDA), the board is organized into these logical blocks:

| Block (schematic label) | Function | Key components |
|-------------------------|----------|----------------|
| **POWER SUPPLY** | 9V input, regulation | `BAT1`, `D4`, `D5`, `F1`, `U3`, `U4`, `C1–C5`, `L1`, `L2` |
| **CONTROLLER** | Main MCU | `U1` Arduino Nano |
| **MOTOR DRIVER** | N20 motor control | `U2` DRV8833, `M1`, `M2` |
| **ULTRASONIC** | Front ranging | `U5` HC-SR04 |
| **IR LINE TRACKER** | 5-channel line sensing | `U6` TRCT5000 5-way module |
| **SIDES SENSORS** *(optional)* | Side analog IR — maze navigation | `D1`, `D2`, `Q2`, `Q3`, `U9` LM358 |
| **IR SENSOR** | IR remote receiver | `U7` VS1838B |
| **LIGHT SENSOR** | Ambient light | `LDR1` + divider |
| **LEDS** | Status / headlights | `LED1` (green), `LED2`, `LED3` WS2812 |
| **BUZZER** | Audio feedback | `BUZZER1` |
| **BLUETOOTH** | Wireless control | `BLUETOOTH1` |
| **ESP32 Camera module** | Wi-Fi / camera (optional) | `U8` ESP32-CAM |

The EasyEDA project also includes a separate **`LineTracker_SCH`** schematic and **`LIneTracker_PCB`** — a reference line-tracker design. The assembled robot uses the ready-made module `U6` instead.

---

## 4. Power System

| Parameter | Value |
|-----------|-------|
| Source | 9V Li-ion rechargeable battery, PP3 / “Krona” form factor (`BAT1` + BH9VPC holder) |
| Input protection | `F1` fuse (optional), ferrite beads `L1`, `L2` |
| Diodes | `D4` 1N5822, `D5` 1N5817 (Schottky) |
| Regulators | 2× DC-DC buck modules `U3`, `U4`: **MH-MINI-361** or **HW-613** (EasyEDA schematic lists MH-MINI-360) |
| Output rails | **+5 V** and **+3.3 V** (adjusted via trim pots on modules **before soldering!**) |
| Power switch | `SW1` slider switch |
| Indicator | `LED1` green — power (labeled PWR on schematic) |

**Critical assembly step:** before soldering `U3`/`U4`, use a multimeter to set **5.0 V** and **3.3 V**. On first power-up, test without plug-in modules installed; verify polarity and all rails.

---

## 5. Controller and Connectivity

### 5.1 Arduino Nano (`U1`)
- **MCU:** ATmega328, Arduino Nano form factor (v3, “old” footprint per BOM);
- mounted on **2× 1×15 female headers** (`U1 holder`, PBS-15);
- firmware upload via **USB** (Mini-B / Micro-B / Type-C depending on Nano revision);
- toolchain: **Arduino IDE**, standard Arduino libraries.

### 5.2 Bluetooth (`BLUETOOTH1`)
- Supported modules: **HC-02, HC-05, HC-06** (BOM lists HC-06);
- UART interface to Nano;
- control from smartphone or PC.

### 5.3 ESP32-CAM (`U8`, optional)
- Module with 120° camera;
- socket: **2× 1×8 female headers** (`U8 holder`);
- jumpers **J1, J2, J3** (pins from strip `H1,H2,H5,H6,J1,J2,J3`) route ESP programming / UART (see `SCH_ByByte_nano.pdf`);
- UART link to Arduino Nano possible for Wi-Fi-based control.

### 5.4 User inputs
- `KEY1`, `KEY2` — 6 mm tactile buttons;
- `SW1` — power slider switch.

---

## 6. Drive and Mechanics

| Component | Qty | Description |
|-----------|:---:|-------------|
| `M1`, `M2` | 2 | N20 DC geared motor, 6V, 500–1000 rpm |
| `Mount`, `Mount1` | 2 | N20 ABS motor bracket |
| `Wheel` | 2 | N20 wheel, 44 mm, 3 mm shaft |
| `Ball wheel` | 2 | Rear caster / ball support |
| `U2` | 1 | **DRV8833** dual H-bridge motor driver |
| `U2 holder` | 2 | 1×6 female header PBS-06 |

**Fasteners:** M2×8 screws (3), M3×12 screws (4), HTP-320 standoffs 20 mm (2), HTP-305 standoffs 5 mm (2), DIN985 lock nuts M2 (3), M3 (2).

**Kinematics:** differential (tank-style) drive — two drive wheels plus ball casters.

---

## 7. Sensors and Indicators

| Designator | Part | Function |
|------------|------|----------|
| `U6` | TRCT5000 5-way | **5 line sensors** (line following) |
| `U5` | HC-SR04 | **Ultrasonic** front distance |
| `LDR1` | ~10k LDR | **Ambient light** (analog) |
| `D1`, `D2` + `Q2`, `Q3` + `U9` | IR LED + phototransistor + LM358 | **Side optical sensors** *(optional)* — primarily for **maze navigation**; skip if maze mode is not planned |
| `U7` | VS1838B | **IR remote receiver** |
| `LED2`, `LED3` | WS2812B-TH 5 mm | **Addressable RGB headlights** |
| `LED1` | Green 3 mm LED | Power indicator |
| `BUZZER1` | Passive 5V buzzer | Audio feedback |

**Side IR sensors (optional):** The **SIDES SENSORS** block (`D1`, `D2`, `Q2`, `Q3`, `U9` LM358, DIP-8 socket, and related passives) is **not required** for basic operation. It is intended mainly for **maze navigation** (wall detection on left/right). If maze projects are not planned, these parts **may be left unpopulated** — line following, obstacle avoidance with the front ultrasonic sensor, Bluetooth/IR control, and other features still work without them.

**Assembly note (if installing side IR):** `D1`/`D2` IR LEDs should be covered with **black 8 mm heat-shrink tubing** (see Consumables in `BOM.md`).

### Optional hardware summary

| Feature | Parts | When to skip |
|---------|-------|--------------|
| Fuse | `F1` | If extra input protection is not desired |
| Side IR / maze sensors | `D1`, `D2`, `Q2`, `Q3`, `U9`, U9 socket | No maze navigation planned |
| ESP32-CAM | `U8`, `U8 holder` | No Wi-Fi / video needed |
| Bluetooth | `BLUETOOTH1` | Wired/USB control only |

---

## 8. Full BOM (57 Line Items)

> Source of truth: `BOM.md`. Text copy below for RAG indexing (no images).

### 8.1 PCB, power, protection (1–10)
1. `BAT1` — 9V battery holder BH9VPC ×1  
2. Li-ion Battery — 9V PP3 BAT-6F22 ×1  
3. `C1,C4,C17` — 470µF 16V electrolytic ×2  
4. `C3,C5` — 470µF 6.3V electrolytic ×3  
5. `D4` — 1N5822 Schottky ×1  
6. `D5` — 1N5817 Schottky ×1  
7. `F1` — TRF250-1000 fuse (optional) ×1  
8. `L1,L2` — ferrite bead R6H-3.0T ×2  
9. `U3,U4` — DC-DC buck MH-MINI-361 / HW-613 ×2  
10. PCB — ByByte Nano main board ×1  

### 8.2 Passive components (11–20)
11. `C2,C6,C7,C9,C11,C12,C13,C14,C18` — 1µF 50V ceramic ×9  
12. `C8,C10,C19` — 0.1µF 50V ceramic ×3  
13. `C15,C16` — 10nF 50V ceramic ×2  
14. `R1,R2` — 1kΩ 1/8W ×2  
15. `R3,R6,R9,R10,R14` — 10kΩ 1/8W ×5  
16. `R4,R5` — 39Ω 1/4W ×2  
17. `R7,R8` — 1.8kΩ 1/8W ×2  
18. `R11,R12` — 100kΩ 1/8W ×2  
19. `R13` — 330Ω 1/8W ×1  
20. `R15` — 100Ω 1/8W ×1  

### 8.3 Semiconductors (21–29)

> **Optional block — side IR / maze sensors:** items 21, 26, 28, 29 (`D1`, `D2`, `Q2`, `Q3`, `U9`, socket) may be omitted if maze navigation is not needed.

21. `D1,D2` — IR LED SFH4545 ×2 *(optional — side sensors)*  
22. `D3` — 1N4148 ×1  
23. `LED1` — green 3 mm FYL-3004GD ×1  
24. `LED2,LED3` — WS2812B-TH ×2  
25. `Q1` — NPN 9014-C ×1  
26. `Q2,Q3` — IR phototransistor TEFT4300 ×2 *(optional — side sensors)*  
27. `Q4` — MOSFET BS170 ×1  
28. `U9` — op-amp LM358AP ×1 *(optional — side sensors)*  
29. `U9 socket` — DIP-8 GOLD-8P ×1 *(optional — side sensors)*  

### 8.4 Modules and controllers (30–38)
30. `BLUETOOTH1` — HC-06 (HC-02/05/06 compatible) ×1  
31. `BUZZER1` — passive 5V buzzer ×1  
32. `LDR1` — 10k photoresistor ×1  
33. `U1` — Arduino Nano ATmega328 ×1  
34. `U2` — DRV8833 motor driver ×1  
35. `U5` — HC-SR04 ultrasonic sensor ×1  
36. `U6` — TRCT5000 5-channel line tracker ×1  
37. `U7` — VS1838B IR receiver ×1  
38. `U8` — ESP32-CAM 120° ×1  

### 8.5 Connectors and switches (39–47)
39. `H1,H2,H5,H6,J1,J2,J3` — 1×40 pin header ZL201-40G ×1 (cut to length)  
40. `H3,H4` — 2×1 female header 90° ZL263-2SG ×2  
41. `XP3,XP4` — 1×40 pin header 90° ZL211-40KG-S ×1  
42. `KEY1,KEY2` — 6 mm tactile switch ×2  
43. `SW1` — slider switch SS-12D ×1  
44. `U1 holder` — 1×15 female header PBS-15 ×2  
45. `U8 holder` — 1×8 female header ZL262-8SG ×2  
46. `U6 holder` — 1×7 female header PBS-07R ×1  
47. `U2 holder` — 1×6 female header PBS-06 ×2  

### 8.6 Mechanics (48–57)
48. `M1,M2` — N20 motor ×2  
49. `Mount,Mount1` — N20 mount ×2  
50. `Ball wheel` ×2  
51. `Wheel` N20 44 mm ×2  
52. M2×8 screw ×3  
53. M3×12 screw ×4  
54. HTP-320 standoff 20 mm ×2  
55. HTP-305 standoff 5 mm ×2  
56. M3 DIN985 lock nut ×2  
57. M2 DIN985 lock nut ×3  

### 8.7 Consumables (not counted in line items)
- Solder wire 0.8–1.0 mm (Sn60/Pb40)  
- Flux paste (optional)  
- Isopropyl alcohol 99% (optional)  
- Black 8 mm heat-shrink tubing *(only if side IR LEDs `D1`/`D2` are installed)*  

### 8.8 Required tools
- Soldering iron 25–60 W (temperature-controlled)  
- Side / flush cutters  
- Multimeter  
- Small Phillips screwdriver  
- USB cable  
- PC with Arduino IDE  

---

## 9. Connectors and Expansion

- **2.54 mm headers:** horizontal (`H1–H6`, `J1–J3`) and 90° (`XP3`, `XP4`) for modules and prototyping;
- **Socketed modules:** Nano, ESP32-CAM, DRV8833, line tracker — removable;
- **Expansion:** free Arduino pins routed to headers (pinout in `SCH_ByByte_nano.pdf`).

---

## 10. PCB Manufacturing

| Artifact | File |
|----------|------|
| Gerber + drill | `hardware/pcb/Gerber_pcb_ByByte_nano.zip` |
| PDF preview | `hardware/pcb/ByByte_nano_pcb.pdf` |
| Editable source | `source/ByByte_nano.epro` (EasyEDA) |
| PCB names in project | `PCB1` (main), `Board1_main` in BOM |

Under CERN-OHL-S v2, products made from this design should **keep the Source Location visible on PCB silkscreen** where practicable.

---

## 11. Recommended Assembly Order

1. Solder small passives and semiconductors on the main PCB (skip `D1`, `D2`, `Q2`, `Q3`, `U9` and socket if side IR / maze sensors are not needed).  
2. Solder connectors, buttons, and power switch.  
3. **Trim `U3`/`U4` to 5 V and 3.3 V** (modules not yet installed).  
4. Solder DC-DC modules; verify rails.  
5. Install `U9` socket, LM358, and plug-in modules (`U2`, `U5`, `U6`, `BLUETOOTH1`, `BUZZER1`).  
6. Insert Arduino Nano and ESP32-CAM (optional).  
7. Assemble mechanics: motors, wheels, standoffs.  
8. Check battery polarity, power on, test with example sketches.  

---

## 12. Software / Firmware Context

- **Target platform:** Arduino IDE, ATmega328 on Arduino Nano.  
- **Typical libraries:** `Serial` / `SoftwareSerial` for Bluetooth, `NewPing` or custom code for HC-SR04, `Adafruit_NeoPixel` or FastLED for WS2812, `IRremote` for VS1838B.  
- **ESP32-CAM:** flashed separately (Arduino IDE / ESP-IDF); J1–J3 control UART routing.  
- **This repository does not contain** a `firmware/` folder or `.ino` sketch files — hardware only.

---

## 13. Educational Use Cases

- line following (5 IR channels);  
- obstacle avoidance (front ultrasonic);  
- maze navigation (optional side IR sensors + ultrasonic);  
- IR remote or Bluetooth control;  
- visual and audio feedback (WS2812, buzzer);  
- optional video streaming (ESP32-CAM);  
- core concepts: power rails, PWM, ADC, UART, I²C/SPI (depending on wiring).

---

## 14. Troubleshooting Knowledge Base

| Symptom | Likely causes | Actions |
|---------|---------------|---------|
| No power | Polarity, `SW1`, dead battery, `F1` | Measure +9V, 5V, 3.3V with multimeter |
| USB upload fails | Wrong board/port, drivers, J1–J3 routing | Check ESP jumpers, cable, CH340/FTDI driver |
| Motors not spinning | `U2` DRV8833, wiring, PWM pins | Verify driver supply and DIR/PWM signals |
| Sensors unresponsive | Missing 5V, bad socket contact | Check 5V rail, analog/digital pin mapping |
| WS2812 not lighting | Wrong GPIO, 5V level, library config | Verify data pin, library, color order |
| Bluetooth won't connect | RX/TX swapped, baud mismatch | Try 9600/115200; HC-05 AT mode if needed |

---

## 15. Known Documentation Discrepancies (for AI grounding)

| Topic | README | BOM / schematic (preferred) |
|-------|--------|----------------------------|
| Line item count | 55 | **57** (`BOM.md` Summary) |
| Motor driver | DRV8834 | **DRV8833** |
| Ultrasonic sensor | HC-SR05 (legacy) | **HC-SR04** |
| Motor speed | 600–1000 rpm | **500–1000 rpm** |
| DC-DC in epro | MH-MINI-360 | BOM: **MH-MINI-361** / HW-613 |
| 2D PCB image path | `2D_PCB_*.png` (old) | **`2D_pcb_*.png`** (case-sensitive on GitHub) |

**Priority when answering users:** `BOM.md` → `SCH_ByByte_nano.pdf` → `source/ByByte_nano.epro`.

---

## 16. Retrieval Keywords

```
ByByte, ByByte Nano, Babai Nano, Arduino Nano, ATmega328, educational robot,
open hardware, CERN-OHL, EasyEDA, DRV8833, HC-SR04, HC-06, ESP32-CAM,
WS2812, line follower, TRCT5000, N20 motor, 9V battery, PP3, Krona,
ultrasonic sensor, line sensor, Bluetooth robot, DIY robot, robotics kit,
BOM, schematic, motor driver, IR sensor, maze robot, classroom robot
```

---

## 17. Trademark and License

- **ByByte.DIY™** and the ByByte.DIY logo are trademarks of the project maintainers.  
- License: **CERN Open Hardware Licence version 2 — Strongly Reciprocal (CERN-OHL-S v2)**.  
- Copyright © 2026 ByByte.DIY™ contributors.

---

*End of AI_CONTEXT.md*
