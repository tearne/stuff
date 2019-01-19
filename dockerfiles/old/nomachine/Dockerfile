FROM phusion/baseimage:0.9.19

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
&&  apt -y upgrade \
&&  apt install -y --no-install-recommends\
        curl \
        sudo \
        pulseaudio \
        x11-utils \
        lxde \
        pwgen

RUN curl -L http://download.nomachine.com/download/5.1/Linux/nomachine_5.1.62_1_amd64.deb -o /tmp/nomachine.deb \
&&  dpkg --install /tmp/nomachine.deb \
&&  rm /tmp/*.deb \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i 's|DefaultDesktopCommand.*|DefaultDesktopCommand "/usr/bin/startlxde"|g' /usr/NX/etc/node.cfg
RUN sed -i '/#ConnectPolicy /s/^#//g' /usr/NX/etc/server.cfg
RUN sed -i 's/,automigrate=1/,automigrate=0/g' /usr/NX/etc/server.cfg

RUN useradd --create-home --shell /bin/bash user \
&&  adduser user sudo

COPY run.sh run.sh
RUN chmod +x run.sh

EXPOSE 4000

ENTRYPOINT ["/sbin/my_init"]
CMD ["--", "./run.sh"]
