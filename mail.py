#!/usr/bin/python
 
import smtplib
import os
from email.mime.text import MIMEText

#This file has the body of the mail
fp = open("mail", 'rb')
msg = MIMEText(fp.read())
fp.close()

#Headers of the mail
msg['Subject'] = 'Aviso de seguridad'
msg['From'] = 'hidsparaguay@gmail.com'
msg['To'] = 'alvarofblanco@gmail.com'

#Initialize the mail service
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()

#Mail and pass of the account
os.system("gpg -d /var/log/hids/pass.gpg > .pass")
f = open(".pass","r")
pwd = f.readlines()
os.system("rm -f .pass")
raw_input("Salir")
s.login('hidsparaguay@gmail.com',pwd)
s.sendmail('hidsparaguay@gmail.com','alvarofblanco@gmail.com',msg.as_string() )
os.system('rm -rf /tmp/mail')
s.quit()
