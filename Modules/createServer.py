import requests, base64
from dotenv import dotenv_values
token = dotenv_values(".env")["TOKEN"]

def imageToBase64(link):
    with requests.get(link) as image:
        return base64.b64encode(image.content).decode('utf-8')

def getGuildRoles(serverID):
    guildRoles = []
    roles = requests.get(
        f"https://discord.com/api/v9/guilds/{serverID}/roles",
        headers={
            "authorization": token,
            "content-type": "application/json"
        }
    ).json()
    for role in roles:
        guildRoles.append(
            {
                "name": role["name"],
                "permissions": role["permissions"],
                "id": role["id"],
                "position": role["position"],
                "color": role["color"],
                "hoist": role["hoist"],
                "mentionable": role["mentionable"],
            }
        )
    guildRoles.sort(key=lambda x:x["position"])
    return guildRoles

def createServer(serverID):
    guildInfo = requests.get(
        f"https://discord.com/api/v9/guilds/{serverID}",
        headers={
            "authorization": token,
            "content-type": "application/json"
        }
    ).json()

    createdServer = requests.post(
        "https://discord.com/api/v9/guilds",
        json={
            "name": guildInfo["name"],
            "icon": "data:image/png;base64," + imageToBase64("https://cdn.discordapp.com/icons/"+guildInfo["id"]+"/"+guildInfo["icon"]+".png?size=240"),
            "roles": getGuildRoles(guildInfo["id"])
        },
        headers={
            "authorization": token,
            "content-type": "application/json"
        }
    ).json()

    return createdServer["id"]