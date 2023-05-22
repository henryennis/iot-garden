import threading as threading
import paho.mqtt.client as paho_mqtt
import queue as queue
import logging as logging
import os
import time as time
from serial import Serial
import json
from dotenv import load_dotenv
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

ARD_HUMIDITY_SENSOR_TOPIC = os.getenv("ARD_HUMIDITY_SENSOR_TOPIC")
ARD_HUMIDITY_ACTUATOR_TOPIC = os.getenv("ARD_HUMIDITY_ACTUATOR_TOPIC")
ARD_HUMIDITY_PORT = os.getenv("ARD_HUMIDITY_PORT")
SERIAL_BAUD_RATE = os.getenv("SERIAL_BAUD_RATE")
LOCAL_INTERFACE_IP = os.getenv("LOCAL_INTERFACE_IP")

def local_mqtt_t():
    local_mqtt_client.connect(LOCAL_INTERFACE_IP, 1883)
    while True:
        if not serial_data_queue.empty():
            data = serial_data_queue.get()
            payload = json.dumps({"sensor": "humidity", "humidityp": data})
            local_mqtt_client.publish("sensors/humidity", payload)
        #Calling mqtt.loop() will process the network traffic and callbacks
        local_mqtt_client.loop(timeout=1.0, max_packets=1)

def read_data_t():
    while True:
        data = serial.readline().decode()
        if data is None:
            #wait some more for port
            continue
        try:
            data_string = data.strip()
            logging.info(f"Received data: {data_string} from {ARD_HUMIDITY_PORT}")
            serial_data_queue.put(data)
        except ValueError:

            #skip iteration if the value is not sensor data
            continue

def change_water_pump_threshold(client, userdata, message):
    logging.info(f"Received data to update threshold: {message} from API")
    serial.write(str(message.payload + "\n").encode())

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))



def main():
    #global makes the variable accessible to all scopes
    global serial
    serial = Serial(ARD_HUMIDITY_PORT, SERIAL_BAUD_RATE)
    time.sleep(2)

    global local_mqtt_client
    local_mqtt_client = paho_mqtt.Client("edge")
    
    local_mqtt_client.on_connect = lambda client, userdata, flags, rc: logging.info(f"Connected to local MQTT broker with result code: {rc}")

    local_mqtt_client.subscribe(ARD_HUMIDITY_ACTUATOR_TOPIC)
    # for processing control messages from the flask server
    local_mqtt_client.on_message = on_message

    global serial_data_queue
    serial_data_queue = queue.Queue()

    # Start the functions concurrently using threads
    read_data_thread = threading.Thread(target=read_data_t)
    mqtt_thread = threading.Thread(target=local_mqtt_t)
    
    read_data_thread.start()
    mqtt_thread.start()


if __name__ == "__main__":
    main()
    
