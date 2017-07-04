#!/usr/bin/python
import MySQLdb as mariadb
import getpass


#varificacion de archivos binarios

print ('Ingrese la contrasena de la base de datos')
pwd = getpass.getpass()

try:
	
	mariadb_conn = mariadb.connect("127.0.0.1", 'root', pwd, 'hids')
except mariadb.Error as error:
	print("Error: {}".format(error))
