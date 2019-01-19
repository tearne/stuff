FROM phusion/baseimage:0.9.19
## Xenial

################################################################################
## System
################################################################################
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
&&  apt-get -y upgrade \
&&  apt-get install -y --no-install-recommends \
        xpra \
        python-lz4 \
        sudo \
        xterm \
        pwgen \
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

################################################################################
## Enable SSH & set up 'user'
################################################################################
RUN rm -f /etc/service/sshd/down \
&&  sed -i "s/.*UsePrivilegeSeparation.*/UsePrivilegeSeparation yes/g" /etc/ssh/sshd_config \
&&  sed -i "s/.*UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \
&&  sed -i "s/.*PermitRootLogin.*/PermitRootLogin no/g" /etc/ssh/sshd_config \
&&  sed -i "s/.*PasswordAuthentication.*/PasswordAuthentication no/g" /etc/ssh/sshd_config \
&&  sed -i "s/.*StrictModes.*/StrictModes yes/g" /etc/ssh/sshd_config

RUN useradd --create-home --shell /bin/bash user \
&&  adduser user sudo

################################################################################
## xpra run and welcome script
################################################################################
COPY run.sh run.sh
RUN chmod +x run.sh

RUN mkdir /.xpra

ENV ROOT_APP "xterm"

EXPOSE 22
ENTRYPOINT ["/sbin/my_init"]
CMD ["--", "./run.sh"]
