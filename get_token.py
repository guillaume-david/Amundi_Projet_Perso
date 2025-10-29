# Script qui permet de récupérer les authentifiants (sandbox) / mais a priori on n'y a pas accès.

import requests

def get_aixigo_token():
    token_url = "https://login.portal.aixigo.cloud/realms/apps/protocol/openid-connect/token"

    data = {
        "grant_type": "password",
        "client_id": "<TON_CLIENT_ID>",
        "client_secret": "<TON_CLIENT_SECRET>",
        "username": "guillaume.david@student-cs.fr",
        "password": "..."
    }

    response = requests.post(token_url, data=data)

    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        token = response.json()["access_token"]
        print("✅ Token récupéré avec succès !")
        return token
    else:
        print("❌ Échec :", response.text)
        return None