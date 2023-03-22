import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def add_attachment(file_attach):
    # Add Attachment 
    with open(file_attach, 'rb') as attachment:
        file = MIMEApplication(attachment.read(), _subtype=os.path.splitext(file_attach)[1][1:])
        file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_attach))
        return file
    
def send_email(email_id, app_pass, to, subject, body, file_attach):
    # Create the message object and add the message details
    msg = MIMEMultipart()
    msg['From'] = email_id
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    file = add_attachment(file_attach)
    msg.attach(file)

    


    # Send the message using SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_id, app_pass)
    text = msg.as_string()
    server.sendmail(email_id, to, text)
    server.quit()


# # Set up the login credentials
# gmail_user = 'jmparvashah@gmail.com'
# gmail_password = 'vhgfjhunjiccvinw'  # generate an app password from your Google account

# # Set up the message parameters
# to = 'shah.parv@northeastern.edu'
# subject = 'Test email from Python'
# body = 'This is a test email sent from Python'
# file_attachment = "attachment/Resume-da.pdf"
# send_email(gmail_user,gmail_password,to,subject,body,file_attachment)
