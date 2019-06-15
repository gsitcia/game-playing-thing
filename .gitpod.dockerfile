FROM gitpod/workspace-full:latest
USER root
RUN apt-get update \
    && apt-get install -yq libmpc-dev libmpfr-dev libgmp-dev flex \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
