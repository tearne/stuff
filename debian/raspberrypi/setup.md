
# Raspberry Pi Zero

## UART Serial
In `/boot/config.txt` add `enable_uart=1` at the end ([source](https://learn.adafruit.com/adafruit-piuart-usb-console-and-power-add-on-for-raspberry-pi))

[CP2104 driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) for OSX (win/lin don't need it)<sup>[Source].(https://learn.adafruit.com/adafruit-piuart-usb-console-and-power-add-on-for-raspberry-pi/setup-software)</sup>

Look for the device `ls /dev/cu.* /dev/tty.*` and connect `screen /dev/tty.SLAB_USBtoUART 115200`

## Wifi

wpa_supplicant.conf in boot (or directly in /etc/wpa_supplicant dir)

    country=gb
    update_config=1
    ctrl_interface=/var/run/wpa_supplicant

    network={
        ssid="myNetwork"
        psk="myPassword"
    }

If not rebooting:
    wpa_cli -i wlan0 reconfigure


# SSH
Enable ssh by creating `ssh` file in `/boot`, or, when running `sudo systemctl enable ssh`, and `sudo systemctl start ssh`.