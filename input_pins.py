"""Klipper plugin to create eight virtual input pins.

This module checks for an [input_pins] section in the given configuration
file and, if present, loads VirtualMCU to provide ams:pin1-ams:pin8.

This is a simplified example intended to illustrate how one might hook a
custom module into Klipper's configuration system. It does not implement
the full Klipper MCU protocol.
"""

import configparser
from typing import Optional

try:  # When loaded by Klipper
    from .. import pins as klipper_pins  # type: ignore
except Exception:  # pragma: no cover - standalone use
    klipper_pins = None

# Import VirtualMCU from the same package when running as a Klipper
# extras module.  Fallback to a direct import so the file can still be
# executed or compiled standalone during development.
try:
    from .virtual_mcu import VirtualMCU
except ImportError:  # pragma: no cover - fallback when not in package
    from virtual_mcu import VirtualMCU


class InputPins:
    """Manage a VirtualMCU when [input_pins] is present."""

    def __init__(self) -> None:
        self.mcu: Optional[VirtualMCU] = None

    def load_from_file(self, cfg_path: str) -> None:
        """Load configuration and initialize VirtualMCU if needed."""
        parser = configparser.ConfigParser()
        parser.read(cfg_path)
        if "input_pins" in parser:
            prefix = parser["input_pins"].get("prefix", "ams")
            self.mcu = VirtualMCU(prefix=prefix)
            self.mcu.register_chip()
            print(
                "InputPins: Virtual MCU loaded with pins:",
                ", ".join(self.mcu.list_pins()),
            )
        else:
            print("InputPins: [input_pins] not defined; module not loaded")


def load_config(cfg_path: str) -> InputPins:
    """Convenience wrapper for standalone testing."""
    ip = InputPins()
    ip.load_from_file(cfg_path)
    return ip


def load_config_prefix(config):  # pragma: no cover - used by Klipper
    """Entry point used by Klipper when [input_pins] is present."""
    prefix = config.get('prefix', 'ams')
    ip = InputPins()
    ip.mcu = VirtualMCU(prefix=prefix)
    ip.mcu.register_chip()
    config.get_printer().add_object('virtual_mcu', ip.mcu)
    return ip
