# Backend API

The backend API container is used to handle any non-customer facing operations. These operations can include posting readings to the database, and pulling data for system output on the display. 

## API endpoint

/api/1.0/token </br>
-- Function - POST </br>
-- Payload {'username':'myusername','password':'mypass'} </br>
-- Output {'duration':'3600','token':'TOKEN'} </br>

/api/1.0/reading - input readings into the backend DB </br>
-- Function - POST </br>
-- Payload {'reading':'46','reading_type':'temp','reading_unit':'celcious','sensor_serial':'990088'} </br>
-- Output 'OK' </br>

### Code Ex

r = requests.get('http://192.168.1.56:9443/api/1.0/token', auth=requests.auth.HTTPBasicAuth('backend', 'rackbrain'))
out = r.raise_for_status()
if(out != None):
    raise Exception(out)

print 'Get the backend token'
token = json.loads(r.text)
print json.loads(r.text)


### CURL

curl -u backend:rackbrain -i -k http://backend-api:9443/api/1.0/token



## Development

### Build Run Remove

make.sh - build the container

run_container.sh - bring up a new backend-api container

stop_container.sh - stop the container and remove it

remove_image.sh - remove the Docker container image from the local image library

### Environment

See base-python2.7 image and Dockerfile in the tools directory.

See the requierments.txt for included libraries and versions.
