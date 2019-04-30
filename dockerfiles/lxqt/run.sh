#!/bin/bash

MYHOME=/home/user

_word=$( [ ${PASS} ] && echo "Preset" || echo "Random" )
PASS=${PASS:-$(pwgen -s 6 1)}
echo "user:$PASS" | chpasswd

cat <<EOF
################################################################################
#      ${_word} password was set for 'user': $PASS
################################################################################

EOF

/etc/NX/nxserver --startup
tail -f /usr/NX/var/log/nxserver.log
