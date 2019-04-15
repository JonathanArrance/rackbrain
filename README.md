# Rackbrain rack intellegence platform. - NOT COMPLETE
IoT device used to monitor the status of AV or IT rack. Moreover Rackbrain can be used as a framework for new IoT projects based on the RPI platform. The code can be adjusted to work on other platforms, and can have functionality easily added to the by adding new containers.

## Environment.
1. OS - Raspian Stretch (9.4) - https://www.raspberrypi.org/downloads/raspbian/
2. Docker - Docker version 18.06.0-ce
3. Dev Language - Python 2.7.13 with support for 3.5
4. Mongo - Mongo 3.0.4 (32bit mongo, 2gb Data limit)
5.

## Things Board
MQTT integration with Things Board - Todo
1. Integrate paho-mqtt python lib

## Hardware.
Raspberry Pi 3 B or B+
NOTE: This software may work on other pi versions, but has not been tested.
DHT-11 temp sensors throught GPIO.
SSD1306 OLED mini display through GPIO

## Alternate environment
Raspian Desktop - https://www.raspberrypi.org/downloads/raspberry-pi-desktop/
NOTE: This software is not tested on this platform, but should work. Connnection of the input output devices is through GPIO.

# Development Environment

## Setup a dev environment.
1. Install Raspian Stretch 9.4 and enable SSH.
2. Run setup_dev_env.sh.
3. Ensure all of the base images have been created and that the rpi-mongo container is running.

```
docker images
```

## Run the Unittests
1. cd into unit test directory
2. python 'unit test file'

## Tools used
1. Robot 3T - Mongo interface
2. Komodo IDE
3. RaspBerry PI 3 B
4. DHT 11 Temp and pressure sensor
5. SSD 1306 OLED
6. Standard bread board

## Build, Run, Rebuild the containers
1. Build the container from docker file in each directory - make.sh
2. Run the contianer - run_container.sh
3. Stop the container and remove from images repo - stop_container.sh


# API Examples

## Front End API

### Create new user account
```
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"paul","password":"python","role":"admin"}' -k https://192.168.10.9:8443/api/1.0/users
```
### Get a new token
```
curl -u paul:python -i -k -X GET https://192.168.10.9:8443/api/1.0/token
```
### Use the token to talk to endpoint
```
curl -u TOKEN:x -i -k -X GET https://192.168.10.9:8443/api/1.0/users
```
## Backend API

In order to use the backend API login to the back end service with the default account or the account that is set at build time.

### Login to backend
```
curl -u backend:rackbrain -i -X GET http://backend_api:9443/api/1.0/token
```
### Post a new reading
```
curl -u TOKEN:x -i -X POST http://backend_api/api/1.0/reading
```
## System Config API
