#!/usr/bin/python
import MySQLdb as mariadb
import getpass
import hashlib
import os

#Create config files

#Create configuration folder
if not os.path.exists("/etc/hids"):
    os.makedirs("/var/hids")

#Crete the log files
os.system("touch /var/log/hids/alarmas.log")
os.system("touch /var/log/hids/prevencion.log")

#Crete the sniffers files
f = open('/etc/hids/sniffers.hids')
f.write("tshark,john,kismet,tcpdump,dsniff,ettercap,ngrep,topng,snort")
f.close()

#Crete the users files
f = open('/etc/hids/users.hids')
nombre = raw_input("Inserte el nombre")

while nombre != 0:
    ip = raw_input("Inserte la direccion IP")
    line = nombre + ',' +ip
    f.write(line)
    nombre = raw_input("Inserte el nombre")
    



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
cursor.execute("CREATE TABLE user_ip(username varchar(40), ip varchar(15))")
cursor.execute("CREATE TABLE sniffers(name varchar(40))")

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

#entering the users
cursor.execute("LOAD DATA LOCAL INFILE '/etc/hids/users.hids' INTO TABLE user_ip FIELDS TERMINATED BY ','")

#entering the sniffers
cursor.execute("LOAD DATA LOCAL INFILE '/etc/hids/sniffers.hids' INTO TABLE user_ip FIELDS TERMINATED BY ','")


mariadb_connection.commit()
cursor.close()
mariadb_connection.close()


#######################CONFIGURACION DE MAIL####################################################
mail = raw_input ('Ingrese su mail: ')
#inserts the pass with 
password = getpass.getpass()

#encrypts the password
m = hashlib.sha256()
m.update(password)
m.digest()

#Saves the encrypted pass in a file
foo = open("/var/mail/pwd","w")
foo.write(password)
foo.close()


print("Configuracion finalizada")
