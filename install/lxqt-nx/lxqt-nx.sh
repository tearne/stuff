#!/usr/bin/env bash

set -e
DEBIAN_FRONTEND=noninteractive

function set-wd
{
    SOURCE="${BASH_SOURCE[0]}"
    while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
            DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
            SOURCE="$(readlink "$SOURCE")"
            [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
    done
    DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"

    cd $DIR
}
######################################################


function dist-check
{
    uname -a | grep -q "Ubuntu" 
    if ! [ $? -eq 0 ]; then
            echo "This isn't Ubuntu, exiting."
            exit 1
    fi
}
######################################################


# function sudo-check
# {
#     if [ "$EUID" -ne 0 ]
#         then echo "Please run script using sudo or as root."
#         exit
#     fi
# }
######################################################


function core-packages
{
    sudo add-apt-repository -y ppa:papirus/papirus && apt update
    sudo apt install -y --no-install-recommends \
        lxqt-core \
        dbus-x11 \
        openbox \
        lxqt-about \
        lxqt-admin \
        lxqt-openssh-askpass \
        xfce4-terminal \
        lxqt-sudo \
        adwaita-icon-theme-full \
        papirus-icon-theme 
}
######################################################


function user-packages
{
    sudo apt install -y --no-install-recommends \
        x11-utils \
        xz-utils \
        nano \
        wget \
        nload \
        glances \
        iotop \
        nmon \
        git \
        firefox \
        ncdu \
        htop \
        tmux \
        lximage-qt \
        featherpad \
        ubuntu-make \
        snapd \
        qpdf \
        qdirstat \
        xarchiver \
        unzip \ # sdkman
        zip     # sdkman

    #apt install -y --no-install-recommends snapd
    #snap install --classic code
}
######################################################


function config
{
    sudo mkdir -p /etc/xdg/lxqt
    sudo cp config_files/lxqt.conf /etc/xdg/lxqt/lxqt.conf
    sudo cp config_files/session.conf /etc/xdg/lxqt/session.conf
    sudo cp config_files/panel.conf /etc/xdg/lxqt/panel.conf
    
    sudo mkdir -p /etc/xdg/pcmanfm-qt/lxqt
    sudo cp config_files/pcmanfm-qt_settings.conf /etc/xdg/pcmanfm-qt/lxqt/settings.conf
    
    sudo mkdir -p /etc/xdg/xfce4/terminal
    sudo cp config_files/terminalrc /etc/xdg/xfce4/terminal/terminalrc

    sudo sed -i '/^TEMPLATES/s/^/#/g' /etc/xdg/user-dirs.defaults
    sudo sed -i '/^PUBLICSHARE/s/^/#/g' /etc/xdg/user-dirs.defaults
    sudo sed -i '/^DOCUMENTS/s/^/#/g' /etc/xdg/user-dirs.defaults
    sudo sed -i '/^MUSIC/s/^/#/g' /etc/xdg/user-dirs.defaults
    sudo sed -i '/^PICTURES/s/^/#/g' /etc/xdg/user-dirs.defaults
    sudo sed -i '/^VIDEOS/s/^/#/g' /etc/xdg/user-dirs.defaults
}
######################################################


function nomachine
{
    NOMACHINE=https://download.nomachine.com/download/6.9/Linux/nomachine_6.9.2_1_amd64.deb

    sudo apt update
    sudo apt install curl
    curl -fSL $NOMACHINE -o /tmp/nomachine.deb
    sudo apt install /tmp/nomachine.deb
    rm /tmp/*.deb

    # mkdir -p $HOME/.nx/config
    # cp $HOME/.ssh/authorized_keys $HOME/.nx/config/authorized.crt \
    # chmod 600 $HOME/.nx/config/authorized.crt

    # sed -i 's|DefaultDesktopCommand.*|DefaultDesktopCommand "/usr/bin/startlxde"|g' /usr/NX/etc/node.cfg

    # SSH
    # sed -i '/#ClientConnectionMethods /s/^#//g' /usr/NX/etc/server.cfg
    # sed -i 's/ClientConnectionMethods NX$/ClientConnectionMethods NX,SSH/g' /usr/NX/etc/server.cfg

    # sed -i '/#ConnectPolicy /s/^#//g' /usr/NX/etc/server.cfg

    # Boot to console, not GUI (required for free version)
    sudo systemctl enable multi-user.target
    sudo systemctl set-default multi-user.target

    sudo /etc/NX/nxserver --restart
}
######################################################


# sudo-check
set-wd

core-packages # Always run first, it does an apt update
user-packages
config
nomachine

tail -f /usr/NX/var/log/nxserver.log