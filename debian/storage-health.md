# Storage Health
_Tested on Proxmox_

## SMART
### Email alerts
***TODO***

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

* Uncomment 

        ZED_EMAIL_ADDR="root"    

    Proxmox forwards to configured email address (Datacenter &rarr; Users &rarr; root &rarr; Edit)
* Uncomment:

        ZED_EMAIL_PROG="mail"
        ZED_EMAIL_OPTS="-s '@SUBJECT@' @ADDRESS@"

* Set:

        ZED_NOTIFY_VERBOSE=1 
        ZED_NOTIFY_DATA=1

Reload service: `systemctl restart zfs-zed`

### Didn't need to...
* Enable service: `systemctl enable zfs-zed`

### Related
* https://www.reddit.com/r/homelab/comments/8c09pr/guide_to_setting_up_zed_to_email_alerts_for_zfs/