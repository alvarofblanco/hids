#!/usr/bin/python
import subprocess
import os
import re
import time
import getpass
import MySQLdb as mariadb

#Database connection
print 'Ingrese la contrasena de la base de datos'
pwd = getpass.getpass()
try:
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("ErrorL {}".format(error))

cursor = mariadb_connection.cursor()

#Executes the cmd
cmd = 'ps aux'
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

#Looks through all the process
for i in xrange(2,limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=10)
	
	program = datos[10]
	pid = datos[1]
	
	query = "SELECT * FROM sniffers WHERE name = '" + program+"'"
	cursor.execute(query)
	data = cursor.fetchone()

	if data:
		print "Se encontro un sniffer!"	 
	    
	    #Alarms
		date = time.strftime("%c")
		alarm = '[' + date + '] Alerta! Se encontro un sniffer: ' + program + '\n'
		prevention ='[' + date + '] Se ha terminado el proceso '+program+'\n'
		
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
		
		#Actually does what it says
		cmd = "kill -9 "+pid
		os.system(cmd)
		os.system("python mail.py")
		
