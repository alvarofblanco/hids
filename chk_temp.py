#!/usr/bin/python

import time
import os

listdir = os.listdir('/tmp')
flag = 0



for i in listdir:
    path = '/tmp/' + i
    #print path
    if os.path.isfile(path):
        file = open(path,"r")
        line = file.readline()
        file.close()
        #print line
        if line.startswith('#!'):
            #Warning
            print "Se ha encontrado un script en la carpeta /tmp"
            print "Se ha borrado el archivo por motivos de seguridad"
            #Prevention
            os.system("rm -rf /tmp/"+i)

            #Creates the strings for the log files and mail
            date = time.strftime("%c")
            alarm = '['+ date +'] Alarma: Se ha encontrado un script con nombre '+i+' en la carpeta /tmp\n'
            prevention = '['+ date +'] Archivo ' +i+ ' eliminado\n'

            #writes the alarms log file
            file = open("/var/log/alarmas.log","a")
            file.write(alarm)
            file.close()

            #writes the prevetion log file
            file = open("/var/log/prevencion.log","a")
            file.write(prevention)
            file.close()

            #writes the mail
            file = open("mail","w")
            file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarm + "y se han tomado las siguientes medidas: \n" + prevention)
            file.close()

            #sends the mail
            os.system("python mail.py")
            flag = 1
if flag == 0:
    print "No hay ningun script en el directorio /tmp"

