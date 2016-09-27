# MQTT_Test
Simple Python test of MQTT

To build Python containers:
- docker build -t publish-python -f Dockerfile-pub
- docker build -t subscribe-python -f Dockerfile-sub

To run containers (Run each of these commands in separate shells, Ctrl-C to exit)
- docker run -it --rm --name publisher publish-python
- docker run -it --rm --name subscriber subscribe-python

Known limitations:
- subscribe-python writes to rpi_sensor_out.txt into the container, not in the host OS directory (or elsewhere)
- publish-python writes to rpi_sensor.txt into the container, not in the host OS directory (or elsewhere)

To-Do List
- Update readTemp() and readHumidity() to read from Raspberry Pi DHT-11 sensor
- Fix output .txt file writing
- Look into using MQTT to detect/add new sensor clients (send in "hello" message)
- Update output CSV to add client identifier column
