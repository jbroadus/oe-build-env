from ubuntu:18.04

RUN apt-get update -y

RUN apt-get install -y chrpath
RUN apt-get install -y clang
RUN apt-get install -y cpio
RUN apt-get install -y diffstat
RUN apt-get install -y dosfstools
RUN apt-get install -y gcc
RUN apt-get install -y git
RUN apt-get install -y g++
RUN apt-get install -y gawk
RUN apt-get install -y libssl-dev
RUN apt-get install -y llvm
RUN apt-get install -y locales locales-all
RUN apt-get install -y make
RUN apt-get install -y mtools
RUN apt-get install -y parted
RUN apt-get install -y python
RUN apt-get install -y python3
RUN apt-get install -y python3-distutils
RUN apt-get install -y texinfo
RUN apt-get install -y wget

RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN useradd builder

RUN update-alternatives --install /bin/sh sh /bin/bash 100

