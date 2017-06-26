#!/usr/bin/python
import sys
import subprocess
import os
def main():
    p=subprocess.Popen(["ls","-l", "/etc/resolv.conf"], stdout=subprocess.PIPE)
    output,err = p.communicate()
    
    listdir = os.listdir('/tmp')
    print listdir[0]
    
    
    

if __name__=="__main__":
	main()

    