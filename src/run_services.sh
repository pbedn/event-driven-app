#!/bin/bash

printenv | egrep 'SECRET|LOG_FILE|MONGO' >> /tmp/user.env

# run processes in the background
cron

python run_web.py &

python run_service.py &

python run_scheduler.py &

# wait for any process to exit
wait -n

# exit with status of process that exited first
exit $?