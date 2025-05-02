import requests
import time
from datetime import datetime
import os
import yaml

# with open('config/config.yaml', 'r') as file:
#     data = yaml.safe_load(file)

config_path = os.path.join(os.path.dirname(__file__), '../config', 'config.yaml')
with open(config_path, 'r') as file:
    data = yaml.safe_load(file)

today = datetime.now()
date_for_file = today.strftime('%m%d%Y%H%M%S')

# Ensure output directory exists
SAVE_DIRECTORY = 'C:/python/ws-order-form-automation/tmp'
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

def login():
    session = requests.Session()
    login_url = 'https://hv.qlshosting.com/entity/auth/login'

    credentials = {
        "name": data['name'],
        "password": data['password'],
        "tenant": data['tenant']
    }

    try:
        response = session.post(
            login_url,
            json=credentials,
            headers={
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }
        )
        response.raise_for_status()
        print(f"[Login] Success | Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[Login] Failed: {e}")
        return None

    # Confirm the session has the correct .ASPXAUTH cookie
    if '.ASPXAUTH' not in session.cookies.get_dict():
        print("[Login] .ASPXAUTH cookie not found.")
        return None

    return session  # return the active, authenticated session


def generate_download_report(session, report_id):
    time.sleep(5)
    base_url = 'https://hv.qlshosting.com'
    report_url = f'{base_url}/entity/Report/23.200.001/{report_id}'

    headers = {
        'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    body_data = {
        "CompanyBranch": {"value": "SOFT"},
        "IncludeNonClearedTransactions": {"value": True}
    }

    try:
        response = session.post(report_url, json=body_data, headers=headers)
        response.raise_for_status()
        print(f'Status code for report gen:: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f"[Report Gen] Failed for {report_id}: {e}")
        return None

    if response.status_code == 202:
        time.sleep(45)
        file_location = response.headers.get('Location')
        print(f'FILE LOCATION:: {file_location}')
        if not file_location:
            print("[Report Gen] No Location header found.")
            return None

        download_url = f'{base_url}{file_location}'
        print(f"[Download] Download URL: {download_url}")

        try:
            file_response = session.get(download_url, headers=headers)
            file_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[Download] Failed for {report_id}: {e}")
            return None

        filename = f'{report_id}{date_for_file}.xlsx'
        file_path = os.path.join(SAVE_DIRECTORY, filename)

        with open(file_path, 'wb') as f:
            f.write(file_response.content)
            print(f"[Download] File saved: {file_path}")

        time.sleep(5)
        # session.close()
        return file_path

    else:
        print(f"[Report Gen] Failed | Status: {response.status_code}")
        return None

def close_acumatica_session(session):

     logout_url = 'https://hv.qlshosting.com/entity/auth/logout'
     try:
        response = session.post(logout_url)
        response.raise_for_status()
        session.close()
        print("Session closed successfully.")
     except requests.exceptions.RequestException as e:
        print(f"Error during logout: {e}")
     except Exception as e:
         print(f"An unexpected error occurred during logout: {e}")