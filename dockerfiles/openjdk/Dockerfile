FROM openjdk:11-jre-slim

ENV DEBIAN_FRONTEND noninteractive

#RUN echo "deb http://http.debian.net/debian sid main" > /etc/apt/sources.list.d/debian-unstable.list
	## && echo 'APT::Default-Release "testing";' > /etc/apt/apt.conf.d/default

ENV R_BASE_VERSION 3.5.1

RUN apt-get update -y \
&&  apt-get -y upgrade \
&&  apt-get install -t unstable -y --no-install-recommends\
        vim \
        nano \
        htop \
        r-base=${R_BASE_VERSION}* \
        r-base-dev=${R_BASE_VERSION}* \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY installRPackages.sh /tmp
RUN /tmp/installRPackages.sh && rm /tmp/installRPackages.sh
