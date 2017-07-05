#!/usr/bin/python

import subprocess
import os
import re
#import MySQLdb as mariadb

#Modulo de deteccion de usuarios conectados. Revisa los usuarios conectados por medio
#De la instruccion who -aH. Si alguno de esos es pts y no esta en la lista de usuarios permitidos, cancela la coneccion y agrega una excepcion a la iptables

exe = 'who -aH'
p = subprocess.Popen(exe,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = p.communicate()
list_users = out.split('\n')

print list_users