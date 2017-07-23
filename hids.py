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
    print("2. Check md5sum signature of bin files")
    print("3. Check the integrity of the /temp folder")
    print("0. Salir")

#Function that calls the chk_bin.py script
def chk_bin():
    print ("Chequeo de archivos binarios del sistema seleccionado")
    #os.system("python chk_bin.py")

#Function that installs and configure the hids      
def conf():
    print ("Instalacion del HIDS")
    #os.system("python instalacion.py")

#Function that calls the chk_temp.py script
def chk_temp():
    print ("Chequeo de la carpeta /temp")
    #os.system("python chk_temp.py")

#Function that checks the mail queue
def chk_mailq():
    print("Chequep de la cola de mail")
    #os.system("python mail_queue.py")
    
#Function that checks if there is a process comsuming too much resources
def chk_resources():
    print("Chequeo de los procesos del sistema")
    #os.sytem("python procesos.py")

#Function that checks if the interfaces are in promis mode
def chk_promisc():
    print("Verificacion de modo promiscuo")
    #os.system("python promisc.py")
    
#Function that looks through sniffers in the system
def chk_sniffers():
    print("Buscando sniffers")
    #os.system("python sniffers.py")

#Function that sees who is connected to the server
def chk_who():
    print("Verificacion de usuarios conectados al servidor")
    os.system("python who.py")

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

    
