 FROM phusion/baseimage:0.11

ENV NOMACHINE https://download.nomachine.com/download/6.7/Linux/nomachine_6.7.6_11_amd64.deb

EXPOSE 4000

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
&&  apt -y full-upgrade \ 
&&  apt install -y --no-install-recommends \
      curl \
      lxqt-core \
&&  curl -fSL $NOMACHINE -o nomachine.deb \
&&  apt install -y ./nomachine.deb \
&&  rm *.deb && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN add-apt-repository ppa:papirus/papirus \
&&  curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
&&  mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
&&  echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list \
&&  apt update \
&&  apt install -y --no-install-recommends \
        # sddm-theme-debian-maui \
        openbox \
        dbus-x11 \   
        lxqt-about \
        lxqt-admin \
        lxqt-openssh-askpass \
        # qterminal \
        xfce4-terminal \
        lxqt-sudo \
#
        # adwaita-icon-theme-full \
        papirus-icon-theme \
        # oxygen-icon-theme \
#
        # gksu   -  No longer available, see https://itsfoss.com/gksu-replacement-ubuntu/
        # dialog \
        apt-transport-https \
        ca-certificates \
        # x11-utils \
        # xz-utils \
        sudo \
        pwgen \
        nano \
        # wget \
        git \
#
        # code \
        firefox \
        ncdu \
        htop \
        tmux \
        nload \
        # glances \
        # iotop \
        # qdirstat \
        # lximage-qt \
        featherpad \
        # qpdf \
        # xarchiver \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/xdg/lxqt \
&&  mkdir -p /etc/xdg/xfce4/terminal \
&&  mkdir -p /etc/xdg/pcmanfm-qt/lxqt

COPY config/lxqt.conf /etc/xdg/lxqt/lxqt.conf
COPY config/session.conf /etc/xdg/lxqt/session.conf
COPY config/panel.conf  /etc/xdg/lxqt/panel.conf
COPY config/pcmanfm-qt_settings.conf /etc/xdg/pcmanfm-qt/lxqt/settings.conf
COPY config/terminalrc /etc/xdg/xfce4/terminal/terminalrc
COPY config/openbox_lxqt-rc.xml /etc/xdg/openbox/lxqt-rc.xml

RUN useradd --create-home --shell /bin/bash user \
&& sudo usermod -aG sudo user

USER user

COPY --chown=user script/setup.sh /home/user/setup.sh
RUN chmod +x ~/setup.sh \
&&  ~/setup.sh \
&&  rm ~/setup.sh

USER root

COPY script/run.sh run.sh
RUN chmod +x run.sh

ENTRYPOINT ["/sbin/my_init"]
CMD ["--", "./run.sh"]
