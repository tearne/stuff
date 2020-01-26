#!/usr/bin/env bash

set -e
DEBIAN_FRONTEND=noninteractive

function install-sdk(){
    sudo apt install -y zip unzip
    curl -s "https://get.sdkman.io" | bash
    source "$HOME/.sdkman/bin/sdkman-init.sh"

    (sdk install java) || true
    (sdk install sbt) || true
}
install-sdk
######################################################

sudo apt install -y snapd
sudo snap install intellij-idea-community --classic
######################################################

function save-alias() {
    # https://unix.stackexchange.com/questions/153977/automatically-put-an-alias-into-bashrc-or-zshrc

    ALIAS_NAME=`echo "$1" | grep -o ".*="`
    ALIASES_FILE_PATH=$HOME/.bash_aliases
    touch $ALIASES_FILE_PATH

    # Deleting dublicate aliases
    sed -i "/alias $ALIAS_NAME/d" $ALIASES_FILE_PATH

    # Quoting command: my-alias=command -> my-alias="command"
    QUOTED=`echo "$1"\" | sed "s/$ALIAS_NAME/$ALIAS_NAME\"/g"`

    echo "alias $QUOTED" >> $ALIASES_FILE_PATH

    # Loading aliases
    source $ALIASES_FILE_PATH
}
######################################################

function install-smartgit() {
    sudo apt install -y flatpak
    sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    sudo flatpak install -y flathub com.syntevo.SmartGit

    save-alias smartgit=flatpak run com.syntevo.SmartGit
    echo "source $HOME/.bashrc or open new terminal"
}
install-smartgit
######################################################