import requests
import msal
import os
import yaml

config_path = os.path.join(os.path.dirname(__file__), '../config', 'config.yaml')
with open(config_path, 'r') as file:
    data = yaml.safe_load(file)

def add_form_to_sharepoint(file_path):
    client_id = data['ms_c_id']
    client_secret = data['ms_c_s']
    tenant_id = data['ms_tnt_id']
    site_name = "__hidden__"
    drive_name = "__hidden__"
    folder_path = "__hidden__"

    file_name = os.path.basename(file_path)

    # auth and get token
    auth_url = f"https://login.microsoftonline.com/{tenant_id}"
    scope = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(
        client_id,
        authority=auth_url,
        client_credential=client_secret
    )

    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" not in result:
        raise Exception(f"Token acquisition failed: {result.get('error_description')}")

    headers = {
        "Authorization": f"Bearer {result['access_token']}",
        "Content-Type": "application/json"
    }

    # get site ID
    site_resp = requests.get(
        f"https://graph.microsoft.com/v1.0/sites/__hidden__:/sites/{site_name}",
        headers=headers
    )
    site_resp.raise_for_status()
    site_id = site_resp.json()["id"]

    # get drive ID
    drive_resp = requests.get(
        f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives",
        headers=headers
    )
    drive_resp.raise_for_status()
    drives = drive_resp.json()["value"]
    drive_id = next(d["id"] for d in drives if d["name"] == drive_name)

    # upload file to sp
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    upload_url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{folder_path}/{file_name}:/content"
    upload_resp = requests.put(
        upload_url,
        headers={"Authorization": f"Bearer {result['access_token']}"},
        data=file_bytes
    )

    upload_resp.raise_for_status()
    link_to_file_on_sp = upload_resp.json()["webUrl"]
    print(f"File uploaded successfully: {link_to_file_on_sp}")

    return link_to_file_on_sp