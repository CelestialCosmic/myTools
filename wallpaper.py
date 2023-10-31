import re
import os
contentDir = "D:\SteamLibrary\steamapps\workshop\content/431960"
for content in os.listdir(contentDir):
    currentDir = os.path.join(contentDir,content)
    for root, dirs, files in os.walk(currentDir):
        for file in files:
            partName = re.findall(r'[\d]{3}\.png',file)
            if(partName != []):
                resourcesPath = os.path.join(contentDir,currentDir,"行楷_Data\Resources")
                for root, dirs, files in os.walk(resourcesPath):
                    for file in files:
                        newName = file+".7z."+partName[0][0:3]
                        newPath = os.path.join(contentDir,"resources",newName)
                        # print(os.path.join(resourcesPath,file))
                        os.replace(os.path.join(resourcesPath,file),newPath)


