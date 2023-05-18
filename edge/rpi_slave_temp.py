from local_mqtt import paho_mqtt
import threading as threading
import queue as queue
import logging as logging

def mqtt():
    client = paho_mqtt.MyMQTTClient()
    client.connect("localhost", 1883)
    client.loop_start()
    while True:
        if not data_queue.empty():
            data = data_queue.get()
            client.publish("ecg", data)


def read_data_t():
    try:
        while True:
            data = read_serial()
            data_queue.put_nowait([data.timestamp, data.value])
            db.write(data)
    except KeyboardInterrupt:
        logging.info("Exiting... ")



if __name__ == "__main__":


    #global makes the variable accessible to all scopes
    global data_queue
    data_queue = queue.Queue()

    # Start the functions concurrently using threads
    mqtt_thread = threading.Thread(target=mqtt)
    read_data_thread = threading.Thread(target=read_data_t, args=(data_queue))

    mqtt_thread.daemon = True
    read_data_thread.daemon = True


    read_data_thread.start()
    mqtt_thread.start()
