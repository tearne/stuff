#!/usr/bin/env bash

set -e
DEBIAN_FRONTEND=noninteractive

curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

sdk install java
sdk install sbt

sudo apt install snapd
sudo snap install intellij-idea-community --classic

function smartgit {
    VERSION=19_1_6

    wget https://www.syntevo.com/downloads/smartgit/smartgit-$VERSION.deb -O /tmp/smartgit.deb
    sudo apt install /tmp/smartgit.deb
    rm /tmp/smartgit.deb
}

smartgit