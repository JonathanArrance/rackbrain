# Use the python alpine image with python
FROM base-sensor

MAINTAINER Jonathan Arrance <jonathan.arrance@gmail.com>

ENV INSTALL_PATH /opt/sensor
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

#add gcc and some builld libs to alpine
RUN apk add build-base

ADD requirements.txt /
RUN pip install -r /requirements.txt

# Copy the current directory contents into the container at /app
ADD dht.py $INSTALL_PATH

#ENTRYPOINT ['python','dht.py']