#!/bin/bash
docker run -e MONGO_HOST=mongo345 --network rack_nw --name backend-api backend-api
