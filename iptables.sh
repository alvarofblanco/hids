#!/bin/bash

#Flush de las reglas actuales
iptables -F

#Establecer las politicas por defecto
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

#permitir acceso localhost
iptables -A INPUT -i lo -j ACCEPT

#aceptar paquetes de conexiones
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

#ssh
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

#http y https
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

#permitir ping
iptables -A INPUT -i enp0s3 -p ICMP -j ACCEPT