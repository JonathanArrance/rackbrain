#!/bin/python
import random
import sys
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

db = MongoAlchemy(app)
auth = HTTPBasicAuth()
mongo = PyMongo(app)

class Account(db.Document):
    username = db.StringField()
    password_hash = db.StringField()
    userid = db.AnythingField()
    role = db.StringField()

    def gen_id(self):
        #self.userid = None
        #if(self.username == str.lower("admin")):
         #   self.userid == 001
        #elif(self.username == str.lower("backend")):
         #   self.userid == 002
        #elif(self.username == str.lower("interface")):
         #   self.userid == 003
        #else:
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
        #user = Account.query.get(data['userid'])
        user = mongo.db.Account.find_one({'userid':data['userid']})
        return user['userid']

class AccountSpecs(db.Document):
    firstname = db.StringField()
    lastname = db.StringField()
    email = db.AnythingField()
    userid = db.AnythingField()
    
    #NOTE: Wenneed to make sure we have an API to verify the address
    def fname(self,firstname):
        if not firstname:
            abort(406)
        self.firstname = firstname

    def lname(self,lastname):
        if not lastname:
            abort(406)
        self.lastname = lastname

    def email(self,email):
        #need regex to check email
        self.email = email

    def userid(self,userid):
        #need regex to check email
        self.userid = userid

class Sensor(db.Document):
    sensortype = db.StringField()
    sensorname = db.StringField()
    sensorid = db.AnythingField()
    sensordesc = db.StringField()
    
    def sensortype(self,sensortype):
        sensor_types = ['DHT11', 'DHT22', 'Power']
        if(stype in sensor_types):
            self.sensortype = stype
        else:
            abort(406)

    def sensorname(self,sensorname):
        self.sensorname = sensorname
    
    def sensorid(self,sensorid):
        key_num = random.SystemRandom()
        self.sensorid = key_num.randint(0, sys.maxsize)
    
    def sensordesc(self,sensordesc):
        self.sensordesc = sensordesc

class Reading(db.Document):
    reading = db.StringField()
    readingtype = db.StringField()
    sensorid = db.AnythingField()
    
    def reading(self, reading):
        self.reading = reading
    
    def readingtype(self,readingtype):
        values = ['temp','humidity','power']
        if readingtype not in values:
            abort(404)
        self.readingtype = readingtype
    
    def readingdate(self,readingdate):
        pass
    
    def sid(self,sensorid):
        pass

class Device(db.Document):
    devicetype = db.StringField()
    deviceid = db.AnythingField()
    