FROM gitpod/workspace-full:latest
USER root
RUN apt-get update \
    && apt-get install -yq gcc-arm-linux-gnueabi binutils-arm-linux-gnueabi \
	&& apt-get install -yq libgtk-3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
