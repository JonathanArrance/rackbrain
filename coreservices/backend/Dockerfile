# Use the python alpine image with python
#need to get this working failing on adafruit stuff
FROM base-python27
MAINTAINER Jonathan Arrance <jonathan.arrance@gmail.com>

ENV INSTALL_PATH /opt/backend
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

ADD requirements.txt /
RUN pip install -r /requirements.txt

# Copy the current directory contents into the container at /app
ADD APIsettings.py $INSTALL_PATH
ADD backendAPI.py $INSTALL_PATH
ADD mongo_lib.py $INSTALL_PATH
ADD api_lib.py $INSTALL_PATH

# Make port 9443 available to the world outside this container
EXPOSE 9443

# Run app.py when the container launches
CMD ["python", "backendAPI.py"]
