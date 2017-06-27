#!/usr/bin/python
import sys
import subprocess
import os

def print_header():
    print("#################### H I D S ####################")
    print("Elaborado por Alvaro Franco Blanco")
    
def print_menu():
    print("Menu")
    print("1. Configuracion inicial del sistema")
    print("2. Verificar archivos binarios del sistema")
    print("0. Salir")

def chk_bin():
    print ("Chequeo de archivos binarios del sistema seleccionado")
    
def conf():
    os.system("python instalacion.py")


def main():

    print_header()
    print_menu()
    option = input("Option: ")
    while option > 2 and option < 0 :
        print("Opcion invalida")
        option = input("Option: ")
    
    cases = {
        '1': conf,
        '2': chk_bin #do not use ()
    }
    
    function = cases [str(option)]
    function()
    
        
    
    

if __name__=="__main__":
	main()

    
