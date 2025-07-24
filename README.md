# Virtual Input Pins

This repository contains Python code that emulates a minimal
microcontroller with eight input pins.  These pins are named `pin1`
through `pin8` and are presented under the prefix `ams` so they can be
referenced as `ams:pin1` ... `ams:pin8` in Klipper configurations.

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

### Loading via printer.cfg

The module `input_pins.py` provides a small example of how a Klipper
plugin might load the virtual MCU when the configuration contains an
`[input_pins]` section.  In your `printer.cfg`, add::

    [input_pins]

Then call `input_pins.load_config('printer.cfg')` from Python (or from
Klipper's module loader) and the virtual MCU will be created
automatically.

This setup shows how a configuration section can trigger loading custom
code, but a real deployment would need additional work to fully emulate
the MCU protocol.
