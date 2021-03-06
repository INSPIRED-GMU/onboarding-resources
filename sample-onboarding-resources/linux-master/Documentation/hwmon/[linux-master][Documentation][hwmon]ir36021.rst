.. SPDX-License-Identifier: GPL-2.0

Kernel driver ir36021
=====================

Supported chips:

  * Infineon IR36021

    Prefix: ir36021
    Addresses scanned: -

    Datasheet: Publicly available at the Infineon website
      https://www.infineon.com/dgdl/ir36021.pdf?fileId=5546d462533600a4015355d0aa2d1775

Authors:
      - Chris Packham <chris.packham@alliedtelesis.co.nz>

Description
-----------

The IR36021 is a dual-loop digital multi-phase buck controller designed for
point of load applications.

Usage Notes
-----------

This driver does not probe for PMBus devices. You will have to instantiate
devices explicitly.

Sysfs attributes
----------------

======================= ===========================
curr1_label             "iin"
curr1_input             Measured input current
curr1_alarm             Input fault alarm

curr2_label             "iout1"
curr2_input             Measured output current
curr2_alarm             Output over-current alarm

in1_label               "vin"
in1_input               Measured input voltage
in1_alarm               Input under-voltage alarm

in2_label               "vout1"
in2_input               Measured output voltage
in2_alarm               Output over-voltage alarm

power1_label            "pin"
power1_input            Measured input power
power1_alarm            Input under-voltage alarm

power2_label            "pout1"
power2_input            Measured output power

temp1_input             Measured temperature
temp1_alarm             Temperature alarm

temp2_input             Measured other loop temperature
temp2_alarm             Temperature alarm
======================= ===========================
