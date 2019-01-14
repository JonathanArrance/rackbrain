# Backend API

The backend API container is used to handle any non-customer facing operations. These operations can include posting readings to the database, and pulling data for system output on the display. 

## Development

### Build Run Remove

make.sh - build the container

run_container.sh - bring up a new backend-api container

stop_container.sh - stop the container and remove it

remove_image.sh - remove the Docker container image from the local image library

### Environment

See base 

# API endpoint

/api/1.0/reading - input readings into the backend DB
-- Function - POST
-- Variables - reading - The reading value from the sensor.
			 - reading_type - The type of reading - temp,pressure,power,humidity
			 - reading_unit - The measurement unit. Ex. Celsius
			 - sensor_serial - The unique serial number for the sensor.

## Ex.

