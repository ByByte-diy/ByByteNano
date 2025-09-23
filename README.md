## "БАБАЙ" (ByByte) Nano — Educational Robot Platform
Українська: `README.uk.md`


<img src="cad/img/3D_PCB_main.png" alt="ByByte Nano 3D View" width="400" height="400" />

**БАБАЙ Nano** is a compact, beginner‑friendly educational robot platform from the ByByte series. It is designed for quick assembly, safe classroom use, and clear learning of robotics fundamentals: electronics, sensors, motor control, and embedded programming. Compared to the more advanced ByByte Mega, Nano focuses on simplicity and affordability while remaining extendable.

- Related project: see the larger sibling, ByByte Mega, for a more feature‑rich variant ([ByByte Mega README](https://github.com/ByByte-diy/ByByteMega/blob/main/README.md)).

### Key Features
- Beginner‑friendly: simple assembly and clear layout
- Compact PCB: optimized footprint for classrooms and workshops
- Modular design: expansion headers for add‑ons and sensors
- Open hardware: schematic and PCB sources included
- Open firmware: works with common Arduino‑compatible toolchains

### Hardware Overview
- Main board: ByByte Nano PCB
- Microcontroller: Arduino‑compatible, Nano‑class form factor (ATmega328)
- Typical peripherals: motor drivers, line sensors, LEDs, power regulation
- Connectors: clearly labeled I/O and power headers for quick prototyping

View the full schematic:
- `hardware/schematics/ByByte_main_schematic.pdf`

Board previews:
- Top: `cad/img/2D_PCB_top.png`
- Bottom: `cad/img/2D_PCB_bottom.png`

### Technical Specifications (high‑level)
- Power: 9V battery (PP3/“Krona”)
- CPU: Arduino Nano (ATmega328)
- Drive: micro N20 geared DC motors, approx. 600–1000 rpm
- Connectivity: USB (Arduino Nano), Bluetooth (HC‑02/HC‑05/HC‑06), optional Wi‑Fi via ESP32‑CAM

### Sensors and Interfaces
- 5 line sensors: line‑following capability
- Side optical analog sensors: maze navigation or obstacle avoidance
- Front distance sensor: ultrasonic range measurement
- Analog light sensor: ambient light intensity
- IR receiver: remote control via IR remote
- Bluetooth: smartphone/PC control support
- 2× WS2812 RGB LEDs: “headlights” visual feedback
- Passive buzzer: audible feedback

### Additional Peripherals
You can install an optional ESP32‑CAM module to stream video over Wi‑Fi. The ESP module can be programmed directly from the robot; set jumpers J1–J3 according to the schematic. You can also configure communication between ESP and the Arduino Nano to control the robot over Wi‑Fi.

### Mobility
Two side wheels provide differential (tank‑style) drive for precise motion control.

### Compatibility
Fully compatible with the Arduino IDE and a wide range of Arduino libraries, making it accessible for both beginners and experienced users.

### Educational Focus
Designed to help learners develop core programming and robotics skills through hands‑on projects:
- Integrate sensors and process data
- Program motion algorithms for obstacle avoidance, line following, and maze navigation
- Use visual and audio feedback to increase interactivity
- Understand controller‑based platforms and communication/control basics

### Assembly Notes
- Besides the PCB and ready‑made modules, a few discrete components are needed for assembly; the design targets easy soldering and widely available modules
- Before soldering the robot’s power modules, set the correct output voltages (5 V and 3.3 V) to protect sensitive electronics
- Before first power‑up, verify polarity; ideally power on without modules inserted and check all rails
- Start with power and logic tests, then connect motors and sensors
- Keep wires short and secure to reduce noise
- Finally, test the robot with example sketches before full use

### Bill of Materials (indicative)
- 1× ByByte Nano PCB
- 1× Arduino Nano controller
- 1× Motor driver module (DRV8833)
- 2× N20 geared DC motors (around 600 rpm) + wheels for 3 mm shaft
- Line/reflectance sensor array (5× TCRT5000)
- Power source: 9V PP3 battery (“Krona”)
- 1× Ultrasonic sensor HC‑SR04
- 1× Bluetooth module (HC‑02/HC‑05/HC‑06 or compatible)
- 2× DC‑DC buck modules (e.g., MINI‑360) adjusted to required voltages
- Misc: pin headers, screws, wires, buzzer, sensors and other components

### Troubleshooting
- No power: check polarity and regulator output
- No USB upload: check board/port selection, drivers, and jumper positions J1–J3
- Motors not spinning: verify driver wiring and module health
- Sensors unresponsive: verify 5 V rail and wiring

### How to Contribute
Contributions are welcome:
1. Test and report issues by creating an issue
2. Help us fix problems and improve documentation
3. Optimize or enhance libraries by forking the repo and submitting a pull request

### License
This project is released under the license specified in `LICENSE`.


