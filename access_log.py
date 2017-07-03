#!/usr/bin/python
import subprocess
import os
import re
import time

#Executes the cmd
cmd = 'tail -n 30 access_log'
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

count = 0

#Looks through all the process
for i in range(limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=25)

	ip = datos[0]
	method = datos[5]
	method = method[1:]
	page = datos[6]
	date = datos[3]
	date_parsed = date[1:12]
	code = datos[8]
	
	print count
	
	#Checks if the line contains a 404 problem
	if '404' in datos:
		#Checks if the ip is the same
		if ip in datos:
			#Checks if the date is the same
			if date in datos[3]:
				count = count + 1

	print count
	if count > 20:
		print "Alerta! Una IP ha intentado ingresar 20 veces a una pagina que no existe"
		count = 0
		
		#Alarms
		date = time.strftime("%c")
		alarm = '[' + date + '] Alerta! La direccion IP ' + ip + ' ha intentado ingresar 20 veces a una pagina que no existe\n'
		prevention ='[' + date + '] Se ha bloquado el ingreso a la IP '+ip+'\n'
		
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
		cmd = 'iptables -A INPUT -s '+ip+' -j DROP'
		os.system(cmd)
		print 'Agregando excepcion a iptables'		
		os.system('service iptables save')
		print 'Reiniciando el servicio iptables'
		os.system('service iptables restart')
		os.system('python mail.py')
		
		count = 0
		break

	if date != datos[3]:
		count = 0	
	
