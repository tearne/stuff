FROM phusion/baseimage:0.11

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
        pcmanfm-qt \
        featherpad \
        # qterminal \ 
        sddm-theme-debian-maui \
        # xfwm4 \
        xarchiver \
        lxqt-qtplugin lxqt-runner lxqt-sudo \
        lxqt-system-theme lxqt-themes \
        lximage-qt lxqt-about lxqt-admin \ 
        lxqt-notificationd lxqt-openssh-askpass lxqt-panel lxqt-policykit \
        lxqt-config \
        # lxqt \
        #git \
        #x11-utils \
        #htop \
        #tmux \
        #nano \
        #wget \
        #nload \
        #ncdu \
        #apt-transport-https \
        ca-certificates \
        xz-utils \
&&  curl -fSL $NOMACHINE -o nomachine.deb \
&&  apt install -y ./nomachine.deb \
&&  rm *.deb && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd --create-home --shell /bin/bash user \
&& sudo usermod -aG sudo user

RUN apt-get update \
&&  apt-get install -y --no-install-recommends \
adwaita-icon-theme \
dbus dbus-user-session dbus-x11 \
#
#   libxmuu1 libxpm4 libxrandr2 libxrender1 libxshmfence1 libxss1 libxt6 \
#   libxtst6 libxv1 libxvidcore4 libxxf86dga1 libxxf86vm1 libyaml-0-2 libzmq5 \
#   libzvbi-common libzvbi0 lximage-qt lximage-qt-l10n lxmenu-data lxqt-about \
#   lxqt-about-l10n lxqt-config lxqt-config-l10n lxqt-core lxqt-globalkeys \
#   lxqt-globalkeys-l10n lxqt-notificationd lxqt-notificationd-l10n lxqt-panel \
#
#   lxqt-panel-l10n lxqt-policykit lxqt-policykit-l10n lxqt-powermanagement \
#   lxqt-powermanagement-l10n lxqt-qtplugin lxqt-runner lxqt-runner-l10n \
#   lxqt-session lxqt-session-l10n lxqt-sudo lxqt-sudo-l10n lxqt-system-theme \
#   lxqt-themes media-player-info mesa-va-drivers mesa-vdpau-drivers miscfiles \
  multiarch-support netbase networkd-dispatcher ntfs-3g oxygen-icon-theme \
#
  p11-kit p11-kit-modules p7zip p7zip-full packagekit packagekit-tools parted \
  pavucontrol-qt pavucontrol-qt-l10n pcmanfm-qt pcmanfm-qt-l10n perl \
  perl-modules-5.26 perl-openssl-defaults pinentry-gnome3 policykit-1 \
  pulseaudio pulseaudio-utils python-talloc python3-cairo python3-certifi \
  python3-chardet python3-cups python3-cupshelpers python3-idna \
  python3-pkg-resources python3-requests python3-six python3-urllib3 \
  python3-xdg qlipper qps qt5-gtk-platformtheme qt5-image-formats-plugins \
  qt5-style-plugins qterminal qterminal-l10n qtermwidget5-data \
  qttranslations5-l10n qtwayland5 rtkit samba-libs shared-mime-info \
  sound-theme-freedesktop system-config-printer system-config-printer-common \
  system-config-printer-udev systemd systemd-sysv ubuntu-mono udev udisks2 \
  unzip upower usbmuxd va-driver-all vdpau-driver-all x11-common x11-utils \
  x11-xkb-utils x11-xserver-utils xarchiver xdg-utils xkb-data xscreensaver \
  xscreensaver-data xz-utils \
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
