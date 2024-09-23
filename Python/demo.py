# a =10
# a = 'Shashank'
# a = ['S',12]
# print(a[2])

# a,b,c,d = 10,20,30,40
# print(a)
# print(b)
# print(c)
# print(d)

# a = 20
# print(type(a))

#Explicit conversion
# a =10
# b ="20"
# c =a+float(b)
# print(c)

# a =38.99
# b = int(a)
# print(b)

# import decimal
# from decimal import Decimal

# a = Decimal('1.1')
# b = Decimal('2.2')
# c = a + b
# print(c)

# Swaping of the two number
# a  = 36
# b = 45
# a,b = b,a
# print(a)
# print(b)

#creating a List
# class_list = [10,20,30,40,50]
# print(class_list)
# print(type(class_list))
# print(class_list[3])

#Slicing a list
# s_list = [1,2,3,4,5,6,7,8]
# print(s_list[0:5])

# a = [1,2,3,4,5]
# b = [6,7,8,9,0]
# c = a + b
# print(c)

# a = [1,['hi','hello','list']]
# print(a[1][1])

#Repating of stings
# stocks = ['sai','ram','sita']
# n = 3*stocks
# print(n)

#Sorting thge alplabits
# a  = ['w','y','z','e','b']
# print(sorted(a))

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "shashankmanjula2003@gmail.com"
receiver_email = "gsd99689@gmail.com"
password = "kbco qjlb kckv cpjo"
subject = "Test Email"
body = "This is a test email sent from Python"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
#Attach the body with msg instance
message.attach(MIMEText(body,"plain"))

#step3-Setup the SMTP server
smtp_server = "smtp.gamil.com"
port = 587
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() #secure the connection
    #login to the email account
    server.login(sender_email,password)
    #send the mail
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email successfully sent")
except Exception as e:
    print(f"error: {e}")
finally:
    server.quit() #close the connection
