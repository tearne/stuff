# Use package from testing when on stable.

E.g. to get a newer `snapd`.

Edit `/etc/apt/sources.list` by adding

    deb http://ftp.uk.debian.org/debian testing main contrib non-free

**Don't update yet!**

Change package priorities in `/etc/apt/preferences`

    Explanation: Uninstall or do not install any Debian-originated
    Explanation: package versions other than those in the stable distro
    Package: *
    Pin: release a=stable
    Pin-Priority: 900

    Package: *
    Pin: release o=Debian
    Pin-Priority: -10

Now install package, e.g.

    sudo apt install -t testing snapd


> From: https://wiki.debian.org/AptPreferences