FROM openjdk:11-jre-slim

RUN echo "deb http://cdn-fastly.deb.debian.org/debian sid main" > /etc/apt/sources.list

RUN apt update && apt -y upgrade \
&&  apt install -y --no-install-recommends \
        python \
        python-pip \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
&&  pip --no-cache-dir install --upgrade pip setuptools

RUN pip --no-cache-dir install awscli

COPY test-job/target/universal/stage stage
COPY run.sh run.sh

ENTRYPOINT ["/run.sh"]
CMD []
