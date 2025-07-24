# Virtual Input Pins

This repository contains Python code that emulates a minimal
microcontroller with eight input pins.  These pins are named ``pin1``
through ``pin8`` and are presented under the prefix ``ams`` so they can be
referenced as ``ams:pin1`` ... ``ams:pin8`` in Klipper configurations.
The intent is that Klipper treats the pins as coming from a real
microcontroller called ``ams``.

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

The module ``input_pins.py`` loads the virtual MCU whenever the
configuration file contains an ``[input_pins]`` section.  In your
``printer.cfg`` simply add::

    [input_pins]

When Klipper loads the module it immediately registers the ``ams`` prefix
so that pins such as ``ams:pin1`` may be referenced anywhere in the
configuration.  **Make sure the ``[input_pins]`` section comes *before* any
other section that refers to an ``ams:`` pin**&mdash;otherwise those sections
will be processed first and Klipper will complain with ``Unknown pin chip
name 'ams'``.  Calling ``input_pins.load_config_file('printer.cfg')`` from
Python has the same effect for simple testing outside of Klipper.

Once loaded, you can reference the pins in other sections of
`printer.cfg` using the `ams:` prefix, for example::

    [filament_switch_sensor my_filament]
    switch_pin: ams:pin1

Copy `input_pins.py` into Klipper's `klippy/extras/` directory so the
module can be loaded as `extras.input_pins`.  All required classes are in
this single file.

This setup shows how a configuration section can trigger loading custom
code, but a real deployment would need additional work to fully emulate
the MCU protocol.
