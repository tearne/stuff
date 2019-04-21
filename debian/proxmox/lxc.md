# LXC

Container config in `/etc/pve/lxc/NNN.conf`/

## UID / GID Mapping

### Default
To check what root in an `unprivileged` container maps to on the host:

    # cat /etc/subuid
    root:100000:65536
    
    # cat /etc/subgid
    root:100000:65536

https://pve.proxmox.com/wiki/Unprivileged_LXC_containers

### Configuring
This configuration will map both user and group ids in the range 0-9999 in the container to the ids 100000-109999 on the host.

    lxc.idmap = u 0 100000 1000
    lxc.idmap = g 0 100000 10000

https://linuxcontainers.org/lxc/manpages/man5/lxc.container.conf.5.html

## Bind Mounts

In container config:

    mp0: /tank/myShare,mp=/share

## Tmux

`tmux` doesnt work in Proxmox VE LXC Debian images because of locale:

    tmux: need UTF-8 locale (LC_CTYPE) but have ANSI_X3.4-1968`)

1. Uncomment `en_GB.UTF-8 UTF-8` in `/etc/locale.gen`
2. Set `LANG="en_GB.UTF-8"` in `/etc/default/locale`
3. Run `locale-gen`

Another way to do the same thing?:

    apt install locales
    dpkg-reconfigure locales