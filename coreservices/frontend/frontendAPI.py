#!/usr/bin/env python
import os
import sys
import random
import api_lib
import mongo_lib
import APIsettings as settings

from pymongo import MongoClient
from flask import  abort, request, jsonify, g, url_for

#api version
api = settings.API_VERSION

@mongo_lib.auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = mongo_lib.Account.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = mongo_lib.Account.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@mongo_lib.app.route('/api/'+api+'/token')
@mongo_lib.auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'duration': 3600})

@mongo_lib.app.route('/api/'+api+'/resource')
@mongo_lib.auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user})

@mongo_lib.app.route('/api/'+api+'/alive')
def get_alive():
    return jsonify({'data': 'Rackbrain is alive.'})

###User Crud####
@mongo_lib.app.route('/api/'+api+'/users', methods=['POST'])
def new_user():
    req_data = request.get_json()
    params = {'username':req_data['username'],'password':req_data['password'],'role':req_data['role']}
    return api_lib.create_user(params)

@mongo_lib.app.route('/api/'+api+'/users/<int:user_id>',methods=['GET'])
@mongo_lib.auth.login_required
def get_user(user_id):
    print user_id
    return api_lib.get_user(user_id)

@mongo_lib.app.route('/api/'+api+'/users', methods=['GET'])
@mongo_lib.auth.login_required
def get_users():
    #params = request.json.get(params)
    return api_lib.list_users()

@mongo_lib.app.route('/api/'+api+'/users/<int:user_id>', methods=['DELETE'])
@mongo_lib.auth.login_required
def delete_user(user_id):
    return api_lib.delete_user(user_id)

@mongo_lib.app.route('/api/'+api+'/users/<int:user_id>', methods=['POST'])
@mongo_lib.auth.login_required
def update_user(user_id):
    return api_lib.update_user(user_id)

###SensorCatalog######
@mongo_lib.app.route('/api/'+api+'/sensorcatalog', methods=['GET'])
@mongo_lib.auth.login_required
def get_sensor_catalog():
    #list the sensors available to the rackbrain system
    return api_lib.get_sensor_catalog()

####Sensor Info########
@mongo_lib.app.route('/api/'+api+'/sensor', methods=['GET'])
@mongo_lib.auth.login_required
def get_sensors():
    return api_lib.get_sensors()

@mongo_lib.app.route('/api/'+api+'/sensor/<int:sensor_id>', methods=['GET'])
@mongo_lib.auth.login_required
def get_sensor(sensor_id):
    return api_lib.get_sensor(sensor_id)

@mongo_lib.app.route('/api/'+api+'/sensor', methods=['POST'])
@mongo_lib.auth.login_required
def add_sensor(sensor_id):
    return api_lib.add_sensor(sensor_id)

@mongo_lib.app.route('/api/'+api+'/sensor/<int:sensor_id>', methods=['DELETE'])
@mongo_lib.auth.login_required
def remove_sensor(sensor_id):
    return api_lib.remove_sensor(sensor_id)



####Devices#########
@mongo_lib.app.route('/api/'+api+'/device', methods=['GET'])
@mongo_lib.auth.login_required
def get_devices():
    return api_lib.get_devices()

@mongo_lib.app.route('/api/'+api+'/device/<int:device_id>', methods=['GET'])
@mongo_lib.auth.login_required
def get_device(device_id):
    return api_lib.get_device(device_id)

@mongo_lib.app.route('/api/'+api+'/device', methods=['POST'])
@mongo_lib.auth.login_required
def add_device(device_id):
    return api_lib.add_device(device_id)

@mongo_lib.app.route('/api/'+api+'/device/<int:device_id>', methods=['DELETE'])
@mongo_lib.auth.login_required
def remove_device(device_id):
    return api_lib.remove_device(device_id)

if __name__ == '__main__':
    mongo_lib.app.run(host='0.0.0.0',port=8443, debug=True,ssl_context='adhoc')
    #mongo_lib.app.run(host='0.0.0.0',port=8443, debug=True)