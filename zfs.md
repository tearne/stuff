# ZFS
Install on ubuntu with
sudo apt install zfs-dkms

Scrubs are setup in cron by default. See `/etc/cron.d/zfsutils-linux`.

## Email alerts
Assumes a working email relay.

Install

    sudo apt install zfs-zed

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


### Other

Email on scrub start
* https://forum.proxmox.com/threads/zfs-scrub_start-event-for-rpool.56159/

## Related

* https://www.reddit.com/r/homelab/comments/8c09pr/guide_to_setting_up_zed_to_email_alerts_for_zfs/

## Replacing a root ZFS mirror drive

Suppose we have

	NAME                   STATE     READ WRITE CKSUM
	rpool                  DEGRADED     0     0     0
	  mirror-0             DEGRADED     0     0     0
	    sda3               OFFLINE      0     0     0
	    sdb3               ONLINE       0     0     0

To find the details of the duff disk (may need a `-d sat`):

    smartctl -a /dev/sdb | grep Serial

Once you've put in a new drive for sda:

    sgdisk --replicate=/dev/sda /dev/sdb
    sgdisk --randomize-guids /dev/sda
    grub-install /dev/sda

    zpool replace rpool sda3 /dev/sda3

    or, for adding a disk to a raid-0 mirror with only one disk:

    zpool attach -f rpool /dev/sdb3 /dev/sda3


This is also good for working around the "ZFS mirrored disks must have the same size" problem during first install.  Start with a single RAID0 smallest disk, then `attach` another as a mirror later.

From: https://forum.proxmox.com/threads/different-size-disks-for-zfs-raidz-1-root-file-system.22774/


## Wiping ZFS Disk
Wiping last bit of disk to clean an old ZFS disk.

Try `mke2fs /dev/sdx`

If that doesn't work, may need to wipe end of disk:

https://unix.stackexchange.com/questions/13848/wipe-last-1mb-of-a-hard-drive

    dd bs=512 if=/dev/zero of=/dev/sdx count=2048 seek=$((`blockdev --getsz /dev/sdx` - 2048))


## Pool export - import

Clean export:

    zpool export tank10

Import:

    zpool import
    zpool import tank10 -f
    zpool list


`zpool import -a` will scan and try to import stuff.


## Checking properties incl ashift

zdb -C

## Encrypted ZFS

sudo zfs create -o encryption=on -o keylocation=prompt -o keyformat=passphrase tank12/encrypted

sudo zfs mount tank12/encrypted -l

https://pov.es/linux/ubuntu/ubuntu-20-04-install-ubuntu-with-zfs-and-encryption/

## Other things

https://zedfs.com/all-you-have-to-know-about-reading-zfs-disk-usage/