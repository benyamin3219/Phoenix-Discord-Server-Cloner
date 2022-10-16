import requests
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]

def getChannels(serverID):
    channels = requests.get(
        f"https://discord.com/api/v8/guilds/{serverID}/channels",
        headers={
            "authorization": token,
            "content-type": "application/json"
        }
    )
    return channels.json()