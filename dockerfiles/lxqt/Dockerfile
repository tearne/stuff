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
&&  apt update \
&&  apt install -y --no-install-recommends \
        ## gksu gone, see https://itsfoss.com/gksu-replacement-ubuntu/
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
        # sddm-theme-debian-maui \
        # adwaita-icon-theme-full \
        papirus-icon-theme \
        # oxygen-icon-theme \
#
        apt-transport-https \
        ca-certificates \
        juffed \
        xarchiver \
        lximage-qt \
        x11-utils \
        xz-utils \
        sudo \
        pwgen \
        htop \
        tmux \
        nano \
        wget \
        nload \
        # ncdu \
        git \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ENV CODEDEB=https://go.microsoft.com/fwlink/?LinkID=760868
# ADD $CODEDEB code.deb
# RUN apt-get update && apt-get -y install \
#     --no-install-recommends \
#     ./code.deb \
# #     libgtk2.0-0 \
# #     libx11-xcb1 \
# #     libxtst6 \
# #     libxss1 \
# #     libasound2 \
# #     git \
# #     openssh-server \
# #     xauth \
# #     ttf-ubuntu-font-family \
# #     sudo \
#  &&  rm -rf code.deb \
#  &&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg &&\
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg &&\
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list

RUN mkdir -p /etc/skel/.config/lxqt
ADD configs/skel_lxqt.conf /etc/skel/.config/lxqt/lxqt.conf
ADD configs/skel_session.conf /etc/skel/.config/lxqt/session.conf
ADD configs/skel_pcmanfm-qt_settings.conf /etc/skel/.config/pcmanfm-qt/lxqt/settings.conf

# config panel / add some launchers
RUN echo '[quicklaunch]\n\
alignment=Left\n\
apps\\1\desktop=/usr/share/applications/pcmanfm-qt.desktop\n\
apps\\2\desktop=/usr/share/applications/qterminal.desktop\n\
apps\size=2\n\
type=quicklaunch\n\
' >> /etc/xdg/lxqt/panel.conf

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
