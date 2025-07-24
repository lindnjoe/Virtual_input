# Virtual Input Pins

This repository contains Python code that emulates a minimal
microcontroller with eight input pins.  These pins are named `pin1`
through `pin8` and are presented under the prefix `ams` so they can be
referenced as `ams:pin1` ... `ams:pin8` in Klipper configurations.
The intent is that Klipper treats the pins as coming from a real
microcontroller called `ams`.

The example does **not** implement the full Klipper MCU protocol.  It is
a lightweight demonstration that can be expanded for integration with
Klipper's host-side code.

## Usage

### Simple Python usage

Run `virtual_mcu.py` directly to create a `VirtualMCU` instance:

```bash
python3 virtual_mcu.py
```

The script will print the available pins.  Pins can be manipulated by
calling the `set_pin` and `read_pin` methods from Python code.
For example the output will look like::

    Virtual MCU initialized with pins: ams:pin1, ams:pin2, ...

### Loading via printer.cfg

The module `input_pins.py` provides a small example of how a Klipper
plugin might load the virtual MCU when the configuration contains an
`[input_pins]` section.  In your `printer.cfg`, add::

    [input_pins]
    prefix: ams

Then call `input_pins.load_config_file('printer.cfg')` from Python (or let
Klipper load the module) and the virtual MCU will be created
automatically.  The optional `prefix` setting controls the name used in
pin references (default `ams`).  When loaded by Klipper, the module
registers the prefix so that other sections may refer to pins such as
`ams:pin1` without additional setup.

Make sure the `[input_pins]` section appears *before* any other
sections that reference these pins so that the chip is registered when
Klipper parses the rest of the configuration.

Once loaded, you can reference the pins in other sections of
`printer.cfg` using the `ams:` prefix, for example::

    [filament_switch_sensor my_filament]
    switch_pin: ams:pin1

Copy both `input_pins.py` and `virtual_mcu.py` into Klipper's
`klippy/extras/` directory so the relative import works when the module
is loaded as `extras.input_pins`.

This setup shows how a configuration section can trigger loading custom
code, but a real deployment would need additional work to fully emulate
the MCU protocol.
