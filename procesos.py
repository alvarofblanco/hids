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
		file = open("/var/log/hids/alarmas.log",'aw')
		date = time.strftime("%c")
		file.write('['+ date +'] Alarma: "Proceso '+datos[10]+' con PID '+datos[1]+' consumiendo CPU en exceso"\n')
		file.close()
		file = open("/var/log/hids/prevencion.log",'aw')
		date = time.strftime("%c")
		file.write('['+ date +'] "Proceso '+datos[10]+' terminado"\n')
