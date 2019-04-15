#!/usr/bin/python
import os

#MONGO_PORT = 27017
MONGO_HOST = os.getenv('MONGO_HOST','localhost')
REDIS_HOST = os.getenv('REDIS_HOST','localhost')
MONGO_PORT = os.getenv('MONGO_PORT',27017)
REDIS_PORT = os.getenv('REDIS_PORT',6379)

MONGO_DBNAME = 'rack'

URI = "mongodb://%s:%s/%s"%(MONGO_HOST,MONGO_PORT,MONGO_DBNAME)

MONGO_URI=os.getenv('MONGO_URI',URI)

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'


SECRET_KEY =  'the quick brown fox jumps over the lazy dog'

API_VERSION= '1.0'

