# Fronend API

The frontend API container is used to handle any customer, or outward facing operations. These operations can include adding a user or getting a set of readings.

## API endpoint
Get a token
```
/api/1.0/token 
-- Function - POST
-- Payload {'username':'myusername','password':'mypass'}
-- Output {'duration':'3600','token':'TOKEN'}
```

Create a user
```
/api/1.0/users
-- Function - POST
-- Payload {'username':'jon','password':'mypass','role':'admin'}
-- Output {'username':'jon','userid':'334455'}
```



### Code Ex
```python
r = requests.get('http://192.168.1.56:8443/api/1.0/token', auth=requests.auth.HTTPBasicAuth('jon', 'password'))
out = r.raise_for_status()
if(out != None):
    raise Exception(out)

print 'Get the login token'
token = json.loads(r.text)
print json.loads(r.text)
```

### CURL

curl -u jon:mypassword -i -k http://my_public_url:8443/api/1.0/token

## Development

### Build Run Remove

make.sh - build the container

run_container.sh - bring up a new frontend-api container

stop_container.sh - stop the container and remove it

remove_image.sh - remove the Docker container image from the local image library

### Environment

See base-python27 image and Dockerfile in the tools directory.

See the requierments.txt for included libraries and versions.
