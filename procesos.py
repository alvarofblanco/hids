#!/usr/bin/python
import subprocess
import os
import re
import time

MAX="75.0"
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
		f = open("/var/log/hids/alarmas.log",'a')
		date = time.strftime("%c")
		f.write('['+ date +'] Alarma: Proceso '+proc+' con PID '+pid+' consumiendo RAM en exceso\n')
		f.close()
		f = open("/var/log/hids/prevencion.log",'a')
		f.write('['+ date +'] Proceso '+proc+' terminado por alto consumo de RAM\n')
		f.close()
		message = 'Proceso consumiendo RAM en exceso detectado. Por prevencion fue terminado.'

        #os.system("kill -9 "+pid)
        continue
