#!/usr/bin/python
from pymongo import MongoClient
import APIsettings as settings
import logging
import random
import datetime
import sys

def start_mongo():
    pass

def nuke_mongo():
    pass

def setup_mongo():
    #Mongo connection
    client = MongoClient(settings.MONGO_HOST, int(settings.MONGO_PORT))
    db = client[settings.MONGO_DBNAME]
    collections = db.collection_names()

    #Rack ID
    key_num = random.SystemRandom()
    rackid = key_num.randint(0, sys.maxsize)

    #get the current date
    now = datetime.datetime.now()
   
    #set the hard code version
    version = 'alpha 1'

    if('RackBrainSys' not in collections):
        print "Creating RackBrainSys table with default values."
        #system level stuff
        Sys = db.RackBrainSys.insert({'rackid':rackid,
                                           'manufacture_date':now.isoformat(),
                                           'version':version,
                                           'location':None,
                                           'setup_date':None})
    else:
        print "RackBrainSys table exists."

    #build out the default accounts
    if('Account' not in collections):
        print "Creating Account table with default values."
        #password: rackbrain
        accs = [{"username":"admin",
                    "password_hash":"$5$rounds=535000$o.iBk6PxET4Oo5WA$5EXk1LpZkN02LMob9iCBGKao8.kMIhmqOJhtK0mQHu4",
                    "userid":0001,
                    "role":"admin"},
                    {"username":"backend",
                    "password_hash":"$5$rounds=535000$o.iBk6PxET4Oo5WA$5EXk1LpZkN02LMob9iCBGKao8.kMIhmqOJhtK0mQHu4",
                    "userid":0002,
                    "role":"service"},
                    {"username":"interface",
                    "password_hash":"$5$rounds=535000$o.iBk6PxET4Oo5WA$5EXk1LpZkN02LMob9iCBGKao8.kMIhmqOJhtK0mQHu4",
                    "userid":0003,
                    "role":"service"}
                    ]
        Acc = db.Account.insert(accs)

    else:
        print "Account table exists."

    if('AccountSpecs' not in collections):
        print "Creating AccountSpecs table with default values."
        specs = [{
                        "firstname":"admin",
                        "lastname":"none",
                        "email":"%s@rackbrainav.com"%(rackid),
                        "userid":0001
                        },
                        {
                        "firstname":"backend",
                        "lastname":"none",
                        "email":"%s@rackbrainav.com"%(rackid),
                        "userid":0002
                        },
                        {
                        "firstname":"interface",
                        "lastname":"none",
                        "email":"%s@rackbrainav.com"%(rackid),
                        "userid":0003
                        }
                    ]
        Aspec = db.AccountSpecs.insert(specs)

    else:
       print "AccountSpecs table exists."

    if('Sensor' not in collections):
       print "Creating a Sensor inventory table"
       Sensor = db.Sensor.insert({"sensortype":None,
                                        "sensorname":None,
                                        "sensorid":None,
                                        "sensordesc":None})
    else:
       print "Sensor inventory table already exists"

    if('SensorCatalog' not in collections):
       print "Creating SensorCatalog table with default values."
       #build out the default sensors
       sensorcatalog = [{
                                       "sensortype":"temp",
                                       "sensorname":"Temp and Humidity Sensor",
                                       "sensorid":"DHT11-001",
                                       "sensordesc": "General purpose temperature and humidity sensor."
                                       },
                                       {
                                       "sensortype":"temp",
                                       "sensorname":"Advanced Temp and Humidity Sensor",
                                       "sensorid":"DHT22-001",
                                       "sensordesc": "Highly sensative temperature and humidity sensor."
                                       },
                                       {
                                       "sensortype":"power",
                                       "sensorname":"Power",
                                       "sensorid":"Power",
                                       "sensordesc": "General purpose power sensor."
                                       },
                                       {
                                       "sensortype":"photo",
                                       "sensorname":"PhotoSensor",
                                       "sensorid":"Photo",
                                       "sensordesc": "General purpose photo sensor."   
                                       },
                                       {
                                       "sensortype":"pressure",
                                       "sensorname":"PressureSensor",
                                       "sensorid":"Pressure",
                                       "sensordesc": "General purpose pressure sensor."
                                       }]
       Sensor = db.SensorCatalog.insert(sensorcatalog)
    else:
       print "SensorCatalog table exists."

    if('Device' not in collections):
       print "Creating a Device inventory table"
       Device = db.Device.insert({"devicetype":None,
                                        "devicename":None,
                                        "deviceid":None,
                                        "devicedesc":None})
    else:
       print "Device inventory table already exists"

    if('DeviceCatalog' not in collections):
       print "Creating DeviceCatalog table with default values."
       #build out the default sensors
       devicecatalog = [{
                                "devicetype":"environment",
                                "devicename":"fan",
                                "deviceid":"FAN-001",
                                "devicedesc": "General purpose cooling fan."
                                },
                                {
                                "devicetype":"display",
                                "devicename":"small LCD",
                                "deviceid":"LCD-001",
                                "devicedesc": "General purpose LCD."
                                }]
       Device = db.DeviceCatalog.insert(devicecatalog)
    else:
       print "DeviceCatalog table exists."
    
    if('Reading' not in collections):
       print "Creating Reading table with default values."
       #build out the default sensors
       reading = [{
                                "readingid":None,
                                "readingtime":None,
                                "reading":None,
                                "readingtype":None,
                                "readingunit":None,
                                "sensorserial":None,
                                }]

       Reading = db.Reading.insert(reading)
    else:
       print "DeviceCatalog table exists."

if __name__ == '__main__':
    #if (check_mongo() == 'down'):
    #   start_mongo()
    #   if(check_mongo == 'down')
    #      nuke_mongo()
    setup_mongo()