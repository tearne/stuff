# Installing Server
sudo apt install -no-install-recommends samba

In `/etc/samba/smb.conf`, comment out printer stuff.

At the end end:
```
# in section [global]
hosts allow = 192.168.1. 127.0.0.1
hosts deny = ALL

# at bottom of file
[myShare]
path = /tank/myShare
valid users = you me them
guest ok = no
browseable = no
read only = no
```

Run `testparm` to check, then `systemctl restart smbd`

# Creating users
To add a system user without a password `sudo adduser john --disabled-password`.

Add: `sudo smbpasswd -a john`
Update pass: `smbpasswd john`
Delete: `smbpasswd -x john`

https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html

## sgid
Setting sgid on all folders to make sure that new folders inherit the parent group

    find somedir -type d -exec chmod g+s {} \;