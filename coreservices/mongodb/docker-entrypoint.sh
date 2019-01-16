#!/bin/bash
set -e

#if [ "$1" = 'mongod' ]; then
#     #exec /sbin/tini -- -g /usr/bin/mongod
exec /usr/bin/mongod
#fi

#exec "$@"
