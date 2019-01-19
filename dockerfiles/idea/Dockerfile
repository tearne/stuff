FROM tearne/dev

ENV PATH="$HOME/bin:$PATH"

RUN VER=ideaIC-2016.3 \
&&  mkdir -p /home/user/bin/$VER \
&&  curl -L https://download.jetbrains.com/idea/$VER.tar.gz | tar xz --strip 1 --directory /home/user/bin/$VER \
&&  ln -s /home/user/bin/$VER/bin/idea.sh /home/user/bin/idea \
&&  chown user:user -R /home/user/bin
