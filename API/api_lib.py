from flask import  jsonify,abort
from mongo_lib import Account as Account
from mongo_lib import AccountSpecs as AccountSpecs
from mongo_lib import Sensor as Sensor
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

    user_out = jsonify({'username':user.username,'role':user.role,'userid':user.userid,'firstname':user_spec.firstname,
                                'lastname':user_spec.lastname,'email':user_spec.email})

    return user_out

def get_users(params=None):
    #Return a list of users based on the role given. If no role given all roles returned except internal roles.
    #if the role is not given and the role of the user makeing the call is internal return all
    return "get users test"

def update_user(input_dict):
    #Update the variables in the input dict
    #input: dict - username
    #                - role
    #                - userid
    #                - firstname
    #                - lastname
    #               - email
    #output: dict - username
    #                 - role
    #                 - firstname
    #                 - lastname
    #                 - email
    #error:  400 invalid value
    #          404no user found
    if Account.query.filter_by(userid=params['userid']).first() is None:
        abort(404)   # no user found

    #check if update values are acceptable
    values = ['username','role','firstname','lastname','email','userid']
    for k in input_dict.keys:
        if k not in values:
            abort(400)

def delete_user(user_id):
    pass

#Sensor API workers
def insert_sensor(input_dict):
    pass

def delete_sensor(sensor_id):
    pass

def get_sensors():
    pass

def get_sensor(sensor_id):
    pass


#Attached devices
def get_devices():
    pass

def get_device(device_id):
    pass

def delete_device(device_id):
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
