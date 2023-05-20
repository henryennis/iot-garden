import time
from awscrt import mqtt, http
from awsiot import mqtt_connection_builder
import time
import logging as logging
from env_vars import AWS_IOT_ENDPOINT, AWS_IOT_CERT_PATH, AWS_IOT_PKEY_PATH, AWS_IOT_CA_PATH, AWS_IOT_CLIENT_ID


class AWSMQTTClient():
    def __init__(self) -> None:
        self.client = mqtt_connection_builder.mtls_from_path(
            endpoint=AWS_IOT_ENDPOINT,
            cert_filepath="C:\\dev\\iot-garden\\cloud\\auth\\bridgev2cert.pem",
            pri_key_filepath="C:\\dev\\iot-garden\\cloud\\auth\\bridgev2private.key",
            ca_filepath="C:\\dev\\iot-garden\\cloud\\auth\\aws_root_ca.pem",
            client_id=AWS_IOT_CLIENT_ID
        )

    def connect(self):
        try:
            connect_future = self.client.connect()
        # Future.result() waits until a result is available
            connect_future.result(5)
        except TimeoutError:
            logging.ERROR("Timed out connecting to AWS IoT.")
            return False
        else:
            logging.INFO("succesfful connect to AWS IoT.")
            return True