# PS3604L

## Overview

The PS3604L is a 144 Watt, high performance dc power supply with output current measurement capability in the microampere range.
Combination of bench-top and system features in these dc source.
For more photos to /Photo.

<img src="Photo/face.jpg" style="zoom:25%;" />

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
| **Ripple and Noise**                                         |                                                       TBD |             TBD             |
| **Load Regulation**                                          |                                                       TBD |             TBD             |
| **Line Regulation**<br/>(change in output voltage<br/>or current for any line<br/>change within ratings) |                                                       TBD |             TBD             |
| **Transient Response Time**<br />*1                          |                                                           |           < 50 μs           |

1. For the output voltage to recover to its previous level within 0.1% of the voltage rating of the unit or 20 millivolts following a
   change in load current of up to 50% of the output current rating

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

## Linear regulator

Linear regulator is a individual module. Module mounted on back cooler.
Regulator is four level voltage regulator. Hardware CC/CV detector.
Controlled by STM32F337. Used SAR 16bit (18bit oversampling mode) for measure voltage and current.
AD5663 16bit DAC use for current and voltage setpoint.
Used fan speed proportional control for minimize sound noise.
Module communicate by UART ModBus.
Module [schematic](PCB/PS3604LR/output/PS3604LR.PDF).
<img src="Photo/regulator_top.jpg" style="zoom:20%;" />

## Front panel

Front panel is GUI and Ethernet bridge.  
Build on STM32F407 MCU, LAN8720 as Eth PHY.  
Module [schematic](PCB/PS3604LF/Project%20Outputs%20for%20PS3604LF/PS3604LF.PDF).
<img src="Photo/IMG_4574.JPG" style="zoom:20%;" />

