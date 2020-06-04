import os
import time
import smtplib
from email.message import EmailMessage

# User Credentials (Email ID and Password)
EMAIL_ID = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

print('************************')
print(' WELCOME TO EASY MAIL !')
print('************************')

# Subject Input
mail_subject = str(input('Enter Email Subject: '))

# Content Input
mail_msg = str(input('Import message from text file ? y/n: '))
# Importing Content from Body_content.txt
isValid = False
while isValid == False:
	if mail_msg == 'y':
		with open('Body_content.txt', 'r') as bc:
			bodyContent = bc.read()
		isValid = True
	elif mail_msg == 'n':
		bodyContent = str(input('Enter Body Content: '))
		isValid = True
	else:
		print('Invalid Input !')

# Recipients / Receivers Input
recipients = str(input('Enter recipients: '))

# Creating message from EmaiLMessage Module
msg = EmailMessage()
msg['Subject'] = mail_subject
msg['From'] = EMAIL_ID
msg['To'] = recipients
msg.set_content(bodyContent)
print('Initializing ...')
time.sleep(3)
print('Creating Email ...')
time.sleep(2)
print('Email Created !!')
time.sleep(1)

# Attachments Input
toAttach = str(input('Attach files from Attachments Folder ? y/n: '))
# Importing attachments from Attachments folder
if toAttach == 'y':
	files = os.listdir('Attachments')
	amtFiles = len(files)
	for file in files:
		with open(f'Attachments/{file}', 'rb') as f:
			file_name = file
			file_data = f.read()

		msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

	print('Attaching Files ...')
	time.sleep(2)
	print(f'{amtFiles} Files Attached !!')
	time.sleep(2)



# Email Sending Server
print('Creating Server ...')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ID, EMAIL_PASSWORD)
	smtp.send_message(msg)
print('Server Created !')
time.sleep(1)

print()
print('E-MAIL COMPOSED !!')
