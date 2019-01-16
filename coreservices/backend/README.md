# The backend API container is used to post readings to the DB from the various sensors connected to the device. 

# Development

## Build

## Run

## Remove

# API endpoint

/api/1.0/reading - input readings into the backend DB
-- Function - POST
-- Variables - reading - The reading value from the sensor.
			 - reading_type - The type of reading - temp,pressure,power,humidity
			 - reading_unit - The measurement unit. Ex. Celsius
			 - sensor_serial - The unique serial number for the sensor.

## Ex.

