# Sensor Base

The base image used to build out all of the sensors that are attached to the Rackbrain framework.

sensor_lib.py is coped to the /opt/sensor directory.

Any new sensor builds should have the WORKINGDIR /opt/sensor set in their Dockerfile. Doing so will enable any sensor specific code to use sensor_lib auto-magically through the power of the Docker image build process.

## Sensor Lib

sensor_lib.py is used to communicate with the backend API. The backend API is a general purpose set of API entry points into the database and any backend services needed for sensors, devices, functions, or displays.

NOTE: The backend API service is internal faceing to the Rackbrain system only.

### Functions
```
**get_backend_token** - get a login token based on the backend service credentials. The default credentials are backend/rackbrain, but can be changed during build time to something different.

Input - None

Output - dictionary
    token - auth token
    duration - token duration - default 3600 seconds

```
```
**send_reading** - send a reading to the backend API and the ultimately to to the backend database.

Input - dictionary
    reading - the measured reding from the sensor
    reading_type - the unit the reading is measured in - ['temp','humidity','power','pressure'].
    reading_unit - the units the reading is measured in
    sensor_serial - the unique serial number for the sensor

Output - 'OK'
```
```
**get_sensor** - Get the info for a sensor
Input - sensor_serial
Output - dictionary
   sensor_name
   last_readings - dictionary of last 20 readings.
```
## Example

If the following is used in your Dockerfile then the custom sensor code will be able to use the sensor lib.
```
FROM base-sensor

ENV INSTALLPATH /opt/sensor

WORKINGDIR $INSTALLPATH

COPY mysensor.py $INSTALLPATH
```
