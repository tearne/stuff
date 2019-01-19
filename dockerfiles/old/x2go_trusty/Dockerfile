FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
&&  apt-get -y upgrade \
&&  apt-get install -y software-properties-common \
&&  add-apt-repository ppa:x2go/stable \
&&  add-apt-repository ppa:git-core/ppa \
&&  add-apt-repository ppa:openjdk-r/ppa \
&&  apt-get update \
&&  apt-get install -y --no-install-recommends \
        curl wget aria2 \
        sudo \
        openssh-server x2goserver x2golxdebindings \
        lxde \
        vim tmux \
        git \
        htop \
        openjdk-8-jdk \
&&  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i "s|id=lxde-x-www-browser.desktop|id=/usr/share/applications/lxterminal.desktop|g" /usr/share/lxpanel/profile/LXDE/panels/panel

RUN adduser --disabled-password --gecos "" user \
&&  adduser user sudo

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
&&  sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \
&&  sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config \
&&  sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config

RUN su - user -c 'git clone https://github.com/tearne/dotfiles.git'

COPY run.sh /run.sh
RUN chmod +x run.sh

EXPOSE 22

CMD ["/run.sh"]
