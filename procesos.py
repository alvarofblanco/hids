#!/usr/bin/python
import subprocess
import os
import re
import time

#Max amount of RAM or CPU that a process can use
MAX="075.0"

#Executes the cmd
cmd = 'ps aux'
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

#Looks through all the process
for i in range(limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=11)
	pid = datos[1]
	cpu = datos[2]
	ram = datos[3]
	
	#Agregar un select de db para ver si el proceso tiene permitido usar tantos recursos
	
	#Checks if the cpu used by the process is higher than MAX
	if cpu > MAX:
		#Alarm
		print "Alarma: Proceso %s consumiendo CPU en exceso" % datos[10]
		
		#Prevention. Kills the process
		os.system("kill -9 "+datos[1])
		
		#Saves tha alarm in the alarm log file
		file = open("/var/log/hids/alarmas.log",'a')
		date = time.strftime("%c")
		alarma = '['+ date +'] Alarma: "Proceso '+datos[10]+' con PID '+datos[1]+' consumiendo CPU en exceso"\n'
		file.write(alarma)
		file.close()
		
		#Saves the prevention in the prevention log file
		file = open("/var/log/hids/procesos.log",'a')
		date = time.strftime("%c")
		prevencion = '['+ date +'] "Proceso '+datos[10]+' terminado"\n'
		file.write(prevencion)
		file.close()
		
		#Creates the mail to be sended
		file = open("mail","w")
		file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarma + "y se han tomado las siguientes medidas: \n" + prevencion)
		file.close()
		os.system("python mail.py")
		
	if ram > MAX:
		#Alarm
		print "Alarma: Proceso %s consumiendo RAM en exceso" % datos[10]
		
		#Prevention
		os.system("kill -9 "+datos[1])
		
		#Saves tha alarm in the alarm log file
		file = open("alarmas.log",'a')
		date = time.strftime("%c")
		alarma = '['+ date +'] Alarma: "Proceso '+datos[10]+' con PID '+datos[1]+' consumiendo RAM en exceso"\n'
		file.write(alarma)
		file.close()
		
		#Saves the prevention in the prevention log file
		file = open("prevencion.log",'a')
		date = time.strftime("%c")
		prevencion = '['+ date +'] "Proceso '+datos[10]+' terminado"\n'
		file.write(prevencion)
		file.close()
		
		#Creates the mail to be sended
		file = open("mail","w")
		file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarma + "y se han tomado las siguientes medidas: \n" + prevencion)
		file.close()
		os.system("python mail.py")
		
