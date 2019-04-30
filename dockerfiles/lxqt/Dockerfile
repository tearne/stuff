FROM ubuntu:18.04

ENV NOMACHINE https://download.nomachine.com/download/6.6/Linux/nomachine_6.6.8_5_amd64.deb

EXPOSE 4000

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
&&  apt -y full-upgrade

RUN  apt install -y --no-install-recommends \
        curl \
        sudo \
        pwgen \
        dialog \
        ## gksu gone, see https://itsfoss.com/gksu-replacement-ubuntu/
        openbox \
        #pcmanfm-qt
        featherpad \
        # qterminal sddm-theme-debian-maui \
        # xfwm4 \
        xarchiver \
        lxqt \
        lxqt-about lxqt-admin lxqt-config lxqt-core \
        lxqt-notificationd lxqt-openssh-askpass lxqt-panel lxqt-policykit \
        lxqt-qtplugin lxqt-runner lxqt-sudo \
        lxqt-system-theme lxqt-themes \
        lximage-qt \
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
&&  curl -fSL $NOMACHINE -o nomachine.deb \
&&  apt install -y ./nomachine.deb \
&&  rm *.deb && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd --create-home --shell /bin/bash user \
&& sudo usermod -aG sudo user

RUN apt-get update \
&&  apt-get install -y --no-install-recommends \

&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER user

ADD --chown=user setup.sh /home/user/setup.sh
RUN chmod +x ~/setup.sh \
&&  ~/setup.sh \
&&  rm ~/setup.sh

USER root

COPY run.sh run.sh
RUN chmod +x run.sh

CMD ["./run.sh"]
