apt install --no-install-recommends samba

cp /etc/samba/smb.conf /etc/samba/smb.conf.bk
nano /etc/samba/smb.conf

https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html

Setting sgid on all folders to make sure that new folders inherit the parent group

    find somedir -type d -exec chmod g+s {} \;