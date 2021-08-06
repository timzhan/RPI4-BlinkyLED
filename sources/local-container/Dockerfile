
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