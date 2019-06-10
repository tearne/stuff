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
        # nload \
        # glances \
        # iotop \
        # nmon \
        git \
#
        # code \
        firefox \
        ncdu \
        htop \
        tmux \
        # lximage-qt \
        featherpad \
        # qpdf \
        # xarchiver \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/skel/.config/lxqt && mkdir -p /etc/skel/.config/xfce4/terminal
COPY config/skel_lxqt.conf /etc/skel/.config/lxqt/lxqt.conf
COPY config/skel_session.conf /etc/skel/.config/lxqt/session.conf
COPY config/skel_pcmanfm-qt_settings.conf /etc/skel/.config/pcmanfm-qt/lxqt/settings.conf
COPY config/skel_terminalrc /etc/skel/.config/xfce4/terminal/terminalrc

# startscript to copy dotfiles from /etc/skel
RUN echo '#! /bin/sh\n\
[ -n "$HOME" ] && [ ! -e "$HOME/.config" ] && cp -R /etc/skel/. $HOME/ \n\
exec $* \n\
' > /usr/local/bin/start && chmod +x /usr/local/bin/start 

COPY config/xdg_lxqt-rc.xml /etc/xdg/openbox/lxqt-rc.xml

COPY config/xdg_panel.conf.append /tmp/
RUN  cat /tmp/xdg_panel.conf.append >> /etc/xdg/lxqt/panel.conf  && rm -f /tmp/xgd_panel.conf.append

COPY config/base_panel.conf /usr/share/lxqt/panel.conf

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
