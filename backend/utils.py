import requests
from dotenv import load_dotenv
import os

def get_access_token() -> str:
    load_dotenv()

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET")
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

if __name__ == '__main__':
    print(get_access_token())