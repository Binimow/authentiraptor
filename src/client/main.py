import json
import shlex
import requests

from utils import *


auth_server_url = "http://localhost:8000"
client_id = ""
client_secret = ""

print("CLIENT: Get access tokens from the authorization server")

with open("credentials.json", "r") as credentials_file:
    try:
        credentials = json.load(credentials_file)
        if ("client_id" in credentials):
            client_id = credentials["client_id"]
            client_secret = credentials["client_secret"]
        else:
            print("CLIENT: No credentials found. Acquire credentials first.")
    except json.decoder.JSONDecodeError:
        print("CLIENT: No credentials found. Acquire credentials first.")



while True:
    cmd, *args = shlex.split(input('> '))

    if (cmd == "exit"):
        break

    if (cmd == "acquire"):
        if (args[0] == "credential" or args[0] == "credentials"):
            client = requests.get(
                url=f"{auth_server_url}/client",
            )
            client_id = client.json()["client_id"]
            client_secret = client.json()["client_secret"]
            with open("credentials.json", "w") as credentials_file:
                credentials_file.write(client.text)


    elif (cmd == "get"):
        if (not has_args(args)):
            print("CLIENT: Missing arguments")
            continue
        if (args[0] == "access_token"):
            print("CLIENT: Get access token")
            if (args[1] == "default"):
                scope = "read"
                audience = "http://localhost:8001"
            else:
                scope = args[1]
                audience = args[2]
            requests.get(
                url=f"{auth_server_url}/auth/token",
                params={
                    "scope": scope,
                    "audience": audience
                }
            )