#!/bin/python
import random
import sys
import time
#import tools_lib as tools
import re

#settings file
import APIsettings as settings

from flask import Flask, abort, request, jsonify, g, url_for
from flask_mongoalchemy import MongoAlchemy
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
#app.config['MONGOALCHEMY_DATABASE'] = 'tatter'
app.config['MONGOALCHEMY_DATABASE'] = settings.MONGO_DBNAME
#app.config['MONGOALCHEMY_SERVER'] = '192.168.10.34'
app.config['MONGOALCHEMY_SERVER'] = settings.MONGO_HOST
#app.config['MONGOALCHEMY_PORT'] = 27017
app.config['MONGOALCHEMY_PORT'] = settings.MONGO_PORT

#app.config['MONGO_HOST'] = '192.168.10.34'
#app.config['MONGO_PORT'] = 27017
#app.config['MONGO_DBNAME'] = 'tatter'
#app.config['API_VER'] = '1.0'

app.config['MONGO_HOST'] = settings.MONGO_HOST
app.config['MONGO_PORT'] = settings.MONGO_PORT
app.config['MONGO_DBNAME'] = settings.MONGO_DBNAME
app.config['API_VER'] = settings.API_VERSION
app.config['MONGO_URI'] = settings.MONGO_URI


db = MongoAlchemy(app)
auth = HTTPBasicAuth()
mongo = PyMongo(app)

class Account(db.Document):
    username = db.StringField()
    password_hash = db.StringField()
    userid = db.AnythingField()
    role = db.StringField()

    def gen_id(self):
        key_num = random.SystemRandom()
        self.userid = key_num.randint(0, sys.maxsize)
        return self.userid

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'userid': self.userid})

    def add_role(self,r):
        role_list = ['user', 'admin', 'support','system']
        if(r in role_list):
            self.role = r

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired as e:
            return None    # valid token, but expired
        except BadSignature as f:
            return None   # invalid token
        user = mongo.db.Account.find_one({'userid':data['userid']})
        return user['userid']

class Reading(db.Document):
    reading = db.StringField()
    readingid = db.AnythingField()
    readingtime = db.AnythingField()
    readingtype = db.StringField()
    readingunit = db.StringField()
    sensor_serial = db.AnythingField()

    def readingid(self):
        key_num = random.SystemRandom()
        self.readingid = key_num.randint(0, sys.maxsize)
        return self.readingid

    def readingtime(self):
        self.readingtime = time.time()
        return self.readingtime

    def readingtype(self,readingtype):
        values = ['temp','humidity','power','pressure']
        if str(readingtype).lower() not in values:
            abort(404)
        self.readingtype = readingtype

    def readingunit(self,readingunit):
        self.readingunit = readingunit

    def sensor_serial(self,sensor_serial):
        self.sensor_serial = sensor_serial

class RackBrainSys(db.Document):
    rackid = db.AnythingField()
    manufacture_date = db.AnythingField()
    location = db.StringField()
    setup_date = db.AnythingField()
    version = db.StringField()

    def location(self,location):
        self.location = location

    def version(self,version):
        self.version = version

    def setup_date(self,date):
        self.date = date
