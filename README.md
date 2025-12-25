# 15 Weeks Of Electronics

# Master Engineering Roadmap: Quantum, VLSI, \& Embedded

**Target:** Industry-Ready Portfolio in 15 Weeks  
**Hardware:** Sipeed Tang Nano 4K, ESP32-WROOM-32  
**Strategy:** Deep Dive (Sequential) — Quantum $\\to$ VLSI $\\to$ Embedded

---

## 🎯 Phase 1: Quantum Computing (The Algorithm Architect)

**Weeks 1–5** **Focus:** From Linear Algebra to Variational Chemistry Simulation.  
**Primary Resource:** *Quantum Mechanics: The Theoretical Minimum* (Susskind) \& IBM Quantum Learning.

| Week | Focus Area | Study Stop Point (Definition of Done) | \*\*LinkedIn Project Milestone\*\* |
| :--- | :--- | :--- | :--- |
| \*\*01\*\* | \*\*The Qubit \& Physics\*\* | \*\*Susskind:\*\* Ch 1 (Systems), Ch 2 (Quantum States).<br>\*\*Math:\*\* Manually calculate $H\\|0\\rangle$ \& $X\\|0\\rangle$. | \*\*"The Bloch Sphere Visualizer"\*\*<br>Python script that accepts a gate matrix (H, X, Z) and plots the resulting vector on the Bloch sphere using `qiskit.visualization`. |
| \*\*02\*\* | \*\*Entanglement\*\* | \*\*Susskind:\*\* Ch 6 (Entanglement).<br>\*\*Concept:\*\* Tensor Products \& Bell States.<br>\*\*Syllabus:\*\* "Multiple qubits, Teleportation". | \*\*"Teleportation Verified"\*\*<br>Implement the Teleportation protocol in Qiskit. Add state tomography code to prove the state was transferred with >99% fidelity. |
| \*\*03\*\* | \*\*Algorithms I\*\* | \*\*Qiskit Textbook:\*\* "Deutsch-Jozsa Algorithm".<br>\*\*Concept:\*\* Phase Kickback \& Oracles.<br>\*\*Syllabus:\*\* "Deutsch’s algorithm". | \*\*"The Oracle Breaker"\*\*<br>Code a Deutsch-Jozsa solver. Create a random hidden function (Constant vs. Balanced) and identify it in exactly \*one\* quantum query. |
| \*\*04\*\* | \*\*Error Correction\*\* | \*\*Qiskit Textbook:\*\* "Quantum Error Correction".<br>\*\*Concept:\*\* $T\_1$ (Relaxation) vs $T\_2$ (Dephasing).<br>\*\*Syllabus:\*\* "Decoherence". | \*\*"Fighting Entropy"\*\*<br>Simulate a \*\*3-Qubit Repetition Code\*\* with artificial noise. Plot a graph of \*Error Rate vs. Circuit Depth\* showing how your code fixes bit-flips. |
| \*\*05\*\* | \*\*VQE (Chemistry)\*\* | \*\*Qiskit Nature Docs:\*\* "Ground State Energy".<br>\*\*Concept:\*\* Variational Forms \& Ansatz.<br>\*\*Syllabus:\*\* "Quantum Simulation". | \*\*"H2 Molecule Simulator"\*\*<br>Calculate the bond dissociation curve of a Hydrogen molecule using the VQE algorithm. (Industry-standard task). |

---

## ⚡ Phase 2: VLSI \& FPGA (The Silicon Architect)

**Weeks 6–10** **Focus:** From CMOS Theory to Hardware AI Accelerators.  
**Hardware:** Sipeed Tang Nano 4K.  
**Method:** Use *Lushay Labs (9K)* for Verilog syntax, but *Sipeed GitHub* for 4K Pinouts.

| Week | Focus Area | Study Stop Point (Definition of Done) | \*\*LinkedIn Project Milestone\*\* |
| :--- | :--- | :--- | :--- |
| \*\*06\*\* | \*\*FSMs \& Toolchain\*\* | \*\*Lushay:\*\* "Installation" $\\to$ "LCD Example".<br>\*\*Sipeed Repo:\*\* Check `led\_test` for `.cst` pins.<br>\*\*Syllabus:\*\* "Simplified state machines". | \*\*"Traffic Light Controller"\*\*<br>A robust Finite State Machine (FSM) on FPGA. Video of LEDs cycling Red-Yellow-Green with precise timing (using clock dividers). |
| \*\*07\*\* | \*\*Timing \& Arithmetic\*\* | \*\*Weste \& Harris:\*\* Ch 4 (Delay Models).<br>\*\*Gowin:\*\* Reading "Timing Analysis Reports".<br>\*\*Syllabus:\*\* "Adders, Multipliers, Elmore Delay". | \*\*"The Adder Showdown"\*\*<br>Synthesize a Ripple Carry vs. Carry Lookahead Adder. Post a screenshot of the \*\*Timing Report\*\* comparing their nanosecond delays. |
| \*\*08\*\* | \*\*Memory Systems\*\* | \*\*Gowin Docs:\*\* "IP Core Generator" (Block RAM).<br>\*\*Concept:\*\* FIFO Buffers \& Pointers.<br>\*\*Syllabus:\*\* "Memories: DRAM, SRAM". | \*\*"FIFO Buffer Design"\*\*<br>Implement a First-In-First-Out memory buffer. Show data entering at one speed and leaving at another (Clock Domain Crossing). |
| \*\*09\*\* | \*\*Systolic Arrays (AI)\*\* | \*\*Topic:\*\* Google TPU Architecture.<br>\*\*Verilog:\*\* Pipelined MAC (Multiply-Accumulate) units.<br>\*\*Syllabus:\*\* "AI Accelerators". | \*\*"Mini-TPU Accelerator"\*\*<br>Design a \*\*Systolic Array\*\* (2x2 grid) in Verilog. Show a simulation waveform of matrix multiplication happening in parallel. |
| \*\*10\*\* | \*\*The Hybrid SoC\*\* | \*\*Sipeed Wiki:\*\* "Cortex-M3" section.<br>\*\*Video:\*\* "Getting Started with Cortex M3".<br>\*\*Goal:\*\* C code blinking FPGA LED. | \*\*"Hardware-Software Co-Design"\*\*<br>Instantiate the Cortex-M3 core inside the FPGA. Write C code to control your custom hardware logic from Week 6. |

---

## 📡 Phase 3: Embedded Systems (The IoT Engineer)

**Weeks 11–15** **Focus:** From Registers to Cloud IoT \& OTA Updates.  
**Hardware:** ESP32-WROOM-32.

| Week | Focus Area | Study Stop Point (Definition of Done) | \*\*LinkedIn Project Milestone\*\* |
| :--- | :--- | :--- | :--- |
| \*\*11\*\* | \*\*Bare Metal Arch\*\* | \*\*Ref Manual:\*\* "IO MUX / GPIO Matrix".<br>\*\*Skill:\*\* Bit-masking \& Pointers (No Drivers).<br>\*\*Syllabus:\*\* "Registers, Instruction Set". | \*\*"Bare Metal Blink"\*\*<br>C snippet showing direct register manipulation (setting bit masks manually) vs. the standard library way. |
| \*\*12\*\* | \*\*Protocols\*\* | \*\*ESP-IDF Docs:\*\* "SPI Master Driver".<br>\*\*Datasheet:\*\* SPI Timing Diagrams.<br>\*\*Syllabus:\*\* "UART, SPI". | \*\*"Chip-to-Chip Talk"\*\*<br>Connect ESP32 (Master) to Tang Nano (Slave). ESP32 sends a command; FPGA changes LED color. |
| \*\*13\*\* | \*\*RTOS Basics\*\* | \*\*Shawn Hymel:\*\* Videos 1–5 (Tasks, Queues).<br>\*\*Concept:\*\* Preemptive Scheduling \& Mutexes.<br>\*\*Syllabus:\*\* "RTOS, Scheduling". | \*\*"The RTOS Dashboard"\*\*<br>Serial log showing a High-Priority task interrupting a Low-Priority task. Use a Mutex to prevent data corruption. |
| \*\*14\*\* | \*\*WiFi \& IoT\*\* | \*\*ESP-IDF Docs:\*\* "HTTP Client".<br>\*\*Skill:\*\* JSON Parsing \& API Requests.<br>\*\*Syllabus:\*\* "Interface Wi-Fi Devices". | \*\*"Live IoT Monitor"\*\*<br>Fetch live weather/stock data via Wi-Fi from a public API and display it on an OLED or Serial Monitor. |
| \*\*15\*\* | \*\*OTA Updates\*\* | \*\*ESP-IDF Docs:\*\* "OTA Updates".<br>\*\*Concept:\*\* Partitions (Factory vs OTA\_0).<br>\*\*Skill:\*\* Flash writing. | \*\*"Self-Healing Firmware"\*\*<br>Video of the device downloading a new update from the cloud and rebooting into new features automatically. |

---

## 📚 Consolidated Resources

### **1. Quantum Computing**

* **Book:** *Quantum Mechanics: The Theoretical Minimum* (Leonard Susskind).
* **Course:** [IBM Quantum Learning](https://learning.quantum.ibm.com/) (Modules: Single Systems, Multiple Systems, Algorithms).
* **Library:** [Qiskit Documentation](https://qiskit.org/documentation/).

### **2. VLSI (Tang Nano 4K Specific)**

* **Official Examples (Pinouts/Cortex-M3):** [Sipeed Tang Nano 4K GitHub](https://github.com/sipeed/TangNano-4K-example).
* **Verilog Syntax Tutorial:** [Lushay Labs (Tang Nano 9K Series)](https://learn.lushaylabs.com/).
* **Theory Book:** *CMOS VLSI Design: A Circuits and Systems Perspective* (Weste \& Harris).

### **3. Embedded Systems (ESP32)**

* **Documentation:** [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/).
* **Video Course:** [Shawn Hymel - Introduction to RTOS](https://www.youtube.com/playlist?list=PLPW8O6W-1chzwNTOkPrQccOm7F9Jk0FrA).
* **Reference:** *ESP32 Technical Reference Manual* (PDF).

---

