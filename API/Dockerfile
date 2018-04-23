FROM base-python2.7

MAINTAINER Jonathan Arrance <speed3nc@gmail.com>

ENV INSTALL_PATH /opt/API

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD API.py $INSTALL_PATH
ADD mongo_lib.py $INSTALL_PATH
ADD APIsettings.py $INSTALL_PATH
ADD api_lib.py $INSTALL_PATH
ADD mongo_setup.py $INSTALL_PATH

ADD start_api.sh $INSTALL_PATH

EXPOSE 8443

#CMD ["python","API.py"]
CMD ["./start_api.sh"]