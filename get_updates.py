# get_updates.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("EITAA_API_TOKEN")
url = f"https://eitaayar.ir/api/{token}/getUpdates"

resp = requests.get(url, verify=False)
data = resp.json()
print(data)
