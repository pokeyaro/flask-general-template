# Serve

> Use the `flask_restful` Library to quickly write a lightweight backend web WSGI project. The deployment plan at each stage is provided below.

## Operation mode

### Development/Test：Developer mode

![image](https://user-images.githubusercontent.com/58482090/199562435-5ff456ab-dce8-4591-addb-167a533f729e.png)

```shell
# No pyc cache file
root@web-server:/serve# python3 -B app.py

# Installation command
root@web-server:/serve# apt-get install curl jq

# Test request
root@web-server:/serve# curl -s http://127.0.0.1/api/hello | jq .
```

### Stage: Gunicorn Start

![image](https://user-images.githubusercontent.com/58482090/199562838-8bc81c39-29c5-451d-9570-fcf3bbef0f64.png)

```shell
root@web-server:/serve# shell/start.sh 

  The service has been successfully started!

root@web-server:/serve# shell/stop.sh 

  Stop all services!
```

### Production: Use Supervisor for service hosting

`Flask` + `Gunicorn` + `Supervisor` + `Nginx`

