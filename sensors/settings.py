import os
#Serial number of the Sensor, created at init time.
#CAUTION - Do not change this value sensor will cease funtioning
GPIO_PORT = os.getenv('GPIO_PORT',None)
#serial number of the sensor - created at init time
SENSOR_SERIAL = os.getenv('SENSOR_SERIAL','000000')
#collect a reading every 5 seconds
READING_INTERVAL = os.getenv('READING_INTERVAL','30')

#fahrenheit, celceious, pressure
#UNIT = os.getenv('READING_INTERVAL',None)

#backend username
BACKEND_USER=os.getenv('BACKEND_USER','backend')
#Password
BACKEND_PASS=os.getenv('BACKEND_USER','rackbrain')

API_VERSION=os.getenv('API_VERSION','1.0')