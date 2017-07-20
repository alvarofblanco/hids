#!/usr/bin/python
import subprocess
import os
import re
import time

#check if the interface is on promisc mode

#Executes the cmd

#set the if in promis mode
#ip link set eth0 promisc on

cmd = 'netstat -i'
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

for i in xrange(2,limit):
    datos = re.compile('\s+').split(ps[i], maxsplit=11)
    interface = datos [0]
    flag = datos[11]
    
    if "P" in flag:
        #Interface is in promisc mode
        
        #Alarm
        print "Alarma: Interfaz %s en modo promiscuo." % interface
        
        #Prevention
        cmd = "ip link set %s promisc off" % interface
        print cmd
        #os.system(cmd)
        
        #Saves the alarm in the log file
        file = open("alarmas.log",'a')
        date = time.strftime("%c")
        alarma = '['+ date +'] Alarma: "Proceso '+datos[10]+' con PID '+datos[1]+' consumiendo CPU en exceso"\n'
        file.write(alarma)
        file.close
        
        #Saves the prevention in the prevention log
        file = open("prevention.log","a")
        date = time.strftime("%c")
        prevention = '[' + date + '] Apagadi el modo promiscuo de la interfaz '+interface+'\n'
        file.write(alarma)
        file.close()
        
        #Creates the mail to be sended
        file = open("mail","w")
        file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad: \n" + alarma + "y se han tomado las siguientes medidas: \n" + prevention)
        file.close()
        #os.system("python mail.py")
        