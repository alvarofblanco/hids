#!/usr/bin/python
import sys
import subprocess
import os

def print_header():
    print("#################### H I D S ####################\n")
    print("Elaborado por Alvaro Franco Blanco")
    
def main():
    p=subprocess.Popen(["ls","-l", "/etc/resolv.conf"], stdout=subprocess.PIPE)
    output,err = p.communicate()
    
    print_header()
    
    
    

if __name__=="__main__":
	main()

    