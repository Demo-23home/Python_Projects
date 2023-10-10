from email.message import EmailMessage
from app_password import password
import ssl
import smtplib


email_sender = "zeyadslama23@gmail.com"
email_password = password
email_reciver = "facoho2464@locawin.com"

subject = "Email Sent from Python Code :)"
body = """
HI?
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
