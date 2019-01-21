# Backend API

The backend API container is used to handle any non-customer facing operations. These operations can include posting readings to the database, and pulling data for system output on the display. 

## API endpoint
Get a token
```
/api/1.0/token
-- Function - POST
-- Payload {'username':'myusername','password':'mypass'}
-- Output {'duration':'3600','token':'TOKEN'}
```

### Code Ex
```python
r = requests.get('http://controller:7443/api/1.0/token', auth=requests.auth.HTTPBasicAuth('controller', 'rackbrain'))
out = r.raise_for_status()
if(out != None):
    raise Exception(out)

print 'Get the controller token'
token = json.loads(r.text)
print json.loads(r.text)
```

### CURL

curl -u controller:rackbrain -i -k http://controller-api:7443/api/1.0/token

## Development

### Build Run Remove

make.sh - build the container

run_container.sh - bring up a new controller-api container

stop_container.sh - stop the container and remove it

remove_image.sh - remove the Docker container image from the local image library

### Environment

See base-python27 image and Dockerfile in the tools directory.

See the requierments.txt for included libraries and versions.
