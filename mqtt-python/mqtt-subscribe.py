import paho.mqtt.client as mqtt
import os

# This function gets called when we try to connect to MQTT Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Connection Successful
        print("Successfully Connected!\n")
        # At this point we can subscribe to the topics
        # Subscribe to the MQTT topic
        client.subscribe("test_topic")
        client.subscribe("test_topic_2")
    else:
        print('Not Able to connect!')
        client.loop_stop()

def on_message(client, userdata, message):
    print(message.topic)
    print(message.payload.decode("utf-8"))

# IP address for the MQTT Broker
broker_address = os.environ['MQTT_BROKER_ADDRESS']

# Create new instance of the MQTT client
# Any name can be used here - But each client should have a unique name
client = mqtt.Client("Test-MQTT-Client-Sub")

# Set user name and password if MQTT client is set-up with one
# Else following line of code is not required

# client.username_pw_set(user_name, password)

# Define on_message function, this gets called when we receive a message
client.on_message = on_message
client.on_connect = on_connect

# Connect to the client
client.connect(broker_address)

# Calling this is important to keep the connection alive with the broker
# As this is loop forever it blocks the program and keeps listening to incoming messages.
client.loop_forever()