import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime


# def send_email(subject, body, sender, password, recipients, attachment_path):
def send_email(file_path):

    try:
        today = datetime.now()
        date = today.strftime('%m/%d/%Y - %H:%M')
        subject = f'Happy Valley Wholesale Order Form {date}'
        body = f'Please find the attached Wholesale Order Form - {date} - NOTE: Enable Editing once opened'
        sender = 'happyvalleybiteam@gmail.com'
        password = 'yuom ejkm rjpy zany'
        attachment = file_path
        recipients = [
        "alan.rubin@happyvalley.org",
        "kai.earthsong@happyvalley.org",
        "ellida.cornavaca@happyvalley.org",
        "jeremy.nestor@happyvalley.org",
        "gilly.motta@happyvalley.org",
        "heather.lovett@happyvalley.org",
        "shannon.oliver@happyvalley.org"
            ]

        # recipients = [
        # "alan.rubin@happyvalley.org"
        #     ]

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        msg.attach(MIMEText(body, 'plain'))

        # Attach file if path provided
        if attachment and os.path.exists(attachment):
            with open(attachment, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment)}'
                )
                msg.attach(part)
        else:
            print("Attachment not found or not provided.")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print('Message sent!')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# send_email()
# send_email(subject, body, sender, password, recipients, attachment_path)



# import smtplib
# from email.mime.text import MIMEText

# subject = 'Correction...'
# body = '...'
# sender = 'alrubi13@gmail.com'
# password = 'pimu cuol xhxn fmuw'
# recipients = 'alanrubin00@yahoo.com'

# def send_email(subject, body, sender, password, recipients):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = recipients

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
#         smtp_server.login(sender, password)
#         smtp_server.sendmail(sender, recipients, msg.as_string())
#     print('Message sent!')


# send_email(subject, body, sender, password, recipients)