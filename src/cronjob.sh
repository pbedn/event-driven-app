#!/bin/bash

echo "------FIRST------"
printenv
echo

# set env vars
set -a
. /tmp/user.env
set +a

echo "------SECOND-------"
printenv
echo

/usr/local/bin/python /app/cron_scheduler.py --$1
