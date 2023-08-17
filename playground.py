import os
import subprocess
import time
import re
import winreg
# import chardet
from winreg import *
def main():
    unZipFolderPath = "D:\@game/new"
    extractedFolder = os.listdir(os.path.join(unZipFolderPath,"extracted"))
    # 大引擎系
    # unity
    # unreal
    # godot
    unityFolder = os.path.join(unZipFolderPath,"extracted","unity")
    unrealFolder = os.path.join(unZipFolderPath,"extracted","UE")
    godotFolder = os.path.join(unZipFolderPath,"extracted","godot")
    # rpgmaker系
    # rpgmakerMV/MZ/nwjs
    # rpgmakerVX/VXACE
    # pixelMakerMV
    rpgMakerFolder = os.path.join(unZipFolderPath,"extracted","mvmz-html")
    vxvxaceFolder = os.path.join(unZipFolderPath,"extracted","vx-bxace")
    pixelMakerMVFolder = os.path.join(unZipFolderPath,"extracted","pgmMV")
    # 小引擎系
    # gameMaker
    # renpy
    # majiroScript
    # kirikiri
    # livemaker
    gameMakerFolder = os.path.join(unZipFolderPath,"extracted","gaameMaker")
    renpyFolder = os.path.join(unZipFolderPath,"extracted","renpy")
    kirikiriFolder = os.path.join(unZipFolderPath,"extracted","Siglus-krkr")
    majiroScriptFolder = os.path.join(unZipFolderPath,"extracted","majiro")
    liveMakerFolder = os.path.join(unZipFolderPath,"extracted","livemaker")
    # 完全未知/安卓安装包
    # android
    # unknown
    androidFolder = os.path.join(unZipFolderPath,"extracted","android")

    # 特征文件列表
    unitySpecialFileList = ["UnityPlayer.dll","UnityCrashHandler64.exe","GameAssembly.dll"]
    unrealSpecialFileList = []
    # 路径判断 Engine\Binaries\ThirdParty
    godotSpecialFileList = []
    # godot 没有特殊文件，只能看图标判断
    # 或者详细信息正则表达式寻找 Juan Linietsky, Ariel Manzur and contributors
    rpgMakerSpecialFileList = ["rpg_core.js","rpg_managers.js","rpg_sprites.js","rpg_scenes.js","rpg_object.js","rpg_windows.js","rmmz_core.js","rmmz_managers.js","rmmz_sprites.js","rmmz_scenes.js","rmmz_object.js","rmmz_windows.js"]
    vxvxaceSpecialFileList = ["winmm.dll","Game.rvproj","RGSS202J.dll","Game.rgss3a","System.rvdata","Game.ini"]
    # game.ini 是都有的，但是它是一个极易产生歧义的文件名
    pixelMakerMVSpecialFileList = ["player.exe","player.lib"]
    liveMakerSpecialFileList = ["live.dll"]
    gameMakerSpecialFileList = ["data.win"]
    renpySpecialFileList = []
    kirikiriSpecialFileList = ["SiglusEngine.exe","scene.pck"]
    majiroSpecialFileList = ["system.arc"]
    for folders in extractedFolder:
        folderPath = os.path.join(unZipFolderPath,"extracted",folders)
        fileList = os.listdir(folderPath)
        for root, dirs, files in os.walk(folderPath):
            for f in files:
                try:
                    if(f in unitySpecialFileList):
                        print("unity:\n"+folderPath+"\n")
                        os.replace(folderPath,unityFolder+"/"+folders)
                        return 1
                    elif(os.path.exists(os.path.join(folderPath,"Engine","Binaries","ThirdParty"))):
                        print("UE:\n"+folderPath+"\n")
                        os.replace(folderPath,unrealFolder+"/"+folders)
                        return 2
                    elif(f in rpgMakerSpecialFileList):
                        print("rpgmakerMV/MZ:\n"+folderPath+"\n")
                        os.replace(folderPath,rpgMakerFolder+"/"+folders)
                        return 3
                    elif(f in vxvxaceSpecialFileList):
                        print("vx/vxace:\n"+folderPath+"\n")
                        os.replace(folderPath,vxvxaceFolder+"/"+folders)
                        return 4
                    elif(f in pixelMakerMVSpecialFileList):
                        print("pixelMakerMV:\n"+folderPath+"\n")
                        os.replace(folderPath,pixelMakerMVFolder+"/"+folders)
                        break
                    elif(f in gameMakerSpecialFileList):
                        print("gameMaker:\n"+folderPath+"\n")
                        os.replace(folderPath,gameMakerFolder+"/"+folders)
                        break
                    elif(f in kirikiriSpecialFileList):
                        print("siglus:\n"+folderPath+"\n")
                        os.replace(folderPath,kirikiriFolder+"/"+folders)
                    elif(f.endswith("xp3")):
                        print("kirikiri:\n"+folderPath+"\n")
                        os.replace(folderPath,kirikiriFolder+"/"+folders)
                        break
                    elif(f.endswith("apk")):
                        print("android:\n"+folderPath+"\n")
                        os.replace(folderPath,androidFolder+"/"+folders)
                        break
                    elif(f in majiroSpecialFileList):
                        print("majiroScript:\n"+folderPath+"\n")
                        os.replace(folderPath,majiroScriptFolder+"/"+folders)
                        break
                    elif(f in liveMakerSpecialFileList):
                        print("livemaker:\n"+folderPath+"\n")
                        os.replace(folderPath,liveMakerFolder+"/"+folders)
                        break
                except FileNotFoundError:
                    pass
                # except PermissionError:
                #     print("权限错误")
                #     pass
    # 换成return + case match


