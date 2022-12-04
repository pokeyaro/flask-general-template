from gevent import monkey
monkey.patch_all()
import multiprocessing

## [Reference] https://docs.gunicorn.org/en/latest/configure.html

# debug = True               # Developer debug mode, production off.

# Log level
loglevel = 'debug'

# Bind ip and listening port
bind = '127.0.0.1:8000'      # Bind the port to communicate with Nginx.

# Set pid file
pidfile = 'logs/gunicorn.pid'

# Set the log path
accesslog = 'logs/access.log'
errorlog = 'logs/error.log'

# Setup daemon
daemon = True                # If you use Gunicorn to manage directly, you need to enable this option; if you use Supervisor to manage, you need to comment this option.

# Number of parallel worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Set the working mode to coroutine
worker_class = 'gevent'      # The default is blocking mode, it is better to choose Gevent mode.

# Set timeout
timeout = 60                 # Default 30s

