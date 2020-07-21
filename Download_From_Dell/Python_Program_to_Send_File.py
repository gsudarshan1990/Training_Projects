"""
This is the program to send the downloaded file
"""

import email, smtplib , ssl

username='sudarshan.suraj2007@gmail.com'
password='zojfybcsqjjoicos'
SMTP_HOST='smtp.gmail.com'
SMTP_PORT=58

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

body ='This is used to send the mails downloaded by selenium'
subject = 'Send the Dell File'
sender = 'sudarshan.suraj2007@gmail.com'
receiver = 'sudarshan.suraj2007@gmail.com'
password ='zojfybcsqjjoicos'

message = MIMEMultipart()
message['From'] =sender
message['To'] = receiver
message['Subject'] = subject

message.attach(MIMEText(body,'plain'))

filename = "F:\Downloads\BIOS_RTWM9_WN64_2.8.1.EXE"
with open(filename,"rb") as attachment:
    payload = MIMEBase("application","octet-stream")
    payload.set_payload(attachment.read())

encoders.encode_base64(payload)

payload.add_header('content-Decomposition',f"attachment; filename ={filename}")
message.attach(payload)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender,receiver,text)

