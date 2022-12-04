#!/usr/bin/env bash
# @Desc: Deploy the Gunicorn WEB service project
set -u
export LANG=en_US.UTF-8
curdir=`dirname $(readlink -f $0)`
basedir=`dirname $curdir`"/"


# Do not generate pyc compiled files
export PYTHONDONTWRITEBYTECODE=1

# Start configuration items
config_file="gunicorn.config.py"
module_name="app"
instance_name="app"

# Start service
which gunicorn &> /dev/null
if [ $? -eq 0 ]; then
    # Query the number of processes that currently exist in Gunicorn
    p_count=$(ps -ef | grep -c "gunicorn")
    if [ ${p_count} -gt 1 ]; then
        # If there are residual processes, kill them first
        ps aux | grep "gunicorn" | grep -v "grep" | awk '{print $2}' | xargs kill -9
    fi
    # Background hangs, no nohup.out log is generated
    cd ${basedir} && \
      nohup gunicorn ${module_name}:${instance_name} -c ${config_file} 1>/dev/null 2>&1 &
    echo -e "\033[32m\n  Service started successfully! \n\033[0m"
else
    echo -e "\033[33m\n  The module command was not found! \n\033[0m"
fi


#EOF
