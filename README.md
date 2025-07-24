# Virtual Input Pins

This repository contains a small Python module that emulates a minimal
microcontroller with eight virtual input pins.  The pins are named
`pin1` through `pin8` and are exposed using the prefix `ams` so they
can be referenced as `ams:pin1` ... `ams:pin8` in Klipper
configurations.

The code does **not** implement the full Klipper MCU protocol; it is a
lightweight example that can be extended or adapted for integration
with Klipper's host-side code.

## Usage

Run `virtual_mcu.py` directly to create the virtual MCU instance::

    python3 virtual_mcu.py

The script will print the available pins.  Pins can be manipulated by
calling the `set_pin` and `read_pin` methods on the `VirtualMCU`
instance from Python code.

This is intended as a starting point for creating a more complete
virtual MCU that Klipper can communicate with.

