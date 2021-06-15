

# mount

    sudo apt install cifs-utils

    sudo mount //server/share /mount/point -o username=me,vers=3,uid=me

# fstab

    sudo apt install cifs-utils autofs

In `/etc/fstab`

    //server/share /media/share  cifs credentials=/home/me/.smb,iocharset=utf8,users,uid=me,vers=3.0  0 0

# autofs

    sudo apt install cifs-utils autofs

Make .smb credentials file

```
cat << EOF >> $HOME/.smb
username=me
password=secret
EOF
chmod 0600 $HOME/.smb
```

Create map in `/etc/auto.master.d`

```
sudo mkdir -p /etc/auto.master.d
sudo sh -c "cat > /etc/auto.master.d/$USER.autofs" <<EOT
/- $HOME/.autofs --timeout=120 --ghost
EOT
```

Make `~/.autofs` in home directory

```
cat << EOF >> $HOME/.autofs
$HOME/share -fstype=cifs,rw,uid=$USER,credentials=$HOME/.smb,file_mode=0770,dir_mode=0770,vers=3.0 ://server/share
EOF
chmod 0600 $HOME/.autofs
```

Restart autofs
    
    sudo systemctl restart autofs

Make it start automatically

    sudo systemctl enable autofs


## Debugging

    sudo systemctl stop autofs
    sudo automount -f -v


