# Rackbrain rack intellegence platform. - NOT COMPLETE
Used to monitor the status of an AV or IT rack.

## Environment.
1. OS - Raspian Stretch (9.4) - https://www.raspberrypi.org/downloads/raspbian/
2. Docker - Docker version 18.04.0-ce
3. Dev Language - Python 2.7.13
4. Mongo - Mongo 3.0.4 (32bit mongo, 2gb Data limit)

## Hardware.
Raspberry Pi 3 B or B+
NOTE: This software may work on other pi versions, but has not been tested.
DHT-11 temp sensors.

## Alternate environment
Raspian Desktop - https://www.raspberrypi.org/downloads/raspberry-pi-desktop/
NOTE: This software is not tested on this platform, but should work.

# Setup a dev environment.
1. Install Raspian Stretch and enable SSH.
2. Run ~/rackbrain/tools/setup_dev_env.sh.
3. Ensure all of the base images have been created and that the rpi-mongo container is running.

## Run the Unittests
1. cd unittests
2. python 'unittestfile'

## Tools used
1. Robot 3T - Mongo interface
2. Komodo IDE

## Build, Run, Rebuild the containers
1. Build the container from docker file - make.sh
2. Run the contianer - run_container.sh
3. Stop and remove from images repo - stop_container.sh

# API Examples
Create new user account
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"paul","password":"python","role":"admin"}' -k https://192.168.10.9:8443/api/users

Get a new token
curl -u paul:python -i -k -X GET https://192.168.10.9:8443/api/token

Use the token to talk to endpoint
curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxOTE0NzExNSwiaWF0IjoxNTE5MTQzNTE1fQ.eyJ1c2VyaWQiOjgzNTQ1NjMyODExNzAxMzgwMzV9.BX0xOSSDLmFiBzANy5pMCYfxkB4edgao3O4IK8akO4c:x -i -k -X GET https://192.168.10.9:8443/api/users

# TODO
