FROM alpine:3.5

RUN apk add --no-cache \
    ca-certificates \
    bash \
    curl \
    rsync \
    openssh-client \
    fuse \
    cifs-utils \
    unzip \
    tmux \
    htop \
    nload \
    ncdu

ENV VERSION=rclone-v1.34-linux-amd64

RUN curl -L -o /tmp/${VERSION}.zip http://downloads.rclone.org/${VERSION}.zip \
&&  cd /tmp \
&&  unzip ${VERSION}.zip \
&&  mv ${VERSION}/rclone /usr/bin \
&&  rm -rf /tmp/${VERSION}*

ENTRYPOINT ["bash"]
