#!/usr/bin/python
import MySQLdb as mariadb
import getpass

print ("Configurando base de datos")
password = getpass.getpass()

try:
    mariadb_connection = mariadb.connect("localhost",'root',password)
except mariadb.Error as error:
    print("Error: {}".format(error))
    
cursor = mariadb_connection.cursor()

#Creacion de la base de datos