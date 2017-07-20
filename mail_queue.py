import subprocess
import os
import time

p = subprocess.Popen([" mailq | tail -n 1"],stdout=subprocess.PIPE,shell=True)
out,err = p.communicate()
tmp = out.split(' ')
tmp = tmp[3]
top_mail = '50'
if tmp is int:
	if int(tmp) > int(top_mail):

        #

		#Alarms
		date = time.strftime("%c")
		alarm = '[' + date + '] Alerta! Se han encontrado mas de 50 mails en la cola\n'
		prevention ='[' + date + '] Se ha avisado al administrador de sistemas\n'
	
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
		os.system('python mail.py')