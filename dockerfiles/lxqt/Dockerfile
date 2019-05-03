FROM phusion/baseimage:0.11

ENV NOMACHINE https://download.nomachine.com/download/6.6/Linux/nomachine_6.6.8_5_amd64.deb

EXPOSE 4000

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
&&  apt -y full-upgrade \ 
&&  apt install -y --no-install-recommends \
      curl \
      dialog \
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
        # xfwm4 xfwm4-themes xfwm4-theme-breeze \
        # kwin-x11 kwin-addons kde-style-breeze kde-style-breeze-qt4 \
        dbus-x11 \   
        lxqt-about \
        lxqt-admin \
        lxqt-openssh-askpass \
        qterminal \
        lxqt-sudo \
#
        # adwaita-icon-theme-full \
        papirus-icon-theme \
        # oxygen-icon-theme \
#
        # gksu   -  No longer available, see https://itsfoss.com/gksu-replacement-ubuntu/
        apt-transport-https \
        ca-certificates \
        x11-utils \
        xz-utils \
        sudo \
        pwgen \
        nano \
        wget \
        nload \
        git \
#
        code \
        firefox \
        ncdu \
        htop \
        tmux \
        # lximage-qt \
        # juffed \
        # xarchiver \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg &&\
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg &&\
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list

RUN mkdir -p /etc/skel/.config/lxqt
COPY configs/skel_lxqt.conf /etc/skel/.config/lxqt/lxqt.conf
COPY configs/skel_session.conf /etc/skel/.config/lxqt/session.conf
COPY configs/skel_pcmanfm-qt_settings.conf /etc/skel/.config/pcmanfm-qt/lxqt/settings.conf

COPY configs/xdg_lxqt-rc.xml /etc/xdg/openbox/lxqt-rc.xml

COPY configs/xdg_panel.conf.append /tmp/
RUN  cat /tmp/xdg_panel.conf.append >> /etc/xdg/lxqt/panel.conf  && rm -f /tmp/xgd_panel.conf.append

# startscript to copy dotfiles from /etc/skel
# runs either CMD or image command from docker run
RUN echo '#! /bin/sh\n\
[ -n "$HOME" ] && [ ! -e "$HOME/.config" ] && cp -R /etc/skel/. $HOME/ \n\
exec $* \n\
' > /usr/local/bin/start && chmod +x /usr/local/bin/start 

ADD configs/base_panel.conf /usr/share/lxqt/panel.conf

RUN useradd --create-home --shell /bin/bash user \
&& sudo usermod -aG sudo user

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
