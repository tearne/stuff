FROM tearne/lxde:6.2.4

ENV NVM https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh

ENV DEBIAN_FRONTEND noninteractive

RUN add-apt-repository ppa:webupd8team/atom \
&&  apt-get update \
&&  apt-get install -y --no-install-recommends \
      chromium-browser \
      atom \
&&  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER user
RUN curl -o- $NVM | bash \
&&  export NVM_DIR="$HOME/.nvm" \
&&  . "$NVM_DIR/nvm.sh" \
&&  . "/home/user/.nvm/nvm.sh" \
&&  nvm install 10 \
&&  npm install http-server -g
USER root
