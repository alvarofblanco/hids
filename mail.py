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
s.login('hidsparaguay@gmail.com','Tiburoncin123')
s.sendmail('hidsparaguay@gmail.com','alvarofblanco@gmail.com',msg.as_string() )
os.system('rm -rf /tmp/mail')
s.quit()
