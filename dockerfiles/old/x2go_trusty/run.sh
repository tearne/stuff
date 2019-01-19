#!/bin/bash

sw_vers -productVersion
if [[ $? == 0 ]]; then
  echo "This is OS X, quitting"
  exit;
fi

PASS=${PASS:-$(pwgen -s 6 1)}
echo "=> Setting a $([ ${PASS} ] && echo "user defined" || echo "random") password to the user"
echo "user:$PASS" | chpasswd

echo "========================================================================"
echo " dockerx password : $PASS "
echo "========================================================================"

exec /usr/sbin/sshd -D
