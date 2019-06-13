FROM gitpod/workspace-full:latest
USER root
RUN apt-get update \
    && apt-get install -yq gcc-arm-linux-gnueabi binutils-arm-linux-gnueabi \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
