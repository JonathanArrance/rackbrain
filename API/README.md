# Rackbrain appliance.
Make dumb AV racks smarter

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

## NOTEs
1. Make sure to check the mongo db and ensure that status-dashboard db is in mongo.
2. Ensure that the accounts, readings, status, and meters collections are in the status-dashboard DB.

## Container Specifics
root_api container - Run - run_gunicorn_app.sh
                    - Stop and remove - stop_container.sh
                    - Build - make.sh

Interface container - not complete, needs to run in nginx

You will want to download this binary
https://stedolan.github.io/jq/download/

This is a link to a great reference implementation
https://github.com/tendermint/basecoin/blob/master/docs/guide/ibc.md

This is a link to some basecoin examples
https://github.com/tendermint/basecoin-examples.git

## API Examples
Create new user account
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"paul","password":"python"}' -k https://192.168.10.9:8443/api/users

Get a new token
curl -u paul:python -i -k -X GET https://192.168.10.9:8443/api/token

Use the token to talk to endpoint
curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxOTE0NzExNSwiaWF0IjoxNTE5MTQzNTE1fQ.eyJ1c2VyaWQiOjgzNTQ1NjMyODExNzAxMzgwMzV9.BX0xOSSDLmFiBzANy5pMCYfxkB4edgao3O4IK8akO4c:x -i -k -X GET https://192.168.10.9:8443/api/users

## TODO