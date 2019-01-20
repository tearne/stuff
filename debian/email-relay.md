
# Email Relay (postfix)
_Tested on Proxmox_

Install the authentication library:

    apt install libsasl2-modules

Make a password file `/etc/postfix/sasl_passwd` containing login details:

    smtp.gmail.com me@gmail.com:password

Save and protect password file:

    chmod 600 /etc/postfix/sasl_passwd

Create a database from the password file:

    postmap hash:/etc/postfix/sasl_passwd

Add/change lines in `/etc/postfix/main.cf`:

    # Set gmail as relay
    relayhost = smtp.gmail.com:587

    smtp_use_tls = yes
    smtp_sasl_auth_enable = yes
   
    # Eliminates default security options which are imcompatible with gmail
    smtp_sasl_security_options = noanonymous
    smtp_sasl_mechanism_filter = plain
    
    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt

Reload config:

    service postfix restart

Test:

    echo "test message" | mail -s "test subject" me@gmail.com

## Debug
In `/etc/postfix/main/cf`:

    #debug_peer_list = smtp.gmail.com
    #debug_peer_level = 3

# Root email forwarding

For some reason it didn't work out of the box.  Run `newaliases` to build `/etc/aliases.db`.

Test:

    echo "test message" | mail -s "test subject" root

https://forum.proxmox.com/threads/should-root-email-alias-be-configure.48386/

## Related
* https://forum.proxmox.com/threads/how-to-use-google-apps-smtp-to-email-warnings.38236/
* https://www.reddit.com/r/homelab/comments/8c09pr/guide_to_setting_up_zed_to_email_alerts_for_zfs/
