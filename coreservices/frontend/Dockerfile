FROM base-python27

MAINTAINER Jonathan Arrance <jonathan.arrance@gmail.com>

ENV INSTALL_PATH /opt/frontend

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

ENV PACKAGES="\
  dumb-init \
  musl \
  libc6-compat \
  linux-headers \
  build-base \
  bash \
  git \
  ca-certificates \
  python2 \
  python2-dev \
  py-setuptools \
  g++ \
  gcc \
  libffi \
  libffi-dev \
  openssl \
  openssl-dev \
"
RUN apk add --no-cache $PACKAGES

RUN pip install --upgrade pip
ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD frontend.py $INSTALL_PATH
ADD mongo_lib.py $INSTALL_PATH
ADD APIsettings.py $INSTALL_PATH
ADD api_lib.py $INSTALL_PATH
ADD mongo_setup.py $INSTALL_PATH

ADD start_api.sh $INSTALL_PATH

EXPOSE 8443

CMD ["python","frontend.py"]
#CMD ["./start_api.sh"]
