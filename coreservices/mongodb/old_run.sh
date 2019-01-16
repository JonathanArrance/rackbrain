docker run --restart unless-stopped --name rpi-mongo --network rack_nw -d -p 28017:28017 -p 27017:27017 -v ~/configdb:/data/configdb -v ~/mongodata:/data/db rpi-mongo
