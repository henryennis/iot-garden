MQTT_KEEP_ALIVE_SECONDS = 10
ENDPOINT = "your-aws-iot-endpoint.amazonaws.com"
ROOT_CA = "root-CA.crt"
DEVICE_CERT = "your-device.cert.pem"
DEVICE_PRIVATE_KEY = "your-device.private.key"

RPI_SLAVE_IP = ""
RPI_SLAVE2_IP = ""


ARD_HUMIDITY_SENSOR_TOPIC = "sensors/humidity"
ARD_HUMIDITY_ACTUATOR_TOPIC = "actuators/water-pump"

ARD_LIGHT_SENSOR_TOPIC  = "sensors/light"
ARD_LIGHT_ACTUATOR_TOPIC  = "actuators/light"

ARD_TEMP_SENSOR_TOPIC = "sensors/temperature"
ARD_TEMP_ACTUATOR_TOPIC = "actuators/fan"

ARD_HUMIDITY_PORT = "/dev/ttyACM0"
ARD_LIGHT_PORT = "/dev/ttyACM0"
ARD_TEMP_PORT = "/dev/ttyACM0"
SERIAL_BAUD_RATE = 9600