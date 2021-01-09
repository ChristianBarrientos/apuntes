#! /bin/bash
##Install Docker inm Debian 10 amd64
apt update; apt upgrade -y
apt-get remove docker docker-engine docker.io containerd runc -y
apt-get install     apt-transport-https     ca-certificates     curl     gnupg-agent     software-properties-common -y
curl -fsSL https://download.docker.com/linux/debian/gpg |  apt-key add -
apt-key fingerprint 0EBFCD88
#lsb_release -cs
add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io -y
curl -L https://github.com/docker/compose/releases/download/1.25.3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
