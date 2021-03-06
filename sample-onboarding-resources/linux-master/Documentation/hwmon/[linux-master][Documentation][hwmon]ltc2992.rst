.. SPDX-License-Identifier: GPL-2.0

Kernel driver ltc2992
=====================

Supported chips:
  * Linear Technology LTC2992
    Prefix: 'ltc2992'
    Datasheet: https://www.analog.com/media/en/technical-documentation/data-sheets/ltc2992.pdf

Author: Alexandru Tachici <alexandru.tachici@analog.com>


Description
-----------

This driver supports hardware monitoring for Linear Technology LTC2992 power monitor.

LTC2992 is a rail-to-rail system monitor that measures current,
voltage, and power of two supplies.

Two ADCs simultaneously measure each supply's current. A third ADC monitors
the input voltages and four auxiliary external voltages.


Sysfs entries
-------------

The following attributes are supported. Limits are read-write,
all other attributes are read-only.

in_reset_history	Reset all highest/lowest values.

inX_input		Measured voltage.
inX_lowest		Minimum measured voltage.
inX_highest		Maximum measured voltage.
inX_min			Minimum voltage allowed.
inX_max			Maximum voltage allowed.
inX_min_alarm		An undervoltage occurred. Cleared on read.
inX_max_alarm		An overvoltage occurred. Cleared on read.

currX_input		Measured current.
currX_lowest		Minimum measured current.
currX_highest		Maximum measured current.
currX_min		Minimum current allowed.
currX_max		Maximum current allowed.
currX_min_alarm		An undercurrent occurred. Cleared on read.
currX_max_alarm		An overcurrent occurred. Cleared on read.

powerX_input		Measured power.
powerX_input_lowest	Minimum measured voltage.
powerX_input_highest	Maximum measured voltage.
powerX_min		Minimum power.
powerX_max		Maximum power.
powerX_min_alarm	An underpower occurred. Cleared on read.
powerX_max_alarm	An overpower occurred. Cleared on read.
