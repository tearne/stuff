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

RUN  apt update && apt install -y --no-install-recommends \
        ## gksu gone, see https://itsfoss.com/gksu-replacement-ubuntu/
        openbox \
        # xfwm4 \
        dbus-x11 \   
        lxqt-about \
        lxqt-admin \
        lxqt-openssh-askpass \
        qterminal \
        lxqt-sudo \
#
        #sddm-theme-debian-maui \
        adwaita-icon-theme-full \
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
        ncdu \git \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/skel/.config/lxqt && \
    echo '[General]\n\
__userfile__=true\n\
icon_theme=Adwaita\n\
single_click_activate=false\n\
theme=ambiance\n\
tool_button_style=ToolButtonTextBesideIcon\n\
\n\
[Qt]\n\
doubleClickInterval=400\n\
font="Sans,11,-1,5,50,0,0,0,0,0"\n\
style=Fusion\n\
wheelScrollLines=3\n\
' >/etc/skel/.config/lxqt/lxqt.conf && \
    echo '[General]\n\
__userfile__=true\n\
[Environment]\n\
TERM=qterminal\n\
' >/etc/skel/.config/lxqt/session.conf

# config pcmanfm-qt
RUN mkdir -p /etc/skel/.config/pcmanfm-qt/lxqt && \
    echo '[Desktop]\n\
ShowHidden=true\n\
Wallpaper=/usr/share/lxqt/themes/ambiance/Butterfly-Kenneth-Wimer.jpg\n\
WallpaperMode=stretch\n\
' >/etc/skel/.config/pcmanfm-qt/lxqt/settings.conf

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
