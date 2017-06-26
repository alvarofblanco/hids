#!/usr/bin/env python
import sys
import subprocess
import os
def main():
    f = os.popen('date')
    now = f.read()
    print "Today is ", now
    