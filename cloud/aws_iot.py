import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from env_vars import ENDPOINT, ROOT_CA, DEVICE_PRIVATE_KEY, DEVICE_CERT

class AWSIoTClient:
    def __init__(self):
        self.client = AWSIoTMQTTClient("my-device")
        self.client.configureEndpoint(ENDPOINT, 8883)
        self.client.configureCredentials(ROOT_CA, DEVICE_PRIVATE_KEY, DEVICE_CERT)
        self.configure_connection_settings()

    def configure_connection_settings(self):
        self.client.configureAutoReconnectBackoffTime(1, 32, 20)
        self.client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.client.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.client.configureConnectDisconnectTimeout(10)  # 10 sec
        self.client.configureMQTTOperationTimeout(5)  # 5 sec

    def connect(self):
        self.client.connect()
        print("Connected to AWS IoT Core")

    ## Callback function for AWS IoT Core
    def on_message(self, client, userdata, message):
        print("Received message:", message.payload.decode("utf-8"), "from topic:", message.topic)

    def subscribe(self, topic, qos):
        self.client.subscribe(topic, qos, self.on_message)

    def publish(self, topic, message, qos):
        self.client.publish(topic, message, qos)

    def run(self):
        self.connect()
        self.subscribe("example/topic", 1)
        self.publish("example/topic", "Hello from the Python SDK", 1)

        while True:
            time.sleep(1)

"""
if __name__ == "__main__":
    aws_iot_client = AWSIoTClient()
    aws_iot_client.run()
"""