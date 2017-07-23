#!/usr/bin/python

import MySQLdb as mariadb
import getpass
import hashlib
import subprocess
import time
import re
import os
import smtplib


if os.stat("ddos").st_size == 0 :
	print 'El equipo no se encuentra bajo un ataque DDOS'
else:
	#Alarms
	date = time.strftime("%c")
	alarm = '[' + date + '] Alerta! El servidor se encuentra bajo un ataque DDOS \n'
	prevention ='[' + date + '] Se han agregado todas las excepciones en iptables\n'

	#Mail creation
	file = open('mail','w')
	file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarm + "y se han tomado las siguientes medidas: \n" + prevention)	
	file.close()

	#Alarma.log file
	file = open('/var/log/hids/alarmas.log','a')
	file.write(alarm)
	file.close()

	#Prevencion.log file edit
	file = open('/var/log/hids/prevencion.log','a')
	file.write(prevention)
	file.close()
	
	f = open('ddos','r')
	content = f.read()
	line = content.split("\n")
	limit = len(line) - 1
	l = []
	for i in range(limit):
		line = content.split('\n')[i]
		tmp = line.split(' ')[2]
		l.append(tmp)	
	l = list(set(l))
	limit = len (l)
	for i in range(limit):
		tmp = l[i].split('.')
		ip_from = tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+tmp[3]
		port = tmp[4]
		os.system ("iptables -A INPUT -s %s -p TCP --dport %s -j DROP" % (ip_from,port))
		os.system ("service iptables save")
		os.system ("service iptables restart")
	f.close()
