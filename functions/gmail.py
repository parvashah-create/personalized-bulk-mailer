# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# import os

# def add_attachment(file_attach):
#     file = MIMEApplication(file_attach.read(), _subtype=file_attach.name[1][1:])
#     file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_attach.name))
#     return file

# def send_email(email_id, app_pass, to, subject, body, file_attach):
#     # Create the message object and add the message details
#     msg = MIMEMultipart()
#     msg['From'] = email_id
#     msg['To'] = to
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))
#     if file_attach is not None:
#         file = add_attachment(file_attach)
#         msg.attach(file)
#     # Send the message using SMTP
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(email_id, app_pass)
#     text = msg.as_string()
#     server.sendmail(email_id, to, text)
#     server.quit()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Function to add attachment to the email
def add_attachment(file_attach):
    # Read the contents of the file and create a MIMEApplication object
    file = MIMEApplication(file_attach.read(), _subtype=file_attach.name[1][1:])
    # Add the header to specify the attachment filename
    file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_attach.name))
    return file

# Function to send email
def send_email(email_id, app_pass, to, subject, body, file_attach):
    # Create the message object and set the message details
    msg = MIMEMultipart()
    msg['From'] = email_id
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain')) # Attach plain text body to the message
    if file_attach is not None: # If a file attachment is provided
        file = add_attachment(file_attach) # Add the attachment to the message
        msg.attach(file)
    # Send the message using SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_id, app_pass)
    text = msg.as_string()
    server.sendmail(email_id, to, text)
    server.quit()
