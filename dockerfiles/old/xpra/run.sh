#!/bin/bash

if [ -n "${SSH_KEY}" ]; then
	# A public key can be provided at runtime: -e SSH_KEY="$(cat ~/.ssh/id_rsa.pub)"
	# To make a key on the host: ssh-keygen -t rsa -C "me@place.com"

	MYHOME=/home/user
	mkdir -p ${MYHOME}/.ssh
	chmod go-rwx ${MYHOME}/.ssh
	echo "${SSH_KEY}" > ${MYHOME}/.ssh/authorized_keys
	chmod go-rw ${MYHOME}/.ssh/authorized_keys
	chown -R user:user /home/user/.ssh
	echo "=> Added SSH key to ${MYHOME}"

	cat <<EOF
################################################################################
## Set public key
################################################################################
${SSH_KEY}

EOF
fi

_word=$( [ ${PASS} ] && echo "Preset" || echo "Random" )
PASS=${PASS:-$(pwgen -s 6 1)}
echo "user:$PASS" | chpasswd

cat <<EOF
################################################################################
## Connect using key with something like
## xpra attach ssh:user@localhost:100 --ssh="ssh -p 2222 -i ~/.ssh/id_rsa" --opengl=yes --dpi=80
##
## ${_word} password was set for 'user': $PASS
################################################################################

EOF

chown -R user:user /home/user

/sbin/setuser user \
  xpra start :100 \
    --daemon=no \
    --exit-with-children \
    --no-notifications \
    --pulseaudio=no \
		--no-mdns \
		--start-child="$ROOT_APP"
