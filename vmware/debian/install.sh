#!/bin/bash

set -e

export DEBIAN_FRONTEND=noninteractive

sudo apt-mark hold xscreensaver

sudo apt -y install \
  unattended-upgrades \
  lxqt-admin \
  lxqt-core \
  lxqt-qtplugin \
  lxqt-config \
  lxqt-sudo \
  sddm-theme-debian-maui \
  qterminal \
  pavucontrol-qt \
  open-vm-tools-desktop \
  snapd \
  htop \
  gufw \
  firefox
