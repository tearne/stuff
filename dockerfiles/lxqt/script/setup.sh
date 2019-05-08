#!/bin/bash

mkdir $HOME/bin

cat << EOF >> ~/.bashrc
# put ~/bin first on PATH
if [ -d "$HOME/bin" ]; then
    PATH="$HOME/bin:$PATH"
fi
EOF
