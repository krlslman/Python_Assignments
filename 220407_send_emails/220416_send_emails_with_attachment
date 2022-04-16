import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Test Subject!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'YourAddress@gmail.com'

msg.set_content('This is a email here')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

file_path = "C:\\Users\\...\\Sreenshots\\screenshot20220414.png"
with open(file_path, 'rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)
	file_name = f.name
msg.add_attachment(file_data, maintype='image', subtype=file_type, file_name=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
