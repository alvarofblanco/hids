#!/usr/bin/python

import os
import re
import MySQLdb as mariadb

#Modulo de deteccion de usuarios conectados. Revisa los usuarios conectados por medio
#De la instruccion who -aH. Si alguno de esos es pts y no esta en la lista de usuarios permitidos, cancela la coneccion y agrega una excepcion a la iptables
