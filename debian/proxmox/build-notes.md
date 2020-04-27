# PVE Build Notes

## Installation

If disks are different sizes, install onto one ZFS disk in RAID 0, and then add another drive.  May need to deep wipe disk to wipe out any traces of a previous ZFS install.

## GMail Email Relay

Authentication library:

    apt install libsasl2-modules

Make **temporary** password file `/etc/postfix/sasl_passwd` containing login details:

    smtp.gmail.com someone@somewhere.com:[API-password]

Save and protect password file:

    chmod 600 /etc/postfix/sasl_passwd

Create a database from the password file:

    postmap hash:/etc/postfix/sasl_passwd

Delete temporary file `/etc/postfix/sasl_passwd`

Add/change lines in `/etc/postfix/main.cf`:

    # Set gmail as relay
    relayhost = smtp.gmail.com:587

    smtp_use_tls = yes
    smtp_sasl_auth_enable = yes
   
    # Eliminates default security options which are incompatible with gmail
    smtp_sasl_security_options = noanonymous
    smtp_sasl_mechanism_filter = plain
    
    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt

Reload config:

    systemctl restart postfix

Test:

    echo "test message" | mail -s "test subject" me@place.com

https://forum.proxmox.com/threads/how-to-use-google-apps-smtp-to-email-warnings.38236/

### Debugging
In `/etc/postfix/main/cf`:

    #debug_peer_list = smtp.gmail.com
    #debug_peer_level = 3





## Root email forwarding

Test:

    echo "test message" | mail -s "test subject" root

If for some reason it doesn't work out of the box try running `newaliases` to build `/etc/aliases.db`.

    newaliases
    systemctl restart postfix

https://forum.proxmox.com/threads/should-root-email-alias-be-configure.48386/





## SMART

* Temp: `smartctl -a /dev/sda | grep emp`
* Health: `smartctl -H /dev/sda`

### Email alerts setup

`smartmontools` needs to be installed.

Check disks have SMART support and it's enabled:

        smartctl -a /dev/sda | grep "support is:"

Setup `/etc/default/smartmontools`:

        enable_smart="/dev/sda /dev/sdb /dev/sdc /dev/sdd"
        start_smartd=yes
        # Check every 3 hrs
        smartd_opts="--interval=10800"

Setup `/etc/smartd.conf`.  E.g. something like;
        
        # Defaults ( -Hfpu -l error -l selftest -C 197 -U 198)
        /dev/sda -a
        /dev/sdb -a
        /dev/sdc -a
        /dev/sdd -a

        # Long test Fri@11, short every day @ 10
        /dev/sda -s (L/../../6/11|S/../.././10)
        /dev/sdb -s (L/../../6/13|S/../.././11)
        /dev/sdc -s (L/../../6/15|S/../.././12)
        /dev/sdd -s (L/../../6/17|S/../.././13)

        # Email warnings and at startup
        /dev/sda -m root
        /dev/sdb -m root
        /dev/sdc -m root
        /dev/sdd -m root

Adding `-M test` at the end will cause emails at startup (to check it works):

        # Email warnings and at startup
        /dev/sda -m root -M test 


## ZFS

Scrubs setup in cron by default. See `/etc/cron.d/zfsutils-linux`.

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

### Related
* https://pve.proxmox.com/wiki/ZFS_on_Linux#_activate_e_mail_notification
* https://www.reddit.com/r/homelab/comments/8c09pr/guide_to_setting_up_zed_to_email_alerts_for_zfs/


## Other Thigns


* Mount `/tankNN/hyper` in the cluster for VZDump backups
* Set backup schedule for all VMs
* Firewall
