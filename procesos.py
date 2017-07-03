#!/usr/bin/python

proc = subprocess.Popen('ps aux', shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print proc

