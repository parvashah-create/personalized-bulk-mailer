import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb

# set up the message
msg = MIMEMultipart()
msg['From'] = 'shah.parv@northeastern.edu'
msg['To'] = 'jmparvashah@gmail.com'
msg['Subject'] = 'Test email from Python'

body = 'Hello, this is a test email from Python!'
msg.attach(MIMEText(body, 'plain'))

# set up the SMTP server
smtp_server = 'smtp.office365.com'
smtp_port = 587

# set up the email credentials
username = 'shah.parv'
password = 'Keepfaith@042030'


#set chromodriver.exe path
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.implicitly_wait(0.5)
#launch URL
browser.get('https://sts.northeastern.edu/adfs/ls/?login_hint=shah.parv%40northeastern.edu&client-request-id=9834e389-469b-31a4-b4a6-307c388db44f&username=shah.parv%40northeastern.edu&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=estsredirect%3d2%26estsrequest%3drQQIARAAjZK_axNxAMXzzSXXpFUbnEQERZyES76X3o8kIHgmuSQ27SVN0qRdwl3uvr30cvdN7r75Sf8AHYTSRambSIdOolWkk3OnzLoILkUQpC7FyRQXwUHf8OFNb3jv3aXYKJu6A38rzlyQgQixTMu4cH_IvTofefyFe_ZcfskeHcCdxJMjZR9EHOwS01A9YrhO1ND7h-CmSUjXS8ViuE86GFtRjFC7ZURb2I7hoRp7D8AUgFMA9vzXPVM1o13VHdz_K8cvCksJlktyrCDEE_zMcmIU6RBBldMYXRU5huO1OJMUVJVBrMCJiRlVBD_6FxWpT8z4BbDbnhhn_jDCrt3sYo_sU8egsTEpZrzClpytdJtbnli32wOYFgpN7BhyV7JlaZQUFKNYHyFnM1N8WM3WCsqarpgbuJGt1MWGJ0llrxcf8OVCz1FzCscNV_DKck6e5DpbsGJVLbOMGrKQN9cJTtgDLcdvYmLCar4zWSetVZ5say1WEeutZNIcQ5zODVV9Oa2PWN0adFinoEFHKemTpXy1B3U0mEiINJlScXhI_ddWryl61raNnROKxl3DaevTAPgcAF8Dl2AwFQrNRxavzd3ynQfAi-Bs1rHWzPzceVt8-uZGrRxc8J0EY5mGIbXrNkyQ4UavludledtCej5b7luW-yC7KqytKI1Sbry0XLgnpthdGuzS9DEdDlER320qXWJPafCdBo_mfMfhfx1iugA-XPadX_l0sPfj3auTb_lf0')
browser.implicitly_wait(5)
neu_login_page  = browser.find_element(By.CLASS_NAME, "idp")
neu_login_page.click()

browser.implicitly_wait(5)
neu_username  = browser.find_element(By.ID, "username")
neu_password  = browser.find_element(By.ID, "password")
neu_username.send_keys(username)
neu_password.send_keys(password)
neu_login_btn = browser.find_element(By.NAME, "_eventId_proceed")
neu_login_btn.click()
browser.implicitly_wait(20)
WebDriverWait(browser, 20).until(EC.url_to_be("https://login.microsoftonline.com/login.srf/"))

WebDriverWait(browser, 25).until(EC.url_to_be("https://outlook.office.com/mail/"))
compose_mail  = browser.find_element(By.CLASS_NAME, "splitPrimaryButton root-756")
compose_mail.click()


# # connect to the SMTP server and send the email
# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login(username, password)
#     server.sendmail(username, 'jmparvashah@gmail.com', msg.as_string())



# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # set up the message
# msg = MIMEMultipart()
# msg['From'] = 'shah.parv@northeastern.edu'
# msg['To'] = 'jmparvashah@gmail.com'
# msg['Subject'] = 'Test email from Python'

# body = 'Hello, this is a test email from Python!'
# msg.attach(MIMEText(body, 'plain'))

# # set up the email credentials
# username = 'shah.parv@northeastern.edu'
# password = 'Keepfaith@042030'

# # set up the SMTP server
# smtp_server = 'smtp.office365.com'
# smtp_port = 587

# # connect to the SMTP server and send the email
# with smtplib.SMTP(smtp_server, smtp_port) as server:
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login(username, password)
#     server.sendmail(username, 'jmparvashah@gmail.com', msg.as_string())

