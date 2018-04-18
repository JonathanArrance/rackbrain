#!/bin/bash -x
#make sure you run as root


echo "Set up Raspberry Pi docker.\n"
#curl -sSL https://get.docker.com | sh


#Set up a private network to connect the containers
echo "Create a network for our monitor.\n"
docker network create --driver bridge --subnet 172.18.0.0/16 rack_nw

#build the base python image
~/rackbrain/tools/baseimage/make.sh

mkdir -p /opt/mongdata
#get the containers we need
#build the mongo image
docker pull andresvidal/rpi3-mongodb3

#rename the repo
docker tag andresvidal/rpi3-mongodb3 rpi-mongo

#start mongo on port 27017
docker run --restart unless-stopped --name mongo --network rack_nw -d -p 28017:28017 -p 27017:27017 -v /opt/mongodata:/data/db rpi-mongo mongod

#create system level accounts
MONGO=`python mongo_setup.py`
echo $MONGO