#!/usr/bin/python

# main.py - test publish script for MQTT

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

def readTemp():
    numTemp = round(random.randint(-10,98) + random.random(), 2)
    return numTemp;

def readHumidity():
    numHumidity = round(random.random(), 4)
    return numHumidity


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Initialize Variables 
txtCurrentAction = "Publish: Initializing variables..."
print txtCurrentAction
txtOutputFile = "rpi_sensor.txt"
print "- Output file: " + txtOutputFile
nSleepSecs = 10
print "- Sleep time: " + str(nSleepSecs)
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

client.connect(txtMQTTServer, nMQTTport, 60) # keepalive=60


# Initialize temp / humidity sensor by reading it once
readTemp()


while True:
    # Read temperature
    nTemp = readTemp()

    # Read humidity
    nHumidity = readHumidity()

    # Read current date/time and build output text
    strOutput = str(datetime.datetime.now())
    strOutput += "," + str(nTemp) + "," + str(nHumidity)

    # Write line to output file
    print "Output: " + strOutput
    fOutput.write(strOutput + "\n")

    # Write line to MQTT
    client.publish(txtMQTTTopic, strOutput)

    print "Sleeping for " + str(nSleepSecs) + " seconds (Ctrl-C to exit)"
    time.sleep (nSleepSecs)

