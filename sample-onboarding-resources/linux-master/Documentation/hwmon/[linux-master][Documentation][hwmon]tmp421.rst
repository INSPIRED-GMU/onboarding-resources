Kernel driver tmp421
====================

Supported chips:

  * Texas Instruments TMP421

    Prefix: 'tmp421'

    Addresses scanned: I2C 0x2a, 0x4c, 0x4d, 0x4e and 0x4f

    Datasheet: http://focus.ti.com/docs/prod/folders/print/tmp421.html

  * Texas Instruments TMP422

    Prefix: 'tmp422'

    Addresses scanned: I2C 0x4c, 0x4d, 0x4e and 0x4f

    Datasheet: http://focus.ti.com/docs/prod/folders/print/tmp421.html

  * Texas Instruments TMP423

    Prefix: 'tmp423'

    Addresses scanned: I2C 0x4c and 0x4d

    Datasheet: http://focus.ti.com/docs/prod/folders/print/tmp421.html

  * Texas Instruments TMP441

    Prefix: 'tmp441'

    Addresses scanned: I2C 0x2a, 0x4c, 0x4d, 0x4e and 0x4f

    Datasheet: https://www.ti.com/product/tmp441

  * Texas Instruments TMP442

    Prefix: 'tmp442'

    Addresses scanned: I2C 0x4c and 0x4d

    Datasheet: https://www.ti.com/product/tmp442

Authors:

	Andre Prendel <andre.prendel@gmx.de>

Description
-----------

This driver implements support for Texas Instruments TMP421, TMP422,
TMP423, TMP441, and TMP442 temperature sensor chips. These chips
implement one local and up to one (TMP421, TMP441), up to two (TMP422,
TMP442) or up to three (TMP423) remote sensors. Temperature is measured
in degrees Celsius. The chips are wired over I2C/SMBus and specified
over a temperature range of -40 to +125 degrees Celsius. Resolution
for both the local and remote channels is 0.0625 degree C.

The chips support only temperature measurement. The driver exports
the temperature values via the following sysfs files:

**temp[1-4]_input**

**temp[2-4]_fault**

Each sensor can be individually disabled via Devicetree or from sysfs
via:

**temp[1-4]_enable**

If labels were specified in Devicetree, additional sysfs files will
be present:

**temp[1-4]_label**
