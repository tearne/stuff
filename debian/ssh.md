## Host fingerprints
### SSH client

    ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub -E sha256

### Cyberduck client

    ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub -E md5

or

    ssh-keyscan localhost > localhost.ssh-keyscan
    ssh-keygen -lf localhost.ssh-keyscan -E md5

or

    ssh-keygen -r localhost

## Remote port forwarding

Port 9000 on remote machine mapping to port 22 on mine:

    ssh -R 9000:localhost:22 me@remote

On remote destination put this at the end of file

    Match User me
      GatewayPorts yes

https://askubuntu.com/questions/50064/reverse-port-tunnelling#50075

## Intermediate jump host

    ssh -J me@intermediate:1234 me@destination -p 5678


