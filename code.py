{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import smtplib\
from email.message import EmailMessage\
\
def send_email(sender_email, receiver_email, subject, body, smtp_server='smtp.gmail.com', smtp_port=587, password='your_password'):\
    msg = EmailMessage()\
    msg['Subject'] = subject\
    msg['From'] = sender_email\
    msg['To'] = receiver_email\
    msg.set_content(body)\
\
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:\
        smtp.starttls()\
        smtp.login(sender_email, password)\
        smtp.send_message(msg)\
\
# Example usage:\
sender_email = 'your_email@gmail.com'\
receiver_email = 'recipient_email@example.com'\
subject = 'Hello from Python!'\
body = 'This is a test email sent using Python.'\
\
send_email(sender_email, receiver_email, subject, body)}