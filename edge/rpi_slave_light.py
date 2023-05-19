from local_mqtt import paho_mqtt
import threading as threading
import queue as queue
import logging as logging

import time as time
from serial import Serial
from env_vars import SERIAL_BAUD_RATE, SERIAL_PORT1



def local_mqtt_t():
    while True:
        if not serial_data_queue.empty():
            data = serial_data_queue.get()
            local_mqtt_client.publish("sensors/ardunio2/light", data)
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

def trigger_motor(client, userdata, msg):
    serial.write((msg.payload).encode())



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    #global makes the variable accessible to all scopes
    global serial
    serial = Serial(SERIAL_PORT1, SERIAL_BAUD_RATE)
    time.sleep(2)


    global local_mqtt_client
    local_mqtt_client = paho_mqtt.MyMQTTClient()
    local_mqtt_client.connect("localhost", 1883)
    local_mqtt_client.subscribe("actuators/ardunio2/light", 1)
    local_mqtt_client.on_connect = lambda client, userdata, flags, rc: print("Connected to local MQTT broker")
    local_mqtt_client.message_callback_add("actuators/ardunio2/light", trigger_motor(client=None, userdata=None, msg=None))
    

    global serial_data_queue
    serial_data_queue = queue.Queue()

    # Start the functions concurrently using threads
    mqtt_thread = threading.Thread(target=local_mqtt_t)
    read_data_thread = threading.Thread(target=read_data_t)

    mqtt_thread.daemon = True
    read_data_thread.daemon = True


    read_data_thread.start()
    mqtt_thread.start()
