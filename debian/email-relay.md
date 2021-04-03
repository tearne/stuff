# GMail Email Relay

Authentication library:

    apt install libsasl2-modules

On Ubuntu also install `postfix` and `mail` (required for using postmap).

Make **temporary** password file `/etc/postfix/sasl_passwd` containing login details:

    smtp.gmail.com someone@somewhere.com:[API-password]

Save and protect password file:

    chmod 600 /etc/postfix/sasl_passwd

Create a database from the password file:

    postmap hash:/etc/postfix/sasl_passwd

Delete temporary file `/etc/postfix/sasl_passwd`

Add/change lines in `/etc/postfix/main.cf`:

    # Set gmail as relay
    relayhost = smtp.gmail.com:587

    smtp_use_tls = yes
    smtp_sasl_auth_enable = yes
   
    # Eliminates default security options which are incompatible with gmail
    smtp_sasl_security_options = noanonymous
    smtp_sasl_mechanism_filter = plain
    
    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt

Reload config:

    systemctl restart postfix

Test:

    printf "$(date)" | mail -s "$USER at $HOSTNAME" [me@place.com]

Test if forwarding root works with (if not see fix below):

    printf "Via root mailbox\n$(date)" | mail -s "$USER at $HOSTNAME via root" root

https://forum.proxmox.com/threads/how-to-use-google-apps-smtp-to-email-warnings.38236/

## Forwarding root

Edit `/etc/aliases` to append

    root: [me@place.com]

Then
* sudo newalises 
* sudo systemctl restart postfix

## Debugging
In `/etc/postfix/main/cf`:

    #debug_peer_list = smtp.gmail.com
    #debug_peer_level = 3

Logs go to `/var/log/mail.log`.

## Related
* https://pve.proxmox.com/wiki/ZFS_on_Linux#_activate_e_mail_notification