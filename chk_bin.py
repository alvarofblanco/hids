#!/usr/bin/python
import MySQLdb as mariadb
import getpass
import subprocess
import time

#bin files checking

print ('Ingrese la contrasena de la base de datos')
pwd = getpass.getpass()

try:	
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("Error: {}".format(error))


#instanciate the cursor object to start running queries
cursor=mariadb_connection.cursor()

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

	file = open("mail","w")
	file.write("Este mail usted esta recibiendo por la siguiente advertencia de seguridad:\n" + alarm +"\n Y se han tomado las siguentes medidas\n" + prevencion)
	file.close()


