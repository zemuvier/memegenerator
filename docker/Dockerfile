FROM ubuntu:14.04
MAINTAINER Alina Nesterova <zemuvier@gmail.com>
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y lib32z1 && apt-get install -y lib32ncurses5 && apt-get install -y lib32bz2-1.0
RUN apt-get install -y gcc-4.9
ADD libmeme.c /
RUN apt-get update
RUN sudo apt-get install -y libgd2-xpm-dev
RUN gcc -shared -o libmeme.so -fPIC libmeme.c -lgd
EXPOSE 80
