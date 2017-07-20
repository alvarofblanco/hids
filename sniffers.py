#!/usr/bin/python
import subprocess
import os
import re
import time
import getpass
import MySQLdb as mariadb

#Database connection
print 'Ingrese la contrasena de la base de datos'
pwd = getpass.getpass()
try:
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("ErrorL {}".format(error))

cursor = mariadb_connection.cursor()

#Executes the cmd
cmd = 'ps aux'
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

#Looks through all the process
for i in xrange(2,limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=10)
	
	program = datos[10]
	
	query = "SELECT * FROM sniffers WHERE name = " + program
	cursor.execute(query)
	data = cursor.fetchone()
	
	print data
	raw_input("J3")
	
	