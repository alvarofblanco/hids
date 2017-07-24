#!/usr/bin/python
import sys
import subprocess
import os

#Exit function
def exit():
    print("Bye")

#Function that prints the header
def print_header():
    print("#################### H I D S ####################")
    print("Developed by Alvaro Franco Blanco")
    
#function that prints the menu
def print_menu():
    print("Menu")
    print("1. HIDS Setup")
    print("2. Verificar la firma md5sum de los archivos")
    print("3. Buscar scripts maliciosos en la carpeta /temp")
    print("4. Buscar script maliciosos en crontab")
    print("5. Verificar ataques ddos")
    print("6. Verificar la cola de mails")
    print("7. Verificar errores de autentificacion")
    print("8. Verificar consumo de recursos de los procesos")
    print("9. Verificar si las interfaces estan en modo promiscuo")
    print("10.Buscar sniffers")
    print("11.Verificar quien esta conectado al servidor")
    print("12. Buscar errores 404")
    print("0. Salir")

#Function that calls the chk_bin.py script
def chk_bin():
    print ("Chequeo de archivos binarios del sistema seleccionado")
    os.system("python chk_bin.py")

#Function that installs and configure the hids      
def conf():
    print ("Instalacion del HIDS")
    os.system("python instalacion.py")

#Function that calls the chk_temp.py script
def chk_temp():
    print ("Chequeo de la carpeta /temp")
    os.system("python chk_temp.py")

#Function that checks the mail queue
def chk_mailq():
    print("Chequep de la cola de mail")
    os.system("python mail_queue.py")
    
#Function that checks if there is a process comsuming too much resources
def chk_resources():
    print("Chequeo de los procesos del sistema")
    os.system("python procesos.py")

#Function that checks if the interfaces are in promis mode
def chk_promisc():
    print("Verificacion de modo promiscuo")
    os.system("python promisc.py")
    
#Function that looks through sniffers in the system
def chk_sniffers():
    print("Buscando sniffers")
    os.system("python sniffers.py")

#Function that sees who is connected to the server
def chk_who():
    print("Verificacion de usuarios conectados al servidor")
    os.system("python who.py")
    
def chk_cron():
    print("Verificacion de los scripts en cron")
    os.system("python cron.py")
def chk_ddos():
    print("Verificacion de ataque ddos")
    os.system("python ddos.py")
def chk_auth():
    print("Verificacion de intentos fallidos de inicio de sesion")
    os.system("python secure.py")
    os.system("pythin messages.py")
def chk_process():
    print("Verificacion de consumo de recursos de los procesos activos")
    os.system("python procesos.py")
def chk_access_log():
    print("Verificacion de errores 404")
    os.system("python access_log.py")

#main function
def main():

    print_header()
    print_menu()
    option = input("$ ")

    while option != 0:
        if option==1:
            conf()
        elif option == 2:
            chk_bin()
        elif option == 3:
	        chk_temp()
        elif option == 4:
		    chk_cron()
        elif option == 5:
	        chk_ddos()
        elif option == 6:
	        chk_mailq()
        elif option == 7:
	        chk_auth()
        elif option == 8:
	        chk_process()
        elif option == 9:
	        chk_promisc()
        elif option == 10:
	        chk_sniffers()
        elif option == 11:
	        chk_who()
        elif option == 12:
	        chk_access_log()
        elif option == 0:
            exit()
        else:
            print "Invalid input"
        
        print_menu()
        print "Imprimiendo menu"
        option = input("$ ")
    
    exit()

if __name__=="__main__":
	main()

    
