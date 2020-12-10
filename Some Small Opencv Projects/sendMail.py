from personal_details import username, password, receiver
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = username
EMAIL_PASSWORD = password

contacts = [username, receiver]
msg = EmailMessage()
msg['Subject'] = 'Attention ...  Attention .. Attention ...'
msg['From'] = EMAIL_ADDRESS
msg['To'] = receiver
msg.set_content('Image attached ...')


def send_mail(files):
    with open(files, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    """for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        """
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("email has been sent ")



