FROM ubuntu:14.04
MAINTAINER Alina Nesterova <zemuvier@gmail.com>

RUN apt-get update && apt-get install -y build-essential
RUN apt-get upgrade -y && apt-get update -y
RUN apt-get install -y git && apt-get install -y unzip

RUN apt-get install -y openssh-server
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN  mkdir -p /var/run/sshd

RUN apt-get install -y openjdk-7-jdk

RUN wget http://www.web2py.com/examples/static/web2py_src.zip
RUN unzip web2py_src.zip && cd web2py

RUN apt-get update
RUN apt-get install -y curl
RUN curl -L https://www.opscode.com/chef/install.sh | bash

RUN adduser --quiet jenkins_deploy
RUN echo "jenkins_deploy:jenkins" | chpasswd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

