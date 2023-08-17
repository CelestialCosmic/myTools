import os
import subprocess
import time
import re
def classifyEngine(folderPath):
    fileList = [
        ["UnityPlayer.dll","UnityCrashHandler64.exe","GameAssembly.dll"],
        ["rpg_core.js","rpg_managers.js","rpg_sprites.js","rpg_scenes.js","rpg_object.js","rpg_windows.js","rmmz_core.js","rmmz_managers.js","rmmz_sprites.js","rmmz_scenes.js","rmmz_object.js","rmmz_windows.js"],
        ["winmm.dll","Game.rvproj","RGSS202J.dll","Game.rgss3a","System.rvdata","Game.ini"],
        ["player.exe","player.lib"],
        ["live.dll"],
        ["data.win"],
        ["SiglusEngine.exe","scene.pck"],
        ["system.arc"],
    ]
    fileSuffix = (
        "arc",
        "apk",
        "wolf",
        ".zst",
        ".tar",
    )
    i = j = 0
    length = len(fileList[i])
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            file = str(file)
            for k in range (len(fileSuffix)):
                if(file.endswith(fileSuffix[k]) == True):
                    return k+100
            while True:
                if file in fileList[i][j]:
                    return i
                if j != length-1:
                    j+=1
                elif j == length-1:
                    if i == len(fileList) - 1:
                        return 10000
                        # break
                    i+=1
                    j=0
                    length = len(fileList[i])

def moveExtracted(unZipFolderPath):
    pathList = {
        # 使用特征文件分类
        0:os.path.join(unZipFolderPath,"extracted","unity"),
        1:os.path.join(unZipFolderPath,"extracted","mvmz-html"),
        2:os.path.join(unZipFolderPath,"extracted","vx-vxace"),
        3:os.path.join(unZipFolderPath,"extracted","pgmMV"),
        4:os.path.join(unZipFolderPath,"extracted","livemaker"),
        5:os.path.join(unZipFolderPath,"extracted","gameMaker"),
        6:os.path.join(unZipFolderPath,"extracted","Siglus-krkr"),
        7:os.path.join(unZipFolderPath,"extracted","majiro"),
        100:os.path.join(unZipFolderPath,"extracted","majiro"),
        # 使用文件后缀分类
        101:os.path.join(unZipFolderPath,"extracted","android"),
        102:os.path.join(unZipFolderPath,"extracted","wolf"),
        # 使用路径分类
        201:os.path.join(unZipFolderPath,"extracted","UE"),
        # tar/zst
        103:os.path.join(unZipFolderPath),
        104:os.path.join(unZipFolderPath),
        # 无法分类
        202:os.path.join(unZipFolderPath,"extracted","godot"),
        203:os.path.join(unZipFolderPath,"extracted","renpy"),
        10000:os.path.join(unZipFolderPath,"extracted","unknown"),
    }
    extractedFolder = os.listdir(os.path.join(unZipFolderPath,"extracted"))
    for folder in extractedFolder:
        folderPath = os.path.join(unZipFolderPath,"extracted",folder)
        match classifyEngine(folderPath):
            case 0:
                print("unity",pathList[0])
            case 1:
                print("rpgMakerMV/MZ")
            case 2:
                print("rpgmakerVx")
            case 3:
                print("pixelMakerMV")
            case 4:
                print("liveMaker")
            case 5:
                print("wolf/gameMaker")
            case 6:
                print("siglus")
            case 7:
                print("majiro")
            case 100:
                print("majiro")
            case 101:
                print("android")
            case 102:
                print("wolf")
            case 103:
                print("tar/zst")
            case 104:
                print("tar/zst")
            case 10000:
                print("unknown")
    


unZipFolderPath = "D:\@game/new"
moveExtracted(unZipFolderPath)