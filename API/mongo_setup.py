#!/usr/bin/python
from pymongo import MongoClient
import APIsettings as settings
import logging
import random
import datetime
import sys

print settings.MONGO_HOST
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

   if('RackBrainSys' not in collections):
      print "Creating RackBrainSys table with default values."
      #system level stuff
      Sys = db.RackBrainSys.insert_many([{'rackid':rackid,'manufacture_date':now.isoformat()}])
   else:
      print "RackBrainSys table exists."

   #build out the default accounts
   if('Account' not in collections):
      print "Creating Account table with default values."
      #password: rackbrain
      Acc = db.Account.insert_many([{"username":"admin",
                                              "password_hash":"$5$rounds=535000$o.iBk6PxET4Oo5WA$5EXk1LpZkN02LMob9iCBGKao8.kMIhmqOJhtK0mQHu4",
                                              "userid":0001,
                                              "role":"admin"
                                              },
                                              {"username":"backend",
                                              "password_hash":"$5$rounds=535000$o.iBk6PxET4Oo5WA$5EXk1LpZkN02LMob9iCBGKao8.kMIhmqOJhtK0mQHu4",
                                              "userid":0002,
                                              "role":"service"},
                                              {"username":"interface",
                                              "password_hash":"$5$rounds=535000$o.iBk6PxET4Oo5WA$5EXk1LpZkN02LMob9iCBGKao8.kMIhmqOJhtK0mQHu4",
                                              "userid":0003,
                                              "role":"service"}
                                              ])

   else:
      print "Account table exists."

   if('AccountSpecs' not in collections):
      print "Creating AccountSpecs table with default values."
      Aspec = db.AccountSpecs.insert_many([{
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
                                      ])

   else:
      print "AccountSpecs table exists."

   if('Sensor' not in collections):
      print "Creating Sensor table with default values."
      #build out the default sensors
      Sensor = db.Sensor.insert_many([{
                                       "sensortype":"DHT11",
                                       "sensorname":"Temp and Humidity Sensor",
                                       "sensorid":"DHT11-001",
                                       "sensordesc": "General purpose temperature and humidity sensor."
                                       },
                                       {
                                       "sensortype":"DHT22",
                                       "sensorname":"Advanced Temp and Humidity Sensor",
                                       "sensorid":"DHT22-001",
                                       "sensordesc": "Highly sensative temperature and humidity sensor."
                                       },
                                       {
                                       "sensortype":"Power",
                                       "sensorname":"Power",
                                       "sensorid":"Power",
                                       "sensordesc": "General purpose power sensor."
                                       }])
   else:
      print "Sensor table exists."

   #return {"Accounts":Acc,"AccountSpecs":Aspec,"Sensor":Sensor}

if __name__ == '__main__':
   #if (check_mongo() == 'down'):
   #   start_mongo()
   #   if(check_mongo == 'down')
   #      nuke_mongo()
    setup_mongo()