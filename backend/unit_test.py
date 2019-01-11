import requests
import json
#login to backend
r = requests.get('http://192.168.1.56:9443/api/1.0/token', auth=requests.auth.HTTPBasicAuth('backend', 'rackbrain'))
out = r.raise_for_status()
if(out != None):
    raise Exception(out)

print 'Get the backend token'
token = json.loads(r.text)
print json.loads(r.text)

#send a reading
#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"paul","password":"python"}' -k https://192.168.10.9:8443/api/users
headers = {"content-type":"application/json;charset=UTF-8","X-Auth-Token":str(token['token'])}

print "Sending a new reading to the backend API"
data = "{'reading':'65','reading_type':'temp','sensor_serial':'67676767','reading_unit':'celcious'}"
r = requests.post('http://192.168.1.56:9443/api/1.0/reading', headers=headers, data=data)
out = r.raise_for_status()
if(out != None):
    raise Exception(out)

print 'Get the backend token'
print json.loads(r.text)
