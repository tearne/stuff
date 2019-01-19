FROM ubuntu:xenial

RUN echo "deb http://cdn-fastly.deb.debian.org/debian sid main" > /etc/apt/sources.list

RUN apt update && apt -y upgrade \
&&  apt install -y --no-install-recommends \
        python \
        python-pip \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN  pip install --upgrade pip setuptools

RUN  pip --no-cache-dir install awscli

COPY run.sh run.sh

ENTRYPOINT ["/run.sh"]
CMD []
