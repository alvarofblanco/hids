#!/usr/bin/python

import subprocess
import os
import re
import time
import getpass
import MySQLdb as mariadb

#Modulo de deteccion de usuarios conectados. Revisa los usuarios conectados por medio
#De la instruccion who -aH. Si alguno de esos es pts y no esta en la lista de usuarios permitidos, cancela la conexion y agrega una excepcion a la iptables


#Database connection
print 'Ingrese la contrasena de la base de datos'
pwd = getpass.getpass()
try:
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("ErrorL {}".format(error))

cursor = mariadb_connection.cursor()



#Executes who command and parse the output 
exe = 'who'
p = subprocess.Popen(exe,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = p.communicate()
response = out.split('\n')


#Check each line of the output
for i in range(len(response)-1):
	#convert each line of the output in a list
	line = re.compile('\s+').split(response[i], 5)
	#print line
	#print len(line)
	
	#if the line has 5 arguments (ip included)
	if len(line) == 5:
	
		ip = line[4].replace('(','')
		ip = ip.replace(')','')
		
		#PRUEBA
		#ip = '192.168.1.110'

		query = 'select * from user_ip where ip = \'' + ip + '\''
		#print query
		cursor.execute(query)
		data = cursor.fetchone()
		if not data:
			
			#Usuario extrano econtrado
			
		
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
			print alarm
			print prevention
			cmd = 'iptables -A INPUT -s '+ip+' -p tcp -m tcp --dport 22 -j REJECT'
			os.system(cmd)
			print 'Agregando excepcion a iptables'		
			os.system('service iptables save')
			print 'Reiniciando el servicio iptables'
			os.system('service iptables restart')
			os.system('python mail.py')
	
