import paho.mqtt.client as mqtt
import os
from time import sleep

# IP address or the MQTT Broker
broker_address = os.environ['MQTT_BROKER_ADDRESS']

# An MQTT topic can be anything as a string,
# Like for a temprature reading you can use 'temperature' as topic
# Or for Living Room temperature reading you can use 'temperature_living_room'
topic = "test_topic"

# Message to be Published
message = "Hi Pico! This is Pi here!"

# This function gets called when we try to connect to MQTT Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Connection Successful
        print("Successfully Connected!\n")

        # Publish the message
        client.publish(topic, message)

    else:
        print('Not Able to connect!')
        client.loop_stop()

# Create new instance of the MQTT client
# Any name can be used here - But each client should have a unique name
client = mqtt.Client("Test-MQTT-Client-Pub")

# Set user name and password if MQTT client is set-up with one
# Else following line of code is not required

# client.username_pw_set(user_name, password)

# Connect to the client
client.connect(broker_address)
# Assign callback function
client.on_connect = on_connect

# Calling this is important to keep the connection alive with the broker
client.loop_start()

sleep(1)