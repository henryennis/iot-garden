import random
import threading
import time


class SerialEmulator:
    def __init__(self, interval=1, min_value=0, max_value=100):
        self.interval = interval
        self.min_value = min_value
        self.max_value = max_value
        self._running = False
        self._thread = None

    def _generate_random_value(self):
        return random.randint(self.min_value, self.max_value)

    def _emulate_serial_read(self):
        while self._running:
            random_value = self._generate_random_value()
            self.readline = lambda: f"{random_value}\n".encode()
            time.sleep(self.interval)

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._emulate_serial_read)
            self._thread.start()

    def stop(self):
        if self._running:
            self._running = False
            self._thread.join()
            self._thread = None

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