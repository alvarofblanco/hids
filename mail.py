#!/usr/bin/python
 
import smtplib
import os
import getpass
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
print "Ingrese la contrasena del correo: "
password = getpass.getpass()
s.login('hidsparaguay@gmail.com',password)
s.sendmail('hidsparaguay@gmail.com','alvarofblanco@gmail.com',msg.as_string() )
os.system('rm -rf /tmp/mail')
s.quit()
