# Blockchain Mangement platform.
Used to deploy a new block chain for a customer

## Environment.
1. OS - CentOS Linux release 7.4.1708 (Core)
2. Docker - Docker version 17.12.0-ce
3. Dev Language - Python 2.7.5/3.6
4. Mongo - Mongo 3.4.5

## Setup a test environment.
1. Run the dev_env_setup.sh
2. Use the test files in the unittest directory.

NOTE: dev_env_setup.sh will setup all the following components in Docker as a SINGLE node. Please refer to the Tendermint docs to build a multi node testnet.
http://tendermint.readthedocs.io/projects/tools/en/master/index.html

## Run the Unittests
1. cd unittests
2. python 'unittestfile'

## Tools used
1. Robot 3T - Mongo interface
2. MongoDB 3.4.5
3. Gunicorn 19.7.1

## Build, Run, Rebuild the containers
1. Build the container from docker file - make.sh
2. Run the contianer - run_container.sh
3. Stop and remove from images repo - stop_container.sh

## API Examples
Create new user account
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"paul","password":"python"}' -k https://192.168.10.9:8443/api/users

Get a new token
curl -u paul:python -i -k -X GET https://192.168.10.9:8443/api/token

Use the token to talk to endpoint
curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxOTE0NzExNSwiaWF0IjoxNTE5MTQzNTE1fQ.eyJ1c2VyaWQiOjgzNTQ1NjMyODExNzAxMzgwMzV9.BX0xOSSDLmFiBzANy5pMCYfxkB4edgao3O4IK8akO4c:x -i -k -X GET https://192.168.10.9:8443/api/users

## TODO
