# Wifi
 in `system-boot` volume, exit `network-config`

```
wifis:
  wlan0:
    dhcp4: true
    optional: true
    access-points:
      "MySSID":
        password: "MyPassword"
```

https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#3-wifi-or-ethernet

# zfs

sudo apt install zfs-dkms


# USAP

[Checking](https://superuser.com/questions/928741/how-can-i-check-whether-usb3-0-uasp-usb-attached-scsi-protocol-mode-is-enabled): Run `lsusb` and look for `Driver=uas`.


