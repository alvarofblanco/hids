#!/usr/bin/python
 
import smtplib
import os
from email.mime.text import MIMEText

fp = open("/tmp/mail", 'w')
fp.write('Hola los perros, soy el HIDS')
fp.close()
fp = open("/tmp/mail", 'rb')
msg = MIMEText(fp.read())
fp.close()
msg['Subject'] = 'The contents of /tmp/prueba'
msg['From'] = 'hidsparaguay@gmail.com'
msg['To'] = 'alvarofblanco@gmail.com'
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('hidsparaguay@gmail.com','Tiburoncin123')
s.sendmail('hidsparaguay@gmail.com','alvarofblanco@gmail.com',msg.as_string() )
os.system('rm -rf /tmp/mail')
s.quit()
