# Minimal Debian Guest with GUI
Minimal LXQT install on Debian for virtualisation:

    sudo apt-mark hold xscreensaver

    sudo apt -y install \
      qemu-guest-agent \
      lxqt-admin \
      lxqt-core \
      lxqt-qtplugin \
      lxqt-config \
      lxqt-sudo \
      sddm-theme-debian-maui \
      qterminal \
      htop \
      tmux \
      firefox-esr
  
  # NoMachine
  Verify NoMachine Subscription:

      sudo /etc/NX/nxserver --subscription
