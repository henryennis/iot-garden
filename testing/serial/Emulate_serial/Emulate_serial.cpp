#include <iostream>
#include <chrono>
#include <thread>
#include <fstream>
#include <string>

int main() {
    std::string port;
#ifdef _WIN32
    port = "COM7";  // Change this to the correct port on your system
#else
    port = "/dev/pts/1";  // Change this to the correct port on your system
#endif

    // Open the virtual serial port
    std::ofstream serial(port, std::ios_base::out | std::ios_base::binary);

    if (!serial.is_open()) {
        std::cerr << "Error opening serial port: " << port << std::endl;
        return 1;
    }

    while (true) {
        std::string data = "Hello from CPP program!\n";
        serial.write(data.c_str(), data.size());
        serial.flush();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    serial.close();

    return 0;
}