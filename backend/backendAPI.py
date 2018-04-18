#!/usr/bin/env python
#all of this needs to be chnaged use as an example and guide
import os
import sys
import random
import api_lib
import mongo_lib

from flask import  abort, request, jsonify, g, url_for
#from mongo_lib import Account as Account
#from mongo_lib import AccountSpecs as AccountSpecs
#from mongo_lib import Property as Property
#from mongo_lib import PropertySpecs as PropertySpecs
#from mongo_lib import UnitSpecs as UnitSpecs
#from mongo_lib import Rents as Rents

@mongo_lib.auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = Account.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = Account.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@mongo_lib.app.route('/api/token')
@mongo_lib.auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'duration': 3600})

@mongo_lib.app.route('/api/resource')
@mongo_lib.auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user})

###User Crud####
@mongo_lib.app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')
    params = {'username':username,'password':password,'role':role}
    return api_lib.create_user(params)

if __name__ == '__main__':
    mongo_lib.app.run(host='127.0.0.1',port=9443, debug=True,ssl_context='adhoc') 