#!/usr/bin/python

import time
import os
import MySQLdb as mariadb
import getpass
import subprocess
import re

#checks for malicious scripts in the cron folder

#Database connection
print 'Ingrese la contrasena de la base de datos'
pwd = getpass.getpass()
try:
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("ErrorL {}".format(error))

cursor = mariadb_connection.cursor()

#Executes the cmd
cmd = "cat /etc/crontab"
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

#Looks through all the process
for i in xrange(4,limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=7)
	
	user = datos[5]
	script = datos[6]
	
	query = "SELECT * FROM cron WHERE name = \'" + script + "\';"
	#print query
	cursor.execute(query)
	data = cursor.fetchone()
	if not data:
		print "Script sospechoso detectado!"
		#Alarms
		date = time.strftime("%c")
		alarm = '[' + date + '] Alerta! Se encontro el siguiente script en la configuracion de cron: ' + script + '\n'
		prevention ='[' + date + '] Se ha movido el script a la carpeta /var/log/hids/vault \n'
		
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
		cmd = "mv " + script + " /var/log/hids/vault"
		os.system(cmd)
		os.system("python mail.py")
