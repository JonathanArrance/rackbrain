#!/bin/bash -x
cp -f ../common/api_lib.py .
cp -f ../common/mongo_lib.py .
docker build -t backend-api .
