
## Power Supplies
The Compute Module has six separate supplies that must be present and powered at all times; you cannot
leave any of them unpowered, even if a specific interface or GPIO bank is unused. The six supplies are
as follows:

- 1. **VBAT** is used to power the BCM283x processor core. It feeds the SMPS that generates the chip
core voltage. `min 2.5V ~ 5V`
- 2. **3V3** powers various BCM283x PHYs, IO and the eMMC Flash. `3.3V`
- 3. **1V8** powers various BCM283x PHYs, IO and SDRAM. (1.8V)
- 4. **VDAC** powers the composite (TV-out) DAC. `2.8V`
- 5. **GPIO0-27 VREF** powers the GPIO 0-27 IO bank. `1.8V ~ 3.3V`
- 6. **GPIO28-45 VREF** powers the GPIO 28-45 IO bank. `1.8V ~ 3.3V`