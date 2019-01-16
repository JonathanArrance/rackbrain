#!/bin/python
import random
import sys
import datetime
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
app.config['MONGOALCHEMY_DATABASE'] = settings.MONGO_DBNAME
app.config['MONGOALCHEMY_SERVER'] = settings.MONGO_HOST
app.config['MONGOALCHEMY_PORT'] = settings.MONGO_PORT

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

class AccountSpecs(db.Document):
    userid = db.AnythingField()
    firstname = db.StringField()
    lastname = db.StringField()
    email = db.StringField()

class SensorCatalog(db.Document):
    #Catalog of supported sensors, updated from time to time
    sensortype = db.StringField()
    sensorname = db.StringField()
    sensorid = db.AnythingField()
    sensordesc = db.StringField()

    def sensortype(self,sensortype):
        sensor_types = ['temp','photo','power','pressure']
        if(str(sensortype).lower in sensor_types):
            self.sensortype = sensortype

class SensorInventory(db.Document):
    #Inventory of sensors attached to the rackbrain 
    sensor_type = db.StringField()
    sensor_name = db.StringField()
    #sensorid = db.AnythingField()
    sensor_desc = db.StringField()
    sensor_serial = db.AnythingField()
    
    #def sensorserial(self):
    #    key_num = random.SystemRandom()
    #    self.sensorserial = key_num.randint(0, sys.maxsize)
    #    return self.sensorserial
    
    def sensor_serial(self,sensor_serial):
        self.sensor_serial = sensor_serial

    def sensor_type(self,sensor_type):
        self.sensortype = sensor_type

    def sensor_name(self,sensor_name):
        self.sensor_name = sensor_name
    
    #def sensorid(self,sensorid):
    #    self.sensorid = sensorid

    def sensor_desc(self,sensor_desc):
        self.sensor_desc = sensor_desc

class Reading(db.Document):
    readingid = db.AnythingField()
    readingtime = db.AnythingField()
    reading = db.StringField()
    readingtype = db.StringField()
    sensorserial = db.AnythingField()
    
    def readingid(self):
        key_num = random.SystemRandom()
        self.readingid = key_num.randint(0, sys.maxsize)
        return self.readingid

    def readingtime(self,readingdate):
        self.readingtime = datetime.datetime.now().timestamp()

    def reading(self, reading):
        self.reading = reading

    def readingtype(self,readingtype):
        values = ['temp','humidity','power','pressure']
        if readingtype not in values:
            abort(404)
        self.readingtype = readingtype

    def sensor_serial(self,sensor_serial):
        self.sensor_serial = sensor_serial

class DeviceCatalog(db.Document):
    #Catalog of supported sensors, updated from time to time
    devicetype = db.StringField()
    devicename = db.StringField()
    deviceid = db.AnythingField()
    devicedesc = db.StringField()

    def devicetype(self,sensortype):
        device_types = ['environment','display']
        if(str(devicetype).lower in device_types):
            self.devicetype = devicetype
        else:
            abort(406)

    def devicename(self,devicename):
        self.devicename = devicename
    
    def deviceid(self,deviceid):
        self.deviceid = deviceid
    
    def devicedesc(self,devicedesc):
        self.devicedesc = devicedesc

class AttachedDevice(db.Document):
    #Inventory of sensors attached to the rackbrain 
    devicetype = db.StringField()
    devicename = db.StringField()
    deviceid = db.AnythingField()
    devicedesc = db.StringField()
    deviceserial = db.AnythingField()
    
    def deviceserial(self):
        key_num = random.SystemRandom()
        self.deviceserial = key_num.randint(0, sys.maxsize)
        return self.deviceserial
    
    def devcietype(self,devicetype):
        self.devicetype = devicetype

    def devicename(self,devicename):
        self.devicename = devicename
    
    def deviceid(self,deviceid):
        self.deviceid = deviceid

    def devicedesc(self,devicedesc):
        self.devicedesc = devicedesc

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
    
    