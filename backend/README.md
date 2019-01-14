# Backend API

The backend API container is used to handle any non-customer facing operations. These operations can include posting readings to the database, and pulling data for system output on the display. 

# API endpoint

/api/1.0/token
-- Function - POST
-- Payload {'username':'myusername','password':'mypass'}

/api/1.0/reading - input readings into the backend DB
-- Function - POST
-- Payload {reading_type,reading_unit,sensor_serial}

## Ex

# CURL



## Development

### Build Run Remove

make.sh - build the container

run_container.sh - bring up a new backend-api container

stop_container.sh - stop the container and remove it

remove_image.sh - remove the Docker container image from the local image library

### Environment

See base-python2.7 image and Dockerfile in the tools directory.

See the requierments.txt for included libraries and versions.
