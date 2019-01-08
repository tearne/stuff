# Getting xterm.js in Guest VM
Add a serial hardware device `0` to guest.

Start service in guest:

    sudo systemctl enable serial-getty@ttyS0.service
    sudo systemctl start serial-getty@ttyS0.service

Now it should work.  But will probalby have to press enter when opening the serial (xterm.js) console.

Can also get boot message to go to serial too, but then the _only_ go to serial.  Bit of a pain if you then expect the NoVNC console to prompt you for the disk encryption passphrase.

in `/etc/default/grub`:

    GRUB_CMDLINE_LINUX="quiet console=tty0 console=ttyS0,115200"

sudo update-grub

## Notes
 Install `xterm` to get the `resize` command.

 Towards colour:

    export TERM=xterm-256color


### Relevant

* https://pve.proxmox.com/wiki/Serial_Terminal
* https://ravada.readthedocs.io/en/latest/docs/config_console.html
* https://raspberrypi.stackexchange.com/questions/40848/colored-console-over-serial-connection
