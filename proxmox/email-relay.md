
# Email relay setup on Proxmox VE

Install the authentication library:

    apt install libsasl2-modules

Make a password file `/etc/postfix/sasl_passwd` containing login details:

    smtp.gmail.com me@gmail.com:password

Save and protect password file:

    chmod 600 /etc/postfix/sasl_passwd

Create a database from the password file:

    postmap hash:/etc/postfix/sasl_passwd

Add/change lines in `/etc/postfix/main/cf`:

    relayhost = smtp.gmail.com:587
    smtp_use_tls = yes
    smtp_sasl_auth_enable = yes
    # Eliminate defaults which are incompatible with gmail
    smtp_sasl_security_options =
    smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
    smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt

Reload the updated configuration:

    service postfix restart

Test:

    echo "test message" | mail -s "test subject" me@gmail.com


## Sources:
Based on:
* https://pve.proxmox.com/wiki/Package_Repositories
* https://forum.proxmox.com/threads/how-to-use-google-apps-smtp-to-email-warnings.38236/
