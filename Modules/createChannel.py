import requests
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]

def createChannel(serverID, type, name, permission_overwrites, parent_id):
    try:
        createdChannel = requests.post(
            f"https://discord.com/api/v9/guilds/{serverID}/channels",
            json={
                "type": type,
                "name": name,
                "permission_overwrites": permission_overwrites,
                "parent_id": parent_id
            },
            headers={
                "authorization": token,
                "content-type": "application/json"
            }
        ).json()
        return createdChannel
    except Exception as e:
        print(e)