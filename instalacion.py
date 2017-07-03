#!/usr/bin/python
import MySQLdb as mariadb
import getpass
import hashlib

print ("Configurando base de datos")
password = getpass.getpass()

try:
    mariadb_connection = mariadb.connect("localhost",'root','ucacytl3d')
except mariadb.Error as error:
    print("Error: {}".format(error))
    
cursor = mariadb_connection.cursor()

#Creacion de la base de datos
cursor.execute("DROP DATABASE hids")
cursor.execute("CREATE DATABASE hids")
cursor.execute("USE hids")
cursor.execute("CREATE TABLE file_checksum(file_name varchar(40), checksum varchar(1024))")

#Extraccion de los checksum de los archivos binarios del sistema
#Checksum de passwd
checksum = hashlib.md5(open('/etc/passwd', 'rb').read()).hexdigest()
cursor.execute ("INSERT INTO file_checksum VALUES ('passwd', %s)", (checksum,))
#Checksum de shadow
checksum = hashlib.md5(open('/etc/shadow', 'rb').read()).hexdigest()
cursor.execute ("INSERT INTO file_checksum VALUES ('shadow', %s)", (checksum,))
#checksum de group
checksum = hashlib.md5(open("/etc/group", 'rb').read()).hexdigest()
cursor.execute("INSERT INTO file_checksum VALUES('group', %s)", (checksum,))
#checksum de resolv.conf
checksum = hashlib.md5(open("/etc/resolv.conf", 'rb').read()).hexdigest()
cursor.execute("INSERT INTO file_checksum VALUES('resolv', %s)", (checksum,))


mariadb_connection.commit()
cursor.close()
mariadb_connection.close()


#######################CONFIGURACION DE MAIL####################################################
mail = input ('Ingrese su mail: ')
password = getpass.getpass()

fh = open("/var/mail","w")
write(password)
fh.close()


print("Configuracion finalizada")
