# Defaults
`ssh ubuntu@ubuntu` 
password `ubuntu`

## Disabling UBoot and enabling USB Boot
In `config.txt` (either in `system-boot` if mounted USB, or in `/boot/firmware` on a live system).

Allows zero 2 to boot 20.04.  See "Boot Surgery" section.
https://waldorf.waveform.org.uk/2021/you-boot-no-u-boot-first.html

* Comment out all the kernel= lines pointing to U-boot,
* Comment out `#device_tree_address=0x03000000` under [all]
* Under `[all]` add `kernel=vmlinuz`, and `initramfs initrd.img followkernel`


## Setting Up Wifi
In `system-boot` volume, edit `network-config`

```
wifis:
  wlan0:
    dhcp4: true
    optional: true
    access-points:
      "MySSID":
        password: "MyPassword"
```

These settings are saved in `/etc/netplan/50-cloud-init.yaml`.  If you change directly, reload with `sudo netplan apply`.

https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#3-wifi-or-ethernet

https://askubuntu.com/questions/1233708/permanently-disable-wlan0-on-raspberrypi-running-ubuntu-20

https://askubuntu.com/questions/1249708/connect-raspberry-pi-4-with-ubuntu-server-to-wifi


## Disabling wifi and bluetooth
In `usercfg.txt` (either in `system-boot` if mounted USB, or in `/boot/firmware` on a live system).

```
dtoverlay=disable-bt
dtoverlay=disable-wifi
```

## Disabling HDMI output
?

# zfs

sudo apt install zfs-dkms


# USAP

[Checking](https://superuser.com/questions/928741/how-can-i-check-whether-usb3-0-uasp-usb-attached-scsi-protocol-mode-is-enabled): Run `lsusb` and look for `Driver=uas`.


# SWAP on Zero 2
https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04

# Removing snap stuff
sudo apt remove snap lxd-agent-loader