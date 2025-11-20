# PS3604L

## Overview

The PS3604L is a 144 Watt, high performance dc power supply with output current measurement capability in the microampere range.
Combination of bench-top and system features in these dc source.
For more photos to /Photo.

<img src="Pictures/face.jpg" style="zoom:25%;" />

### Convenient bench-top features

- Up to 144 Watts output power
- Easy to use knob for voltage and current settings
- IPS 160x128 pixel front panel display
- Excellent load and line regulation; low ripple and noise
- Measurement capability down to microampere levels
- Light weight

### Flexible system features

- 10/100BASE-T Ethernet

- Modbus TCP for remote programming

- Web interface for monitoring


## Specifications

Unless otherwise noted, specifications apply when measured after a 30-minute warm-up period.

### Performance Specifications

| Parameter                                                    |                                                           |                             |
| :----------------------------------------------------------- | --------------------------------------------------------: | :-------------------------: |
| **Output Ratings**                                           |                                    Voltage:<br />Current: |    0 – 36 V<br />0 – 4 A    |
| **Programming Accuracy**<br/>(@ 25°C ±5°C)                   |                                    Voltage:<br />Current: |        5 mV<br />2mA        |
| **DC Measurement Accuracy**<br />(@ 25°C ±5°C)               | Voltage:<br />Current 0 – 1 mA:<br />Current 0.001 – 4 A: | 5 mV<br />0.01 mA<br />2 mA |
| **Ripple and Noise**                                         |                        Voltage: (rms)<br />Current (rms): |     0.5 mV<br />1.5 mA      |
| **Load Regulation**                                          |                                                       TBD |             TBD             |
| **Line Regulation**<br/>(change in output voltage<br/>or current for any line<br/>change within ratings) |                                                       TBD |             TBD             |
| **Transient Response Time**<br />*1                          |                                                           |           < 50 μs           |

1. For the output voltage to recover to its previous level within 0.1% of the voltage rating of the unit or 20 millivolts following a
   change in load current of up to 50% of the output current rating

Short term voltage accuracy:

<img src="Pictures/Measured/ShortTermVoltAccuracy.JPG" style="zoom:30%;" />

### Supplemental Characteristics

| Parameter                                                    |                                                              |                                               |
| ------------------------------------------------------------ | -----------------------------------------------------------: | :-------------------------------------------: |
| **Input Rating**<br/>(at full load )                         |                                               230 Vac mains: | 230 Vac nominal, 50/60 Hz, 0.85A, 200 VA max. |
| **Average Programming<br/>Resolution**                       | Voltage (panel):<br />Voltage (remote)<br />Current (panel):<br />Current (remote) |   10 mV<br<br />1 mV<br />1 mA<br />0.1 mA    |
| **Output Voltage Rise/Fall Time**<br/>(for a change from 10% to 90% or<br/>90% to 10% of the total excursion) |                                               Rise<br />Fall |             < 80 μs<br />< 10 μs              |
| **Command Processing Time**                                  |                                                              |                     10 ms                     |
| **Isolation to Ground**<br/>(Maximum from either<br/>output terminal to chassis) |                                                              |                    200 Vdc                    |
| **Dimensions**                                               |                              Height:<br />Width:<br />Depth: |         78 mm<br />158 mm<br />268 mm         |
| **Net weight**                                               |                                                              |                   3.850 kg                    |

------



## Structure

The device has the following modules: Transformer, Rectifier, Regulator, and Front Panel. The structural diagram is shown below.

<img src="PS3604L.drawio.svg" style="zoom:100%;" />

------



## Linear regulator

Linear regulator is a separate module. Module mounted on back aluminum radiator.
Regulator is four level voltage regulator. Hardware CC/CV detector.
Controlled by STM32F337. Used AD4680 SAR 16bit (18bit oversampling mode) for measure voltage and current.
AD5060 16bit DAC use for current and voltage setpoint.
Fan speed proportional control for minimize sound noise.
Module communicate by UART ModBus.
Module [schematic](PCB/PS3604LR/output/PS3604LR.PDF).
<img src="Pictures/regulator_top.jpg" style="zoom:20%;" />

Measurement and comparison of the transient process.
Semiconductor resistors and a switch controlled by a functional generator are used as a transient generator.
One resistor with a resistance of 10 Ohms is connected in parallel to the output of the device under test, the second resistor with a nominal value of 7.3 Ohms is connected in parallel to the device under test through a controlled switch.
Current measurement is performed using a Lecroy AP015 current probe. The voltage measurement is performed directly at the terminals of the device under tested using a high impedance passive probe.

Test 1. Both devices are set up the same, 8V 4A, the table shows the graphs of the current rise transient process measurement:

|                        Agilent 6611C                         |                           PS3604L                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="Pictures/v3.3_compare_with_6611C/setting_8V_4A/6611C_rs.png" style="zoom:60%;" /> | <img src="Pictures/v3.3_compare_with_6611C/setting_8V_4A/3604L_rs.png" style="zoom:60%;" /> |

Test 2. Both devices are set up the same, 8V 4A, the table shows the graphs of the current fall transient process measurement:

|                        Agilent 6611C                         |                           PS3604L                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                                                              |                                                              |
| <img src="Pictures/v3.3_compare_with_6611C/setting_8V_4A/6611C_fl.png" style="zoom:60%;" /> | <img src="Pictures/v3.3_compare_with_6611C/setting_8V_4A/3604L_fl.png" style="zoom:60%;" /> |

Test 3. Both devices are set up the same, 8V 1A, the table shows the graphs of the current rise transient process measurement:

|                        Agilent 6611C                         |                           PS3604L                            |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                                                              |                                                              |
| <img src="Pictures/v3.3_compare_with_6611C/setting_8V_1A/6611C.png" style="zoom:60%;" /> | <img src="Pictures/v3.3_compare_with_6611C/setting_8V_1A/3604L.png" style="zoom:60%;" /> |

In more detail, PS3604L:

<img src="Pictures/v3.3_compare_with_6611C/setting_8V_1A/3604L_det.png" style="zoom:100%;" />

------



## Front panel

Front panel is GUI and Ethernet bridge.  
Build on STM32F407 MCU, LAN8720 as Eth PHY.  
Module [schematic](PCB/PS3604LF/Project%20Outputs%20for%20PS3604LF/PS3604LF.PDF).
<img src="Pictures/IMG_4574.JPG" style="zoom:20%;" />

------



## Extra application

1. Measure series output characteristics of a MOSFET. [Link](/Firmware/Scripts/x-curve.py) to script.

<img src="Pictures/Measured/IRF3710.svg" figcaption="Measured series output characteristics of a MOSFET" style="zoom:67%;" />
