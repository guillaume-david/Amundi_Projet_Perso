""" Script mort,
il permettrait de récupérer le token pour accéder à la SANDBOX de AMUNDI
mais il nous faudrait client_id et client_secret
"""

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