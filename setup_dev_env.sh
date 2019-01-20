#!/bin/bash -x
#make sure you run as root

COMPOSE='1.23.2'
DOCKER='18.06.0.ce'

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

#check raspian version
VERSION=$(cat /etc/debian_version)

if [ $VERSION !=  9.4 ]
  then echo "Must use Raspbian Stretch 9"
  exit
fi

echo 'Set iptables'
iptables -A INPUT -p tcp --dport 8443 -j ACCEPT
/sbin/service iptables save

echo 'Cleaning off Docker if present.'
apt-get remove docker docker-engine docker.io

echo 'Set up Raspberry Pi Docker CE.'
#curl -sSL https://get.docker.com | sh
apt-get update
apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
apt-key fingerprint 0EBFCD88
echo "deb [arch=armhf] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
apt-get update
apt-get install docker-ce=$DOCKER

echo 'Add pi user to Docker'
usermod -a -G docker $USER
echo 'WARNING: Added pi user to the docker group, user $USERNAME will need to logout once finished for the addition to take effect.'

echo 'Setting up docker compose.'
curl -L https://github.com/docker/compose/releases/download/$COMPOSE/docker-compose-`uname -s`-`uname -m` > /opt/bin/docker-compose
chmod +x /opt/bin/docker-compose
cp /opt/bin/docker-compose

#Set up a private network to connect the containers
echo 'Create a network for our monitor.'
docker network create --driver bridge --subnet 172.18.0.0/16 rack_nw

echo 'Creating the base service image.'
#build the base python image
docker build -t base-python27 ~/coreservices/base-python27

echo 'Creating the base sensor image.'
docekr build -t base-sensor ~/sensors/

#build the mongo image
echo 'Creating the Mongo 3.0.4 image.'
#docker pull andresvidal/rpi3-mongodb3
docker build -t rpi-mongo ~/mongodb/

#create the mongo docker volume
docker volume create mongodata

#start mongo on port 27017
docker run --restart unless-stopped --name rpi-mongo --network rack_nw -d -p 28017:28017 -p 27017:27017 --mount source=mongodata,target=/data rpi-mongo


#create system level accounts
cp ~/coreservices/common/mongo_setup.py ~/rackbrain
MONGO=`python ~/rackbrain/mongo_setup.py`
echo $MONGO