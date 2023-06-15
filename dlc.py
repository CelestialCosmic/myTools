import os
lists = os.listdir("D:\SteamLibrary\steamapps\common\Europa Universalis IV\dlc")
for i in range(0,200):
    try:
        print(str(i+1)+" "+lists[i])
    except:
        break
