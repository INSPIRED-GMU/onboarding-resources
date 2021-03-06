.. SPDX-License-Identifier: GPL-2.0

Kernel driver xdpe122
=====================

Supported chips:

  * Infineon XDPE11280

    Prefix: 'xdpe11280'

  * Infineon XDPE12254

    Prefix: 'xdpe12254'

  * Infineon XDPE12284

    Prefix: 'xdpe12284'

Authors:

	Vadim Pasternak <vadimp@mellanox.com>

Description
-----------

This driver implements support for Infineon Multi-phase XDPE112 and XDPE122
family dual loop voltage regulators.
These families include XDPE11280, XDPE12284 and XDPE12254 devices.
The devices from this family compliant with:

- Intel VR13 and VR13HC rev 1.3, IMVP8 rev 1.2 and IMPVP9 rev 1.3 DC-DC
  converter specification.
- Intel SVID rev 1.9. protocol.
- PMBus rev 1.3 interface.

Devices support linear format for reading input voltage, input and output current,
input and output power and temperature.
Device supports VID format for reading output voltage. The below modes are
supported:
- VR12.0 mode, 5-mV DAC - 0x01.
- VR12.5 mode, 10-mV DAC - 0x02.
- IMVP9 mode, 5-mV DAC - 0x03.
- AMD mode 6.25mV - 0x10.

Devices support two pages for telemetry.

The driver provides for current: input, maximum and critical thresholds
and maximum and critical alarms. Critical thresholds and critical alarm are
supported only for current output.
The driver exports the following attributes for via the sysfs files, where
indexes 1, 2 are for "iin" and 3, 4 for "iout":

**curr[3-4]_crit**

**curr[3-4]_crit_alarm**

**curr[1-4]_input**

**curr[1-4]_label**

**curr[1-4]_max**

**curr[1-4]_max_alarm**

The driver provides for voltage: input, critical and low critical thresholds
and critical and low critical alarms.
The driver exports the following attributes for via the sysfs files, where
indexes 1, 2 are for "vin" and 3, 4 for "vout":

**in[1-4]_crit**

**in[1-4_crit_alarm**

**in[1-4]_input**

**in[1-4_label**

**in[1-4]_lcrit**

**in[1-41_lcrit_alarm**

The driver provides for power: input and alarms. Power alarm is supported only
for power input.
The driver exports the following attributes for via the sysfs files, where
indexes 1, 2 are for "pin" and 3, 4 for "pout":

**power[1-2]_alarm**

**power[1-4]_input**

**power[1-4]_label**

The driver provides for temperature: input, maximum and critical thresholds
and maximum and critical alarms.
The driver exports the following attributes for via the sysfs files:

**temp[1-2]_crit**

**temp[1-2]_crit_alarm**

**temp[1-2]_input**

**temp[1-2]_max**

**temp[1-2]_max_alarm**
