#!/usr/bin/env bash

# Try killing the Gunicorn process
ps aux | awk '/gunicorn/{if ($0!~/awk/) system("kill -9 "$2)}' && \
  echo -e "\033[31m\n  All services have been stopped! \n\033[0m"


#EOF
