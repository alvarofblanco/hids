#!/usr/bin/python
import MySQLdb as mariadb
import getpass
import subprocess
import time
import os

#bin files checking

print ('Ingrese la contrasena de la base de datos')
pwd = getpass.getpass()

try:	
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("Error: {}".format(error))


#instanciate the cursor object to start running queries
cursor=mariadb_connection.cursor()

###################################################### PASSWD ######################################################
	#Check passwd sign

#Runs a bash command
cmd = "md5sum /etc/passwd | awk '{print $1}'"
process = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = process.communicate()
out = out.split('\n')

#BRINGS THE PASSWD MD5SUM SIGNATURE FROM THE DATABASE
query = "SELECT checksum FROM file_checksum WHERE file_name = 'passwd'"
cursor.execute(query)
response = cursor.fetchone()

#checks if the signatures dismatch
if response[0] != out[0] :
	#print ("No es igual")
	#Writes the alarm log file
	date = time.strftime("%c")
	alarm = '[' + date + '] Alarma! El archivo passwd ha sido modificado\n'
	print alarm
	file = open("/var/log/hids/alarmas.log","a")
	file.write(alarm)
	file.close()

	#writes in the prevencion.log file
	prevencion = '[' + date + '] Aviso mediante mail al administrador\n'
	file = open("/var/log/hids/prevencion.log","a")
	file.write(prevencion)
	file.close()

	#writes the body of the mail
	file = open("mail","w")
	file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad:\n" + alarm +"\n Y se han tomado las siguentes medidas\n" + prevencion)
	file.close()
	
	#sends the mail
	#os.system("python mail.py")
	
	
###################################################### SHADOW ######################################################
#Runs a bash command to retrieve the signature of the shadow file
cmd = "md5sum /etc/shadow | awk '{print $1}'"
process = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = process.communicate()
out = out.split('\n')

#BRINGS THE SHADOW MD5SUM SIGNATURE FROM THE DATABASE
query = "SELECT checksum FROM file_checksum WHERE file_name = 'shadow'"
cursor.execute(query)
response = cursor.fetchone()

#checks if the signatures dismatch
if response[0] != out[0] :
	#print ("No es igual")
	#Writes the alarm log file
	date = time.strftime("%c")
	alarm = '[' + date + '] Alarma! El archivo shadow ha sido modificado\n'
	print alarm
	file = open("/var/log/hids/alarmas.log","a")
	file.write(alarm)
	file.close()

	#writes in the prevencion.log file
	prevencion = '[' + date + '] Aviso mediante mail al administrador\n'
	file = open("/var/log/hids/prevencion.log","a")
	file.write(prevencion)
	file.close()

	#writes the body of the mail
	file = open("mail","w")
	file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad:\n" + alarm +"\n Y se han tomado las siguentes medidas\n" + prevencion)
	file.close()
	
	#sends the mail
	#os.system("python mail.py")
	
############################################GROUP################################################################################
	#Runs a bash command to retrieve the signature of the group file
cmd = "md5sum /etc/group | awk '{print $1}'"
process = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = process.communicate()
out = out.split('\n')

#BRINGS THE SHADOW MD5SUM SIGNATURE FROM THE DATABASE
query = "SELECT checksum FROM file_checksum WHERE file_name = 'group'"
cursor.execute(query)
response = cursor.fetchone()

#checks if the signatures dismatch
if response[0] != out[0] :
	#print ("No es igual")
	#Writes the alarm log file
	date = time.strftime("%c")
	alarm = '[' + date + '] Alarma! El archivo group ha sido modificado\n'
	print alarm
	file = open("/var/log/hids/alarmas.log","a")
	file.write(alarm)
	file.close()

	#writes in the prevencion.log file
	prevencion = '[' + date + '] Aviso mediante mail al administrador\n'
	file = open("/var/log/hids/prevencion.log","a")
	file.write(prevencion)
	file.close()

	#writes the body of the mail
	file = open("mail","w")
	file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad:\n" + alarm +"\n Y se han tomado las siguentes medidas\n" + prevencion)
	file.close()
	
	#sends the mail
	#os.system("python mail.py")



	
############################################RESOLV################################################################################
	#Runs a bash command to retrieve the signature of the resolv file
cmd = "md5sum /etc/resolv | awk '{print $1}'"
process = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = process.communicate()
out = out.split('\n')

#BRINGS THE SHADOW MD5SUM SIGNATURE FROM THE DATABASE
query = "SELECT checksum FROM file_checksum WHERE file_name = 'resolv'"
cursor.execute(query)
response = cursor.fetchone()

#checks if the signatures dismatch
if response[0] != out[0] :
	#print ("No es igual")
	#Writes the alarm log file
	date = time.strftime("%c")
	alarm = '[' + date + '] Alarma! El archivo resolv ha sido modificado\n'
	print alarm
	file = open("/var/log/hids/alarmas.log","a")
	file.write(alarm)
	file.close()

	#writes in the prevencion.log file
	prevencion = '[' + date + '] Aviso mediante mail al administrador\n'
	file = open("/var/log/hids/prevencion.log","a")
	file.write(prevencion)
	file.close()

	#writes the body of the mail
	file = open("mail","w")
	file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad:\n" + alarm +"\n Y se han tomado las siguentes medidas\n" + prevencion)
	file.close()
	
	#sends the mail
	#os.system("python mail.py")

