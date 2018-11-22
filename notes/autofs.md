# Mounting cifs directly in home dir using autofs

    sudo apt install cifs-utils autofs

Make .smb credentials file

    cat << EOF >> $HOME/.smb
    username=me
    password=secret
    EOF
    chmod 0600 $HOME/.smb

Check `/etc/auto.master` imports the `auto.master.d` directory

Create map in `/etc/auto.master.d`

    sudo sh -c "cat > /etc/auto.master.d/$USER.autofs" <<EOT
    /- $HOME/.autofs --timeout=120 --ghost
    EOT


Make `~/.autofs` in home directory

    cat << EOF >> $HOME/.autofs
    $HOME/share -fstype=cifs,rw,uid=$USER,credentials=$HOME/.smb,file_mode=0770,dir_mode=0770,vers=3.0 ://moo/share
    EOF

Restart autofs
    
    sudo systemctl restart autofs

Make it start automatically

    sudo systemctl enable autofs


# Debugging

    sudo service autofs stop
    sudo automount -f -v


