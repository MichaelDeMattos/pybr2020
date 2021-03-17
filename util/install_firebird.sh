#!/usr/bin/bash

#Instalação do firebird no linux

apt update
apt upgrade -y

#Colocar na lista de repositorio source.list
echo "deb http://security.debian.org/debian-security jessie/updates main contrib non-free" >> /etc/apt/sources.list

apt update

#Instalar o firebird
apt install firebird2.5-superclassic -y

#Cria o diretório base
#mkdir your_path

#Dar permissão ao usuário de banco de dados no diretório 
#chown -R firebird:firebird your_path/

#Dar permissao ao banco de dados
#chown -R firebird:firebird database.fdb

#admin banco de dados
#apt install flamerobin

#liberar portas no servidor: 
#sudo iptables -A INPUT -p tcp --dport 3050 -j ACCEPT
#sudo iptables -A OUTPUT -p tcp --dport 3050 -j ACCEPT

#criando banco de dados
#/usr/bin/isqlfb
#CREATE DATABASE '/your_path/database.fdb' user 'SYSDBA' password 'masterkey';
