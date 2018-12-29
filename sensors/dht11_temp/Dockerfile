# Use the python alpine image with python
FROM alpine-python

MAINTAINER Jonathan Arrance <jonathan.arrance@gmail.com>

ENV INSTALL_PATH /opt/dht
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

ADD requirements.txt /
RUN pip install -r /requirements.txt

# Copy the current directory contents into the container at /app
ADD sensor.py $INSTALL_PATH
ADD settings.py $INSTALL_PATH

# Define environment variable
ENV NAME dht11

# Run app.py when the container launches
CMD ["python", "sensor.py"]