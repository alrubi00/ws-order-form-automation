import requests
import base64
from datetime import datetime
import os
import yaml
from dotenv import load_dotenv

# config_path = os.path.join(os.path.dirname(__file__), '../config', 'config.yaml')
# with open(config_path, 'r') as file:
#     data = yaml.safe_load(file)

today = datetime.now()
date_for_file = today.strftime('%m%d%Y%H%M%S')

def send_email(file):

    load_dotenv()

    TENANT_ID = os.environ.get("TENANT_ID")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_S = os.environ.get("CLIENT_S")

    AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"


    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_S,
        "scope": "https://graph.microsoft.com/.default"
    }

    # ws_order_form_name = f'Wholesale_Order_Form_{date_for_file}.xlsx'
    # os.rename(file, ws_order_form_name)

    with open(file, 'rb') as f:
        excel_bytes = f.read()

    excel_base64 = base64.b64encode(excel_bytes).decode('utf-8')

# Requesting the access token
    response = requests.post(AUTH_URL, data=data)

    # Check for errors in the token request
    if response.status_code != 200:
        print("Error fetching access token:", response.status_code, response.text)
    else:
        token = response.json().get("access_token")
        # print("Access Token:", token)

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        email_data = {
            "message": {
                "subject": "Google Review Removal Service Offer",
                "body": {
                    "contentType": "Text",
                    "content": f'''Here's Johnny'''
                },
                "toRecipients": [
                    {"emailAddress": {"address": "alan.rubin@happyvalley.org"}},
                    {"emailAddress": {"address": "alanrubin00@yahoo.com"}}
                ],
                "attachments": [
                    {
                        "@odata.type": "#microsoft.graph.fileAttachment",
                        "name": file,
                        "contentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        "contentBytes": excel_base64                    
                    }
                ]
            }
        }

        response = requests.post(
            "https://graph.microsoft.com/v1.0/users/alan.rubin@happyvalley.org/sendMail",
            headers=headers,
            json=email_data
        )

        # print(response.status_code, response.text)
        print(response.status_code)

# file = 'Book2.xlsx'
# send_email(AUTH_URL, data, file)
