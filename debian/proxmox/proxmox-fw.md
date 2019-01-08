# PVE Firewall


Security Groups with rules:
* **Direction**: IN
* **Action**: ACCEPT
* **Protocol**: TCP
* **Source**: 192.168.1.0/24
* **Dest. port**
  * 3128 (spice proxy)
  * 22 (ssh cluster actions)
  * 111 (rcpbind)
  * 85 (pvedaemon - listens on 127.0.0.1  only)
  * 5900:5999 (VMC web console)
  * 8006 (Web interface)

One more rule
* **Direction**: IN
* **Action**: ACCEPT
* **Protocol**: **UDP**
* **Source**: 192.168.1.0/24
* **Dest Port**: 5404:5405 (corosync cluster multicast)

Add new security group to Datacenter firewall and enable.

Enable firewall on node(s) to make rules propagate down.

## Relevant

* https://pve.proxmox.com/wiki/Ports
* https://www.kiloroot.com/secure-proxmox-install-sudo-firewall-with-ipv6-and-more-how-to-configure-from-start-to-finish/