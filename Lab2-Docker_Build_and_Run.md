# Lab 2: Docker Build and Run the app

## Prerequisites:
- Lab 1 need to completed


## Create a Dockerfile

```

FROM arm32v7/python:3.7-slim-buster

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-setuptools

# Install RPi.GPIO
RUN pip3 install RPi.GPIO

COPY . .

CMD [ "python3", "test_Blinky_Led.py"]
```

We use python:3.7 here just for the reason that the default version of RPI4 is Python 3.7. You may use 3.8, 3,9 or 3.10.


## Build Docker image

Use below commands:

```
sudo docker build -t blinky-led:v1 .
```

## Run the container

Use below commands:

```
sudo docker run --privileged blinky-led

```

You will see the LED blinking for 5 times.

