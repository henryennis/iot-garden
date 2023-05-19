import paho.mqtt.client as mqtt
import logging as logging

class MyMQTTClient(mqtt.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Additional initialization code for your subclass

        # Set up callback functions
        self.on_connect = None
        self.on_message = None


