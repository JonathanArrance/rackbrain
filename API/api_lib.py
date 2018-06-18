from flask import  jsonify,abort
from mongo_lib import Account as Account
from mongo_lib import AccountSpecs as AccountSpecs
from mongo_lib import SensorInventory
from mongo_lib import SensorCatalog as SensorCatalog
from mongo_lib import Reading as Reading
from mongo_lib import AttachedDevice as Device

def create_user(params=None):
    #Create a new user based on the params given
    #input: Params dict
    #output: 201 on successful add
    #error: 400 no user found
    #          409 duplicate user
    if params is None:
        abort(400)
    if params['username'] is None or params['password'] is None or params['role'] is None:
        abort(400)    # missing arguments
    if Account.query.filter_by(username=params['username']).first() is not None:
        abort(409)   # existing user
    user = Account(username=params['username'])
    user.hash_password(params['password'])
    userid = user.gen_id()
    user.add_role(params['role'])
    user.save()

    specs = AccountSpecs(userid=userid)
    specs.fname('None')
    specs.lname('None')
    specs.phone('None')
    specs.email('None')
    specs.social('None')
    specs.save()

    return (jsonify({'username': user.username,'userid':userid}), 201)

def get_user(userid):
    #Return the user based on the userid
    #input: userid
    #output: dict - username
    #                 - role
    #                 - userid
    #error: 400 no user found
    if Account.query.filter_by(userid=params['userid']).first() is None:
        abort(400)   # no user found

    user = Account.query.filter_by(userid=userid).first()
    user_spec = AccountSpecs.query.filter_by(userid=userid).first()

    return (jsonify({'username':user.username,'role':user.role,'userid':user.userid,'firstname':user_spec.firstname,
                                'lastname':user_spec.lastname,'email':user_spec.email}),201)

def update_user(input_dict):
    #Update the variables in the input dict
    #error:  400 invalid value
    #          404 no user found
    if Account.query.filter_by(userid=params['userid']).first() is None:
        abort(404)   # no user found

    #check if update values are acceptable
    #values = ['username','role','firstname','lastname','email','userid']
    #for k in input_dict.keys:
    #   if k not in values:
    #        abort(400)
    return ('Not implemented',201)

def list_users():
    #Return a list of users based on the role given. If no role given all roles returned except internal roles.
    #if the role is not given and the role of the user makeing the call is internal return all
    return ('Not implemented',201)

def delete_user(userid=None):
    pass
    #return ('Not implemented',201)

#Sensor API workers
#Used to get info from the db in regards to the sensors attached to the rackbrain
def create_sensor(params=None):
    #400 if invalid sensortype is given
    sc = SensorCatalog.sensorinfo()
    if params is None:
        abort(400)
    if params['sensorname'] is None or params['sensortype'] is None:
        abort(400)    # missing arguments
    if SensorInventory.query.filter_by(sensorname=params['sensorname']).first() is not None:
        abort(409)   # existing sensor
    if SensorCatalog.query.filter_by(sensortype=params['sensortype']).first() is None:
        abort(409)   # sensor type is not in the catalog

    sensor = SensorInventory(sensorname=params['sensorname'])
    sensorid = sensor.gen_id()
    sensor.sensortype(params['sensortype'])
    sensor.sensordesc(params['sensordesc'])
    sensor.save()
    return (jsonify({'sensorname': sensor.sensorname,'sensorid':sensorid}), 201)

def get_sensors():
    return ("Not implemented",201)

def get_sensor(sensorid=None):
    if(sensorid is None):
        abort(400)
    sensor = SensorInventory.query.filter_by(sensorid=sensorid).first()
    return (jsonify({'sensorname':sensor.sensorname,'sensorid':sensor.sensorid,'sensortype':sensor.sensortype,'sensordesc':sensor.sensordesc}),201)

def delete_sensor(sensorid=None):
    if(sensorid is None):
        abort(400)
    sensor = SensorInventroy(sensorid=sensorid)
    sensor.remove()
    
    

#Attached devices
#Devices can be fans, LCD screens, power outlets, etc.
def list_devices():
    devices = Device.query()
    return devices

def get_device(deviceid):
    if(deviceid is None):
        abort(400)
    device = Device.query.filter_by(deviceid=deviceid).first()
    return (jsonify({'sensorname':sensor.sensorname,'sensorid':sensor.sensorid,'sensortype':sensor.sensortype,
                          'sensordesc':sensor.sensordesc}),201)


def delete_device(deviceid):
    pass

def add_device(input_dict):
    pass

#Backend Only workers
#Reading API workers
def get_readings(input_dict):
    #sensorID, date/time(timestamp),daterange(min timestamp, max timestamp)
    pass

def get_all_readings(sensorid):
    pass

def insert_reading(input_dict):
    pass

#location API workers
def insert_location(input_dict):
    pass

def update_location(input_dict):
    pass
