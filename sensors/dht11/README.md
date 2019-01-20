# DHT 11 Temperature Probe 
The DHT 11 temprature probe is a general purpose probe that can be connected to the GPIO port on a Raspbeery PI. The probe will record temprature and humidity on a 2 second basis. The Rackbrain defualut config will gather data from the DHT 11 every 30 seconds. 

## Functions
```
**send_reading** - Send a reading to the 

## Build
Use the dht11 sensor as an example when building out other sensor libraries. 

### Tools
DHT11 sensor
basic bread board
functioning base Rackbrain

### Example Docker file
```
FROM base-sensors
ENV INSTALL_PATH /opt/sensor
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY dht11.py $INSTALL_PATH
```
