FROM phusion/baseimage:0.11

ENV NOMACHINE https://download.nomachine.com/download/6.4/Linux/nomachine_6.4.6_1_amd64.deb

EXPOSE 4000

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt -y upgrade \
&&  apt install -y --no-install-recommends \
        curl \
        sudo \
        pwgen \
        dialog \
        ## gksu gone, see https://itsfoss.com/gksu-replacement-ubuntu/
        lxde-core lxde-common lxterminal lxde-icon-theme notification-daemon \ 
&&  curl -fSL $NOMACHINE -o nomachine.deb \
&&  apt install -y ./nomachine.deb \
&&  rm *.deb && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd --create-home --shell /bin/bash user \
&& sudo usermod -aG sudo user

RUN apt-get update \
&&  apt-get install -y --no-install-recommends \
        x11-utils \
        git \
        tmux \
        htop \
        nano \
        wget \
        nload \
        ncdu \
        apt-transport-https \
        ca-certificates \
        xz-utils \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER user

ADD --chown=user setup.sh /home/user/setup.sh
RUN chmod +x ~/setup.sh \
&&  ~/setup.sh \
&&  rm ~/setup.sh

USER root

COPY run.sh run.sh
RUN chmod +x run.sh

ENTRYPOINT ["/sbin/my_init"]
CMD ["--", "./run.sh"]
