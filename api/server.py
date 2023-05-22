from flask import Flask, render_template, request
import paho.mqtt.client as paho_mqtt
from dotenv import load_dotenv
import os
import logging as logging
import threading as threading
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()
LOCAL_INTERFACE_IP = os.getenv("LOCAL_INTERFACE_IP")
ARD_HUMIDITY_ACTUATOR_TOPIC = os.getenv("ARD_HUMIDITY_ACTUATOR_TOPIC")
ARD_LIGHT_ACTUATOR_TOPIC = os.getenv("ARD_LIGHT_ACTUATOR_TOPIC")
ARD_TEMP_ACTUATOR_TOPIC = os.getenv("ARD_TEMP_ACTUATOR_TOPIC")



app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('group.html')


# Define a route to handle the form submission
@app.route('/tempapi', methods=['POST'])
def tempapi():
    temp = request.form.get('temp')
    local_mqtt_client.publish(ARD_TEMP_ACTUATOR_TOPIC, temp)
    return 'Values received: {}'.format(temp)


# Define a route to handle the form submission
@app.route('/lightapi', methods=['POST'])
def lightapi():
    light = request.form.get('light')
    local_mqtt_client.publish(ARD_LIGHT_ACTUATOR_TOPIC, light)
    return 'Values received: {}'.format(light)


# Define a route to handle the form submission
@app.route('/humidityapi', methods=['POST'])
def humidityapi():
    humidity = request.form.get('humidity')
    local_mqtt_client.publish(ARD_HUMIDITY_ACTUATOR_TOPIC, "humidity")
    return 'Values received: {}'.format(humidity)

def local_mqtt_t():
    while True:
        local_mqtt_client.loop(timeout=1.0, max_packets=1)

def main():

    mqtt_thread = threading.Thread(target=local_mqtt_t)
    global local_mqtt_client
    local_mqtt_client = paho_mqtt.Client("api")
    local_mqtt_client.on_connect = lambda client, userdata, flags, rc: logging.info(f"Connected to local MQTT broker with result code: {rc}")
    local_mqtt_client.connect(LOCAL_INTERFACE_IP, 1883)
    mqtt_thread.start()
    app.run(debug=False)
    #mqtt_thread.join()

main()