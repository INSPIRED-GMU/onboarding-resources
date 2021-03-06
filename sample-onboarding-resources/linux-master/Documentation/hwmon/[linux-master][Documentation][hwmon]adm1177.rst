Kernel driver adm1177
=====================

Supported chips:
  * Analog Devices ADM1177
    Prefix: 'adm1177'
    Datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/ADM1177.pdf

Author: Beniamin Bia <beniamin.bia@analog.com>


Description
-----------

This driver supports hardware monitoring for Analog Devices ADM1177
Hot-Swap Controller and Digital Power Monitors with Soft Start Pin.


Usage Notes
-----------

This driver does not auto-detect devices. You will have to instantiate the
devices explicitly. Please see Documentation/i2c/instantiating-devices.rst
for details.


Sysfs entries
-------------

The following attributes are supported. Current maxim attribute
is read-write, all other attributes are read-only.

in0_input		Measured voltage in microvolts.

curr1_input		Measured current in microamperes.
curr1_max_alarm		Overcurrent alarm in microamperes.
