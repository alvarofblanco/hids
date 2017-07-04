#!/usr/bin/python
import subprocess
import os
import re
import time

MAX="075.0"
proc = subprocess.Popen('ps aux',shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()
ps = out.split('\n')
limit = len(ps)-1
for i in range(limit):
	datos = re.compile('\s+').split(ps[i], maxsplit=11)
	pid = datos[1]
	cpu = datos[2]
	ram = datos[3]
	if cpu > MAX:
		print "Alarma: Proceso %s consumiendo CPU en exceso" % datos[10]
		os.system("kill -9 "+datos[1])
		file = open("alarmas.log",'a')
		date = time.strftime("%c")
		alarma = '['+ date +'] Alarma: "Proceso '+datos[10]+' con PID '+datos[1]+' consumiendo CPU en exceso"\n'
		file.write(alarma)
		file.close()
		file = open("prevencion.log",'a')
		date = time.strftime("%c")
		prevencion = '['+ date +'] "Proceso '+datos[10]+' terminado"\n'
		file.write(prevencion)
		file = open("mail","w")
		file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarma + "y se han tomado las siguientes medidas: \n" + prevencion)
		file.close()
		os.system("python mail.py")
		
	if ram > MAX:
		print "Alarma: Proceso %s consumiendo RAM en exceso" % datos[10]
		os.system("kill -9 "+datos[1])
		file = open("alarmas.log",'a')
		date = time.strftime("%c")
		alarma = '['+ date +'] Alarma: "Proceso '+datos[10]+' con PID '+datos[1]+' consumiendo RAM en exceso"\n'
		file.write(alarma)
		file.close()
		file = open("prevencion.log",'a')
		date = time.strftime("%c")
		prevencion = '['+ date +'] "Proceso '+datos[10]+' terminado"\n'
		file.write(prevencion)
		file = open("mail","w")
		file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarma + "y se han tomado las siguientes medidas: \n" + prevencion)
		file.close()
		os.system("python mail.py")
		
