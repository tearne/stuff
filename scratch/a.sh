#!/bin/bash
apt-get update \
&& apt-get install --no-install-recommends \
  xfce4 xfce4-goodies tightvncserver \
  firefox \
  tightvncserver
