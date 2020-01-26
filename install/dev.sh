#!/usr/bin/env bash

set -e
DEBIAN_FRONTEND=noninteractive

curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

sdk install java
sdk install sbt

sudo apt install -y snapd
sudo snap install intellij-idea-community --classic

function save-alias() {

    ALIAS_NAME=`echo "$1" | grep -o ".*="`
    ALIASES_FILE_PATH=$HOME/.bash_aliases

    # Deleting dublicate aliases
    sed -i "/alias $ALIAS_NAME/d" $ALIASES_FILE_PATH

    # Quoting command: my-alias=command -> my-alias="command"
    QUOTED=`echo "$1"\" | sed "s/$ALIAS_NAME/$ALIAS_NAME\"/g"`

    echo "alias $QUOTED" >> $ALIASES_FILE_PATH

    # Loading aliases
    source $ALIASES_FILE_PATH
}


function smartgit_old() {
    VERSION=19_1_6

    wget https://www.syntevo.com/downloads/smartgit/smartgit-$VERSION.deb -O /tmp/smartgit.deb
    sudo apt install -y /tmp/smartgit.deb
    rm /tmp/smartgit.deb

    mkdir -p $HOME/.local/bin
    ln -s /usr/share/smartgit/bin/smartgit.sh $HOME/.local/bin/smartgit
    source $HOME/.profile
}

function smartgit_new() {
    sudo apt install -y flatpak
    sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    sudo flatpak install -y flathub com.syntevo.SmartGit

    save-alise smartgit=flatpak run com.syntevo.SmartGit
}

smartgit_new