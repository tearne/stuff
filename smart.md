## StarTech `USB31C2SAT3`
Test with

    sudo apt install smartmontools
    sudo smartctl -a -d sat /dev/sda

Temp info

    sudo smartctl -d sat -a /dev/sda | grep emp

## Email alerts setup
Check disks have SMART support and it's enabled (may need `-d sat` as above):

        smartctl -a /dev/sda | grep "support is:"
        sudo smartctl -a -d sat /dev/sda | grep "support is:"
        

Setup `/etc/default/smartmontools`:

```
start_smartd=yes
# Check every 3 hrs
smartd_opts="--interval=10800"
```

Setup `/etc/smartd.conf`.  Commenting out the `DEVICESCAN` line and setting something like the following.  NOTE: May need `-d sat` as above

```        
# -a      Defaults ( -Hfpu -l error -l selftest -C 197 -U 198)
# -s ...  Long test Fri@11, short every day @ 10
# -m      Email warnings 
# -M      Test email at startup to check it works
/dev/sda -a -s (L/../../6/11|S/../.././10) -m root -M test
/dev/sdb -a -s (L/../../6/13|S/../.././11) -m root -M test
/dev/sdc -a -s (L/../../6/15|S/../.././12) -m root -M test
/dev/sdd -a -s (L/../../6/17|S/../.././13) -m root -M test
```

The `-M test` sends confirmation email at startup.

Finally `sudo systemctl restart smartmontools`