



https://learn.adafruit.com/adafruit-piuart-usb-console-and-power-add-on-for-raspberry-pi


sudo nano /boot/config.txt
enable_uart=1 on last line

https://learn.adafruit.com/adafruit-piuart-usb-console-and-power-add-on-for-raspberry-pi/setup-software
CP2104 driver for OSX (win/lin don't need it)
http://www.silabs.com/Support%20Documents/Software/Mac_OSX_VCP_Driver.zip


ls /dev/cu.*
dev/cu.usbserial-NNNN or /dev/cu.SLAB_USBtoUART or /dev/cu.usbmodem

screen /dev/cu.usbserial-A4001nCf 115200