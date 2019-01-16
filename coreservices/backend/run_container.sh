#!/bin/bash
docker run -d -p 9443:9443 -e MONGO_HOST=rpi-mongo --network rack_nw --name backend-api backend-api
