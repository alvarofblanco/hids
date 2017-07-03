#!/usr/bin/python
import subprocess
import os
import re
import time

#Executes the cmd
cmd = 'tail -n 50 secure'
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

count = 0

#Looks through all the process
for i in range(limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=15)
	#print datos

	date = datos[0] +" "+ datos[1]
	ts = date + " " +datos[2]
	access = datos[14]
	access = access.split("=")
	user = access[1]

	#Checks if the line contains 
	if 'failure;' in datos and 'authentication' in datos:
		if user in datos[14]:
			if datos[0] +" "+ datos[1] == date:
				
				count += 1

	if count > 10:
		print "Alerta! Un usuario ha ingresado mal mas de 10 veces su contrasena"
		count = 0
		
		#Alarms
		date = time.strftime("%c")
		alarm = '[' + date + '] Alerta! El usuario ' + user + ' ha ingresado mal 10 veces su contrasena\n'
		prevention ='[' + date + '] Se ha bloquado el ingreso al usuario '+user+'\n'
		
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
		cmd = "passwd -l "+user
		os.system(cmd)
		os.system("python mail.py")
		
		count = 0
		break
	
	if date != datos[0] +" "+ datos[1]:
		count = 0	
	
