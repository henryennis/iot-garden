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

2. Configure AWS CLI to use your AWS account

   [Using environment variables to configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

## Setting up AWS IoT Core & CloudWatch
   The following setup describes how to create a new IoT device in AWS cloud that will serve as the entry point for MQTT data published on the Fog network (local --> cloud).

1. Create an IoT device that will serve as the host for MQTT data
   The device is named bridge because it is resposible for receiving the data our local MQTT broker publishes.

   ```
   aws iot create-thing --thing-name bridge
   ```
2. Now we need a method of connecting our local broker to the MQTT broker in AWS cloud. To connect to the broker there are 3 authentication requirements:
   - A cirtificate associated with the thing "bridge" we created earlier
   - Private key
   - AWS root CA cirtificate

   Run the following commands to download these objects into the ./authentication directory:

   ```
   cd ./authentication
   ```
   ```
   aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key
   ```
   ```
   wget -O root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
   ```
   ```
   aws iot attach-thing-principal --thing-name bridge --principal <CERTIFICATE_ARN>
   ```
## Installing and configuring Mosquitto MQTT
1. Open the terminal and run the following command to install Mosquitto MQTT:

   ```
   sudo apt-get update && sudo apt-get install mosquitto mosquitto-clients
   ```

2. Once the installation is complete, run the following command to stop the Mosquitto MQTT broker service (we wish to run Mosquitto broker as a program):

   ```
   sudo systemctl stop mosquitto && sudo systemctl disable mosquitto
   ```
3. Now you need to edit the mosquitto.conf file provided by the repo by replacing the following with the path to your authentication objects

   ```
   bridge_cafile yourpath
   bridge_certfile yourpath
   bridge_keyfile yourpath
   ```
4. Get your AWS IoT endpoint domain

   ```
   aws iot describe-endpoint --endpoint-type iot:Data-ATS
   ```
5. Edit the mosquitto.conf file by changing the endpoint paramater, replacing it with your own.


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
1. Install pip packages
    ```
    pip install -r requirements.txt
    ```
2. Launch Mosquitto broker
   ```
   mosquitto -c mosquitto.conf -v
   ```
3. Launch the web API
   ```
   python "./api/server.py"
   ```
4. Launch the Fog server master node
   ```
   python "./api/rpi_master_humidity"
   ```


