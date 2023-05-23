# Installing AWS CLI, Mosquitto MQTT, and Python 3.x for the IoT Garden Project

## Introduction
This manual will guide you through the installation process of the AWS CLI, Mosquitto MQTT, and Python 3.x for the IoT Garden Project. These tools are essential for building and deploying IoT projects on the AWS platform and communicating with MQTT brokers.

## Prerequisites
Before proceeding with the installation process, make sure that you have the following prerequisites:

- Debian operating system
- Internet connection

## Installing AWS CLI
1. Open the terminal and run the following command to install AWS CLI:

   ```
   sudo apt-get update && sudo apt-get install awscli
   ```

2. Once the installation is complete, run the following command to check the version of AWS CLI:

   ```
   aws --version
   ```

   You should see the version of AWS CLI that you have installed.

## Installing Mosquitto MQTT
1. Open the terminal and run the following command to install Mosquitto MQTT:

   ```
   sudo apt-get update && sudo apt-get install mosquitto mosquitto-clients
   ```

2. Once the installation is complete, run the following command to start the Mosquitto MQTT broker:

   ```
   sudo systemctl start mosquitto
   ```

3. To check the status of the Mosquitto MQTT broker, run the following command:

   ```
   sudo systemctl status mosquitto
   ```

   You should see the status of the Mosquitto MQTT broker, which should say "active (running)".

## Installing Python 3.x
1. Open the terminal and run the following command to install Python 3.x:

   ```
   sudo apt-get update && sudo apt-get install python3
   ```

2. Once the installation is complete, run the following command to check the version of Python 3.x:

   ```
   python3 --version
   ```

   You should see the version of Python 3.x that you have installed.

# Running the project
1. Clone the github repository
    ```
    git clone https://github.com/xSCIven/iot-garden & cd iot-garden
    ```
2. Install pip packages
    ```
    pip install -r requirements.txt
    ```