#!/usr/bin/python

import subprocess
import os
import re
import time
#import MySQLdb as mariadb

#Modulo de deteccion de usuarios conectados. Revisa los usuarios conectados por medio
#De la instruccion who -aH. Si alguno de esos es pts y no esta en la lista de usuarios permitidos, cancela la coneccion y agrega una excepcion a la iptables

#Ejecuta el commando who y convierte la salida en cadenas de caracteres 
exe = 'who -a'
p = subprocess.Popen(exe,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = p.communicate()
response = out.split('\n')

for i in range(len(response)-1):
	line = re.compile('\s+').split(response[i], 7)
	#print line
	
	#Checks if the second value of the string is pseudo terminal slave probably with ssh
	if line[2].startswith('pts'):
		#String parsing
		ip = line[7].replace('(','')
		ip = ip.replace(')','')
		pid = line[6]
		
		
		#Alarms
		date = time.strftime("%c")
		alarm = '[' + date + '] Alerta! Conexion remota desde ' + ip + '\n'
		prevention ='[' + date + '] Se a agregado esa exepcion de la ip '+ip+' en iptables\n'
		
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

		#Actually does what it says it has done
		cmd = 'iptables -A INPUT -s '+ip+' -p tcp -m tcp --dport 22 -j REJECT'
		#os.system(cmd)
		#os.system('service iptables save')
		#os.system('service iptables restart')

		
