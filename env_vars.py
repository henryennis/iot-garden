AWS_AUTH_PATH = "./auth"


AWS_IOT_ENDPOINT="a2t49keckhjlsm-ats.iot.ap-southeast-2.amazonaws.com",
AWS_IOT_CERT_PATH=f"{AWS_AUTH_PATH}/bridgev2.cert.pem"
AWS_IOT_PKEY_PATH=f"{AWS_AUTH_PATH}/bridgev2.private.key",
AWS_IOT_CA_PATH=f"{AWS_AUTH_PATH}/aws_root_ca.pem"
#thing name
AWS_IOT_CLIENT_ID="bridgev2",



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