import argparse
import subprocess

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="A simple command-line program to launch and mannage our application.")

    # Add arguments
    parser.add_argument("--test", action="store_true", help="Enable test mode")

    # Parse command line arguments
    args = parser.parse_args()

    # Access parsed arguments
    test_mode = args.test

    # Implement functionality based on passed arguments
    exe(args)

def exe(test_mode):
    if (test_mode):
        result = subprocess.run("C:\dev\iot-garden\tests\serial\Emulate_serial\x64\Debug\Emulate_serial.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    result = subprocess.run("mosquito -c mosquitto.conf -v" , stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    rpi_edge1 = subprocess.run("mosquito -c mosquitto.conf -v" , stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    

if __name__ == "__main__":
    main()