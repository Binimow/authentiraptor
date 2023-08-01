import requests
import json

client_credentials = requests.get("http://localhost:8000/client/").json()

with open("src/assets/client_id.json", "w") as file:
    json.dump(client_credentials["client_id"], file, indent=4)

with open("/credentials.json", "w") as file:
    json.dump(client_credentials, file, indent=4)

