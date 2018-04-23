#!/bin/bash
echo 'Creating the base container image.'
#build the base python image
~/rackbrain/tools/baseimage/make.sh

mkdir -p /opt/mongdata
mkdir -p /opt/configdb
#get the containers we need

#build the mongo image
echo 'Creating the Mongo 3.0.4 image.'
#docker pull andresvidal/rpi3-mongodb3
~/rackbrain/tools/mongodb/make.sh

#start mongo on port 27017
docker run --restart unless-stopped \
--name mongo \
--network rack_nw -d \
-p 28017:28017 \
-p 27017:27017 \
-v /opt/configdb:/data/configdb \
-v /opt/mongodata:/data/db rpi-mongo mongod --rest

#create system level accounts
MONGO=`python ./mongoddb/mongo_setup.py`
echo $MONGO
