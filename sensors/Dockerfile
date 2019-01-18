# Use the python alpine image with python
FROM base-python27 

MAINTAINER Jonathan Arrance <jonathan.arrance@gmail.com>

ENV INSTALL_PATH /opt/sensor
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

ADD requirements.txt /
RUN pip install -r /requirements.txt

# Copy the current directory contents into the container at /app
ADD sensor_lib.py $INSTALL_PATH
ADD settings.py $INSTALL_PATH
