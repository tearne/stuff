FROM phusion/baseimage:0.11 as build

ENV NOMACHINE https://download.nomachine.com/download/6.7/Linux/nomachine_6.7.6_11_amd64.deb

EXPOSE 4000

ENV DEBIAN_FRONTEND noninteractive

RUN add-apt-repository ppa:papirus/papirus \
&&  apt update \
&&  apt -y full-upgrade

RUN apt install -y --no-install-recommends \
        curl \
        lxqt-core \        
        # sddm-theme-debian-maui \
        openbox \
        dbus-x11 \   
        lxqt-about \
        lxqt-admin \
        lxqt-openssh-askpass \
        # qterminal \
        xfce4-terminal \
        lxqt-sudo \
        papirus-icon-theme \
        # oxygen-icon-theme \
        # --== Notice below suppressed ==--
        adwaita-icon-theme-

RUN curl -fSL $NOMACHINE -o nomachine.deb \
&&  apt install -y ./nomachine.deb

RUN  apt install -y --no-install-recommends \
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
        firefox \
        ncdu \
        htop \
        tmux \
        nload \
        # glances \
        # iotop \
        # qdirstat \
        # lximage-qt \
        # qpdf \
        # xarchiver \
        featherpad 

# RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
# &&  mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
# &&  echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list
# &&  apt install -y --no-install-recommends code

RUN mkdir -p /etc/xdg/lxqt \
&&  mkdir -p /etc/xdg/xfce4/terminal \
&&  mkdir -p /etc/xdg/pcmanfm-qt/lxqt

COPY config/lxqt.conf /etc/xdg/lxqt/lxqt.conf
COPY config/session.conf /etc/xdg/lxqt/session.conf
COPY config/panel.conf  /etc/xdg/lxqt/panel.conf
COPY config/pcmanfm-qt_settings.conf /etc/xdg/pcmanfm-qt/lxqt/settings.conf
COPY config/terminalrc /etc/xdg/xfce4/terminal/terminalrc

COPY config/setOneDesktop.py /tmp/setOneDesktop.py
RUN chmod +x /tmp/setOneDesktop.py \
&&  /tmp/setOneDesktop.py \
&&  rm /tmp/setOneDesktop.py

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

RUN rm *.deb && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

FROM scratch
COPY --from=build / /

ENTRYPOINT ["/sbin/my_init"]
CMD ["--", "./run.sh"]
