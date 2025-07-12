import requests
import msal
import base64
import os
import yaml
from datetime import datetime
import constants as cs

config_path = os.path.join(os.path.dirname(__file__), '../config', 'config.yaml')
with open(config_path, 'r') as file:
    data = yaml.safe_load(file)

def email_form_w_link(file_path, link_to_file_on_sp):
    today = datetime.now()
    date = today.strftime('%m/%d/%Y - %H:%M')
    client_id = data['ms_c_id']
    client_secret = data['ms_c_s']
    tenant_id = data['ms_tnt_id']
    subject = f'Happy Valley Wholesale Order Form {date}'
    
    body = f'''<p>Please find the attached Wholesale Order Form - {date}.</p>
            <p>NOTE: Enable Editing once opened.</p>
            <p>You can also <a href="{link_to_file_on_sp}">view it on SharePoint</a>.</p>'''

    auth_url = f"https://login.microsoftonline.com/{tenant_id}"
    scopes = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(
        client_id,
        authority=auth_url,
        client_credential=client_secret
    )
    result = app.acquire_token_for_client(scopes=scopes)
    if "access_token" not in result:
        raise Exception(f"Token acquisition failed: {result.get('error_description')}")

    access_token = result["access_token"]

    with open(file_path, "rb") as f:
        attachment_content = base64.b64encode(f.read()).decode()

    attachment_name = os.path.basename(file_path)
    attachment = {
        "@odata.type": "#microsoft.graph.fileAttachment",
        "name": attachment_name,
        "contentBytes": attachment_content
    }

    # generate recipient list
    recipients = [{"emailAddress": {"address": email}} for email in cs.to_email]

    message = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": body
            },
            "toRecipients": recipients,
            "attachments": [attachment]
        },
        "saveToSentItems": "true"
    }

    # send email with attachment
    send_url = f"https://graph.microsoft.com/v1.0/users/{cs.from_email}/sendMail"
    response = requests.post(send_url, headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }, json=message)

    if response.status_code == 202:
        print("Email sent successfully.")
    else:
        print("Failed to send email:", response.status_code, response.text)