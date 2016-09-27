#!/usr/bin/python

# subscribe.py - test subscribe script for MQTT

import sys
import time
import paho.mqtt.client as mqtt
from xmlrpclib import datetime
import signal
import random

###################################################################
# Subroutines                                                     #
###################################################################

def signal_handler(signal, frame):
    # Cleanup
    # close output file
    print "\nClosing output file"
    fOutput.close()

    # Disconnect MQTT
    print "Disconnecting MQTT"
    client.disconnect()

    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Initialize Variables 
txtCurrentAction = "Subscribe: Initializing variables..."
print txtCurrentAction
txtOutputFile = "rpi_sensor_out.txt"
print "- Output file: " + txtOutputFile
txtMQTTServer = "iot.eclipse.org"
nMQTTport = 1883
print "- MQTT Server: " + txtMQTTServer +":" + str(nMQTTport)
txtMQTTTopic = "jmaaks/test"
print "- MQTT Topic: " + txtMQTTTopic
print "\n"

# Initialize files
fOutput = open(txtOutputFile, 'at')

# Initialize MQTT Connection
client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message
def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
    fOutput.write(str(message.payload) + "\n")

client.on_message = on_message

client.connect(txtMQTTServer, nMQTTport, 60) # keepalive=60
client.subscribe(txtMQTTTopic, 2)
print "Waiting for MQTT messages...Ctrl-C to exit."
client.loop_forever()


