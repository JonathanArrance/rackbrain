#!/usr/bin/env python
#all of this needs to be chnaged use as an example and guide
import os
import sys
import random
import api_lib
import mongo_lib
import APIsettings as settings

from pymongo import MongoClient
from flask import  abort, request, jsonify, g, url_for

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

#curl -u backend:rackbrain -i -k -X GET http://192.168.1.56:9443/api/1.0/token
@mongo_lib.app.route('/api/'+api+'/token')
@mongo_lib.auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'duration': 3600})

@mongo_lib.app.route('/api/'+api+'/alive')
def get_alive():
    return jsonify({'data': 'Backend api is alive.'})

#curl -u token:x -i -k -X POST http://192.168.1.56:9443/api/1.0/reading
#-d '{'reading':'34','reading_type':'temp','sensor_serial':'434343434','reading_unit':'kelvin'}'
@mongo_lib.app.route('/api/'+api+'/reading', methods=['POST'])
#@mongo_lib.auth.login_required
def add_reading():
    #only the "backend" user can add readings, all other will be rejected
    #times should be a unix timestamp since it accounts for date and time
    reading_type = request.json.get('reading_type')
    reading = request.json.get('reading')
    sensor_serial = request.json.get('sensor_serial')
    reading_unit = request.json.get('reading_unit')
    params = {'reading_type':reading_type,'reading':reading,'sensor_serial':sensor_serial,'reading_unit':reading_unit}
    return api_lib.add_reading(params)

'''
@mongo_lib.app.route('/api/'+api+'/readings', methods=['GET'])
@mongo_lib.auth.login_required
def get_readings():
    #times should be a unix timestamp since it accounts for date and time
    start = request.json.get('starttime')
    end = request.json.get('endtime')
    sensorid = request.json.get('sensorid')
    params = {'start':start,'end':end,'sensorid':sensorid}
    return api_lib.get_readings(params)
'''
if __name__ == '__main__':
    #mongo_lib.app.run(host='0.0.0.0',port=9443, debug=True,ssl_context='adhoc')
    mongo_lib.app.run(host='0.0.0.0',port=9443, debug=True)