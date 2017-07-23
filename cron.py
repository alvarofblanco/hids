#!/usr/bin/python

import time
import os
#import MySQLdb as mariadb
import getpass
import subprocess
import re

#checks for malicious scripts in the cron folder
'''
#Database connection
print 'Ingrese la contrasena de la base de datos'
pwd = getpass.getpass()
try:
	mariadb_connection = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("ErrorL {}".format(error))

cursor = mariadb_connection.cursor()
'''
#Executes the cmd
cmd = "cat /etc/crond"
proc = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

#Parse the output
ps = out.split('\n')
limit = len(ps)-1

#Looks through all the process
for i in range(limit):
	#Parse each line of the output
	datos = re.compile('\s+').split(ps[i], maxsplit=11)
	
	print datos