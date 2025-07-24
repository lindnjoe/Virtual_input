class VirtualPin:
    """A configurable digital pin."""

    def __init__(self, name: str, mode: str = "input"):
        self.name = name
        self.mode = mode
        self.state = 0

    def configure(self, mode: str) -> None:
        self.mode = mode

    def read(self) -> int:
        return self.state

    def set_state(self, value: bool) -> None:
        self.state = 1 if value else 0


class VirtualMCU:
    """A minimal MCU emulator exposing 8 input pins."""

    def __init__(self, prefix: str = "ams"):
        self.prefix = prefix
        self.pins = {
            f"pin{i}": VirtualPin(f"{prefix}:pin{i}") for i in range(1, 9)
        }

    def read_pin(self, pin: str) -> int:
        return self.pins[pin].read()

    def set_pin(self, pin: str, value: bool) -> None:
        self.pins[pin].set_state(value)

    def configure_pin(self, pin: str, mode: str) -> None:
        self.pins[pin].configure(mode)

    def list_pins(self):
        return list(self.pins.keys())


if __name__ == "__main__":
    mcu = VirtualMCU()
    print("Virtual MCU initialized with pins:", ", ".join(mcu.list_pins()))
    print(
        "Use mcu.set_pin(name, value) to change pin state "
        "and mcu.read_pin(name) to read it."
    )

