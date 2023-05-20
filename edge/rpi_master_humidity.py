from local_mqtt import paho_mqtt
import threading as threading
import queue as queue
import logging as logging
from cloud.aws_mqtt_client import AWSIoTClient
import time as time
from serial import Serial
from env_vars import SERIAL_BAUD_RATE,ARD_HUMIDITY_ACTUATOR_TOPIC,ARD_HUMIDITY_SENSOR_TOPIC, ARD_HUMIDITY_PORT



def local_mqtt_t():
    while True:
        if not serial_data_queue.empty():
            data = serial_data_queue.get()
            local_mqtt_client.publish(ARD_HUMIDITY_SENSOR_TOPIC, data)
        #Calling mqtt.loop() will process the network traffic and callbacks
        local_mqtt_client.loop(timeout=1.0, max_packets=1)


def read_data_t():
    while True:
        data = serial.readline().decode().strip()
        try:
            data = float(data)
            serial_data_queue.put(data)
        except ValueError:
            #skip iteration if the value is not sensor data
            continue


def change_water_pump_threshold(client, userdata, msg):
    serial.write((msg.payload).encode())


def foward_to_aws_mqtt(msg):
    aws_iot_client.publish(msg.topic, msg.data)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    #global makes the variable accessible to all scopes
    global serial
    serial = Serial(ARD_HUMIDITY_PORT, SERIAL_BAUD_RATE)
    time.sleep(2)

    global aws_iot_client
    aws_iot_client = AWSIoTClient()
    aws_iot_client.connect()

    
    global local_mqtt_client
    local_mqtt_client = paho_mqtt.MyMQTTClient()
    local_mqtt_client.connect("localhost", 1883)
    local_mqtt_client.subscribe("actuators/ardunio2/humidity", 1)
    local_mqtt_client.on_connect = lambda client, userdata, flags, rc: print("Connected to local MQTT broker")

    # for processing control messages from the flask server
    local_mqtt_client.message_callback_add(ARD_HUMIDITY_ACTUATOR_TOPIC, change_water_pump_threshold(client=None, userdata=None, msg=None))

    #bridge between local and aws cloud mqtt
    local_mqtt_client.message_callback_add("sensors/#", foward_to_aws_mqtt(client=None, userdata=None, msg=None))

    global serial_data_queue
    serial_data_queue = queue.Queue()

    # Start the functions concurrently using threads
    mqtt_thread = threading.Thread(target=local_mqtt_t)
    read_data_thread = threading.Thread(target=read_data_t)

    mqtt_thread.daemon = True
    read_data_thread.daemon = True


    read_data_thread.start()
    mqtt_thread.start()
