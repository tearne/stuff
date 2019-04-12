# Storage Health
_Tested on Proxmox_

## SMART
### Email alerts

* `smartmontools` needs to be installed.
* Check disks have SMART support and it's enabled:

        smartctl -a /dev/sda | grep "support is:"

* Setup `/etc/default/smartmontools`:

        enable_smart="/dev/sda /dev/sdb"
        start_smartd=yes
        # Check every 3 hrs
        smartd_opts="--interval=10800"

* Setup `/etc/smartd.conf`.  E.g. for each drive;
        
        # Defaults ( -Hfpu -l error -l selftest -C 197 -U 198)
        /dev/sda -a 

        # Long test Fri@11, short every day @ 10
        /dev/sda -s (L/../../6/11|S/../.././10) 
        
        # Email warnings and at startup
        /dev/sda -m root -M test 

    Notes:

        #   -d TYPE Set the device type: ata, scsi, marvell, removable, 3ware,N, hpt,L/M/N
        #   -T TYPE set the tolerance to one of: normal, permissive
        #   -o VAL  Enable/disable automatic offline tests (on/off)
        #   -S VAL  Enable/disable attribute autosave (on/off)
        #   -n MODE No check. MODE is one of: never, sleep, standby, idle
        #   -H      Monitor SMART Health Status, report if failed
        #   -l TYPE Monitor SMART log.  Type is one of: error, selftest                                            Samsung_SSD_850_PRO_256GB
        #   -f      Monitor for failure of any 'Usage' Attributes
        #   -m ADD  Send warning email to ADD for -H, -l error, -l selftest, and -f                                Samsung_SSD_850_PRO_256GB
        #   -M TYPE Modify email warning behavior (see man page)
        #   -s REGE Start self-test when type/date matches regular expression (see man page)                       Samsung_SSD_850_PRO_256GB
        #   -p      Report changes in 'Prefailure' Normalized Attributes
        #   -u      Report changes in 'Usage' Normalized Attributes                                                Samsung_SSD_850_PRO_256GB
        #   -t      Equivalent to -p and -u Directives
        #   -r ID   Also report Raw values of Attribute ID with -p, -u or -t                                       Samsung_SSD_850_PRO_256GB
        #   -R ID   Track changes in Attribute ID Raw value with -p, -u or -t
        #   -i ID   Ignore Attribute ID for -f Directive
        #   -I ID   Ignore Attribute ID for -p, -u or -t Directive
        #   -C ID   Report if Current Pending Sector count non-zero
        #   -U ID   Report if Offline Uncorrectable count non-zero
        #   -W D,I,C Monitor Temperature D)ifference, I)nformal limit, C)ritical limit
        #   -v N,ST Modifies labeling of Attribute N (see man page)
        #   -a      Default: equivalent to -H -f -t -l error -l selftest -C 197 -U 198
        #   -F TYPE Use firmware bug workaround. Type is one of: none, samsung
        #   -P TYPE Drive-specific presets: use, ignore, show, showall

* After `service smartmontools restart` you should get an email.


### Notes
* Temp: `smartctl -a /dev/sda | grep emp`
* Health: `smartctl -H /dev/sda`


## ZFS
### Scrubbing
Manually

        zpool status
        zpool scrub rpool

cron: ***TODO***
* https://forum.proxmox.com/threads/zfs-health.24213/#post-121787

### Email alerts
Assumes a working email relay.

Install

    apt install zfs-zed

Configure `/etc/zfs/zed.d/zed.rc`

* Uncomment (if not already):

        ZED_EMAIL_ADDR="root"    

    Proxmox forwards to configured email address (Datacenter &rarr; Users &rarr; root &rarr; Edit)
* Uncomment:

        ZED_EMAIL_PROG="mail"

* Set:

        ZED_NOTIFY_VERBOSE=1 
        ZED_NOTIFY_DATA=1

Reload service :

        systemctl restart zfs-zed`

**Didn't** need to enable service: `systemctl enable zfs-zed`

### Related
* https://pve.proxmox.com/wiki/ZFS_on_Linux#_activate_e_mail_notification
* https://www.reddit.com/r/homelab/comments/8c09pr/guide_to_setting_up_zed_to_email_alerts_for_zfs/