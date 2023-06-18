#!/usr/bin/env python3
import util
import cargo


def main(password):


def install_helix(password):
	util.sudo("add-apt-repository ppa:maveonair/helix-editor",password)
	util.sudo("apt update",password)
	util.sudo("apt install helix",password)


if __name__ == "__main__"
    main(util.Password())



todo
* zellij
* helix
* broot
