import unittest
from cloud.aws_mqtt_client import AWSMQTTClient


class TestAWSMQTTClient(unittest.TestCase):

    def test_client_connect(self):
        client = AWSMQTTClient()
        result = client.connect()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()