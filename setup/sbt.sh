#!/bin/bash
DIR='sbt-0.13.11' 
mkdir -p ~/bin/$DIR
curl -L https://dl.bintray.com/sbt/native-packages/sbt/0.13.11/sbt-0.13.11.tgz | tar xz --strip 1 --directory ~/bin/$DIR
ln -s ~/bin/$DIR/bin/sbt ~/bin/sbt