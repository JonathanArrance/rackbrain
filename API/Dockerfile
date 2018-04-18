FROM base-python2.7

MAINTAINER Jonathan Arrance <speed3nc@gmail.com>

ENV INSTALL_PATH /opt/publicAPI

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD API.py $INSTALL_PATH
ADD mongo_lib.py $INSTALL_PATH
#ADD mongo_setup.py $INSTALL_PATH
ADD APIsettings.py $INSTALL_PATH
ADD api_lib.py $INSTALL_PATH

EXPOSE 8443

ENV NAME rack-api

CMD ["python","API.py"]