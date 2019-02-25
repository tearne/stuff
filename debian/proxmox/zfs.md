## Replacing a root ZFS mirror drive

Suppose we have

	NAME                   STATE     READ WRITE CKSUM
	rpool                  DEGRADED     0     0     0
	  mirror-0             DEGRADED     0     0     0
	    sda3               OFFLINE      0     0     0
	    sdb3               ONLINE       0     0     0

and have put in a new drive for sda.  Now:

    sgdisk --replicate=/dev/sda /dev/sdb
    sgdisk --randomize-guids /dev/sda
    grub-install /dev/sda
    zpool replace rpool sda3 /dev/sda3

    or, for adding a disk to a raid-0 mirror with only one disk:

    zpool attach -f rpool /dev/sdb3 /dev/sda3


This is also good for working around the "ZFS mirrored disks must have the same size" problem during first install.  Start with a single RAID0 smallest disk, then `attach` another as a mirror later.

From: https://forum.proxmox.com/threads/different-size-disks-for-zfs-raidz-1-root-file-system.22774/


## Wiping ZFS Disk
Wiping last bit of disk to clean an old ZFS disk
mke2fs /dev/sdx

https://unix.stackexchange.com/questions/13848/wipe-last-1mb-of-a-hard-drive

    dd bs=512 if=/dev/zero of=/dev/sdx count=2048 seek=$((`blockdev --getsz /dev/sdx` - 2048))


## Pool export - import

Clean export:

    zpool export tank10

Import:

    zpool list
    zpool import tank10