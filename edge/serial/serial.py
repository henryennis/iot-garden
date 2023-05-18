
import threading
import time
from serial import Serial
from serial_emulator import SerialEmulator

class Serial:
    MODE_NORMAL = "normal"
    MODE_TEST = "test"

    def __init__(self, *args, **kwargs):
        self.mode = kwargs.pop("mode", self.MODE_NORMAL)
        self.interval = kwargs.pop("interval", 1)
        self.min_value = kwargs.pop("min_value", 0)
        self.max_value = kwargs.pop("max_value", 100)

        self.serial = Serial(*args, **kwargs)
        self.emulator = SerialEmulator(self.interval, self.min_value, self.max_value)

        if self.mode == self.MODE_TEST:
            self.emulator.start()

    def readline(self):
        if self.mode == self.MODE_TEST:
            return self.emulator.readline()
        else:
            return self.serial.readline()

    def close(self):
        if self.mode == self.MODE_TEST:
            self.emulator.stop()
        self.serial.close()

"""
# Usage example
if __name__ == "__main__":
    # Emulation mode
    adapter = PySerialAdapter(port='COM1', baudrate=9600, mode=PySerialAdapter.MODE_TEST)
    time.sleep(5)  # Run the emulator for 5 seconds
    for _ in range(5):
        print(f"Received value: {adapter.readline().decode().strip()}")
    adapter.close()

    # Normal mode
    adapter = PySerialAdapter(port='COM1', baudrate=9600)
    # Use the adapter as a regular serial.Serial instance
    adapter.close()
"""