# PVE Build Notes

## Installation

If disks are different sizes, install onto one ZFS disk in RAID 0, and then add another drive.  May need to deep wipe disk to wipe out any traces of a previous ZFS install.

See 

* email-relay.md
* smart.md
* zfs.md


## Other Thigns

* Mount `/tankNN/hyper` in the cluster for VZDump backups
* Set backup schedule for all VMs
* Firewall
