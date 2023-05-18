import paho.mqtt.client as mqtt
import logging as logging

class MyMQTTClient(mqtt.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Additional initialization code for your subclass

        # Set up callback functions
        self.on_connect = self.my_on_connect
        self.on_message = self.my_on_message

    def my_on_connect(self, client, userdata, flags, rc):
        # Custom on_connect callback logic
        print("Connected with result code " + str(rc))


    def my_on_message(self, client, userdata, msg):
        # Custom on_message callback logic
        print("Message received on topic: " + msg.topic)
        print("Message payload: " + msg.payload.decode())

