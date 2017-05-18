FROM ubuntu:14.04
MAINTAINER Alina Nesterova <zemuvier@gmail.com>

RUN apt-get update && apt-get install -y build-essential
RUN apt-get upgrade -y && apt-get update -y
RUN apt-get install -y git

RUN apt-get install -y openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN  mkdir -p /var/run/sshd

RUN apt-get install -y openjdk-7-jdk

RUN apt-get update -y
RUN apt-get install -y lib32z1 && apt-get install -y lib32ncurses5 && apt-get install -y lib32bz2-1.0
RUN apt-get install -y gcc-4.9
RUN apt-get update -y
RUN sudo apt-get install -y libgd2-xpm-dev

RUN adduser --quiet jenkins
RUN echo "jenkins:jenkins" | chpasswd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
