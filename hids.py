#!/usr/bin/python
import sys
import subprocess
import os

def exit():
    print("Bye")
def print_header():
    print("#################### H I D S ####################")
    print("Developed by Alvaro Franco Blanco")
    
def print_menu():
    print("Menu")
    print("1. HIDS Setup")
    print("2. Check md5sum signature of bin files")
    print("3. Check the integrity of the /temp folder")
    print("0. Salir")

def chk_bin():
    print ("Chequeo de archivos binarios del sistema seleccionado")
    
def conf():
    os.system("python instalacion.py")

def chk_temp():
    os.system("python chk_temp.py")



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
    
    print "Bye"

if __name__=="__main__":
	main()

    
