#1/bin/bash
DIR=scala-SDK-4.4.1-vfinal-2.11-linux.gtk.x86_64
mkdir -p ~/bin/$DIR
curl -L http://downloads.typesafe.com/scalaide-pack/4.4.1-vfinal-luna-211-20160504/scala-SDK-4.4.1-vfinal-2.11-linux.gtk.x86_64.tar.gz | tar xz --strip 1 --directory ~/bin/$DIR
ln -s ~/bin/$DIR/eclipse ~/bin/eclipse