
# Raspberry Pi Zero

## Hostname
Change in `/rootfs/etc/hostname`, and if it's listed in there, `/rootfs/etc/hosts`.

## UART Serial
In `/boot/config.txt` add `enable_uart=1` at the end <sup>[(source)](https://learn.adafruit.com/adafruit-piuart-usb-console-and-power-add-on-for-raspberry-pi)</sup>.

[CP2104 driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) for OSX; win/lin don't need it<sup>[(Source)](https://learn.adafruit.com/adafruit-piuart-usb-console-and-power-add-on-for-raspberry-pi/setup-software)</sup>

When connecting on OSX look for device `ls /dev/cu.* /dev/tty.*` and connect with `screen /dev/tty.SLAB_USBtoUART 115200`

## SPI ON
Uncomment `dtparam=spi=on` in `/boot/config.txt`

## Wifi

wpa_supplicant.conf in boot (or directly in /etc/wpa_supplicant dir)

    country=gb
    update_config=1
    ctrl_interface=/var/run/wpa_supplicant

    network={
        ssid="myNetwork"
        psk="myPassword"
    }

If not rebooting run `wpa_cli -i wlan0 reconfigure`

To turn WiFi off/on and check status:

    sudo rfkill block wifi
    sudo rfkill unblock wifi
    sudo rfkill list all


## SSH
Enable ssh by creating `ssh` file in `/boot`, or, if already running `sudo systemctl enable ssh`, and `sudo systemctl start ssh`.

## EEPROM update
Must be performed on Rasbian OS, won't work on Ubuntu - but only needed once.

sudo apt update
sudo apt full-upgrade
sudo apt install rpi-eeprom
sudo rpi-eeprom-update

`sudo rpi-eeprom-update -a` if needed, then reboot.

https://gist.github.com/bus710/44dee4d679f05ef68a7de48ab0cc01d6

## USB boot
Must be performed on Rasbian OS, won't work on Ubuntu - but only needed once.

`sudo raspi-config`
Run `sudo raspi-config`
Select `Advanced Options`
Select `Bootloader Version`
Select `Default` for factory default settings or `Latest` for the latest stable bootloader release.
`Reboot` (changes only applied during reboot)

On the USB stick

config.txt

```
kernel=vmlinuz
initramfs initrd.img followkernel
```

https://www.raspberrypi.org/documentation/hardware/raspberrypi/booteeprom.md

https://teck78.blogspot.com/2020/11/raspberry-pi-4b-change-usb-boot-order.html

https://askubuntu.com/questions/1254810/booting-ubuntu-server-20-04-on-pi-4-from-usb

## Install minimal LXQT

sudo apt-mark hold xscreensaver

sudo apt -y install \
    lxqt-admin \
    lxqt-core \
    lxqt-qtplugin \
    lxqt-config \
    lxqt-sudo \
    sddm-theme-debian-maui \
    qterminal \
    htop \
    tmux

## Disable MOTD adverts

sudo vi /etc/default/motd-news

Set `ENABLED=0`.

Also disable the service?  

```
sudo systemctl stop motd-news
sudo systemctl disable motd-news
```

https://ostechnix.com/how-to-disable-ads-in-terminal-welcome-message-in-ubuntu-server/