#!/usr/bin/python
import MySQLdb as mariadb
import getpass
import hashlib
import os
import time

#Saludos
print("Bienvenido al instalador del HIDS")
time.sleep(2)
print("Creando archivos de configuracion...")
time.sleep(3)

#Create config files

os.system("rm -rf /var/log/hids")
os.system("rm -rf /etc/hids")

#Create configuration folder
if not os.path.exists("/etc/hids"):
    os.makedirs("/etc/hids")
os.makedirs("/var/log/hids")
if not os.path.exists("/var/log/hids/vault"):
    os.makedirs("/var/log/hids/vault")

#Crete the log files
os.system("touch /var/log/hids/alarmas.log")
os.system("touch /var/log/hids/prevencion.log")

#Crete the sniffers files
f = open('/etc/hids/sniffers.hids', 'a')
f.write("tshark\njohn\nkismet\ntcpdump\ndsniff\nettercap\nngrep\ntopng\nsnort")
f.close()

print("Archivos de configuracion creados")
time.sleep(2)

#Usuarios permitidos
print "Agregar permisos a usuarios que se conectan al equipo. 0 para salir"

#Crete the users files
f = open('/etc/hids/users.hids','a')
nombre = raw_input("Inserte el nombre: ")

while nombre != '0':
    ip = raw_input("Inserte la direccion IP: ")
    line = nombre + ',' +ip
    f.write(line)
    nombre = raw_input("Inserte el nombre: ")
    
#Scripts que se pueden ejecutar en modo cron
print "Agregar el path de los scripts que se pueden ejecutar en modo cron. 0 para salir"

#Crete the users files
f = open('/etc/hids/cron.hids','a')
nombre = raw_input("Inserte el nombre: ")

while nombre != '0':
    f.write(nombre)
    nombre = raw_input("Inserte el nombre: ")


print ("Configurando base de datos")
password = getpass.getpass()

try:
    mariadb_connection = mariadb.connect("localhost",'root',password)
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
cursor.execute("CREATE TABLE cron(name varchar(40))")

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
cursor.execute("LOAD DATA LOCAL INFILE '/etc/hids/sniffers.hids' INTO TABLE sniffers FIELDS TERMINATED BY ','")

#entering the cron scripts
cursor.execute("LOAD DATA LOCAL INFILE '/etc/hids/cron.hids' INTO TABLE cron")


mariadb_connection.commit()
cursor.close()
mariadb_connection.close()
#######################CONFIGURACION DE iptables####################################################
os.system("chmod +x iptables.sh")
os.system("./iptables.sh")

#######################CONFIGURACION DE MAIL####################################################
mail = raw_input ('Ingrese la direccion de correo que enviara las alertas: ')
#inserts the pass with 
password = getpass.getpass()

#Guardar la contrasena en un archivo
f = open("/var/log/pass","w")
f.writelines(password)
f.close()

#cifrar esa contrasena
os.system("gpg -c /var/hids/mail/pass")
os.system("rm -f /var/hids/mail/pass")


print("Configuracion finalizada")
