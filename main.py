from Modules import createChannel, createServer, getChannels
from time import sleep, perf_counter

def main():
    serverID = input("Enter Server ID To Clone: ")
    t1 = perf_counter()
    print("Creating Server...")
    createdServer = createServer.createServer(serverID)
    print("Server Created!")
    print("Creaing Categories...")
    targetchannels = getChannels.getChannels(serverID)
    categories = []
    for i in targetchannels:
        if i["type"] == 4:
            categories.append(i)
    categories.sort(key=lambda x:x["position"])
    for i in categories:
        createChannel.createChannel(createdServer, i["type"], i["name"], i["permission_overwrites"], i["parent_id"])
        print(f"Created Category {i['name']}")
        sleep(1)
    print("Categories Created!")
    print("Creaing Channels...")
    createdServerchannels = getChannels.getChannels(createdServer)
    channels = []
    for i in targetchannels:
        if i ["type"] != 4:
            channels.append(i)
    channels.sort(key=lambda x:x["position"])
    for i in categories:
        for j in createdServerchannels:
            if i['name'] == j['name']:
                for x in channels:
                    if x['parent_id'] == i['id']:
                        x['parent_id'] = j['id']
    for i in channels:
        createChannel.createChannel(createdServer, i["type"], i["name"], i["permission_overwrites"], i["parent_id"])
        print(f"Created Channel {i['name']}")
        sleep(1)
    print("Channels Created!")
    print(f"Done Cloning Server in {round(perf_counter()-t1,1)}S !")

if __name__ == "__main__":
    main()