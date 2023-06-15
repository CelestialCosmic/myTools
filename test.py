import os
import subprocess
import time
import re
global passwdList
passwdList = [
    # "半夏",
    # "莱茵",
    # "https://t.me/RhineLibrary",
    # "dayuyu",
    # "xiaoli",
    # "ShirleyGames",
    # "lt.gkdacg.com",
    # "telegram@tgwebdrive",
    # "天堂巴比伦",
    # "LaiYin",
    # "逍遥2048",
    # "阿蕾",
    # "ed2k",
    # "指尖绅士",
    # "zx",
    # "三次郎",
    # "QW333",
    # "QW444",
    # "91acg.xyz",
    # "飞雪ACG论坛",
    # "@HanaYuki",
    # "哥特动漫王国@游龙逍遥",
    # "ashin791209@eyny",
    # "mengzhan-text",
    # "himengzhan.com",
    # "https://t.me/Zhzbzx",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    "123",
    ""
]
address_7z = "C:/Users/root/Desktop/7z/7-Zip/7z.exe"
UnZipPath = "D:/@game/new/moon"
UnZipFiles = os.listdir(UnZipPath)
for fileName in UnZipFiles:
    if (os.path.isdir(UnZipPath+"/"+fileName) == True):
            print(fileName+" 是文件夹，跳过\n")
            continue
    for passes in passwdList:
        command = "%s t %s\%s -p%s"%(address_7z,UnZipPath,fileName,passes)
        print(command)
        resultString = str(subprocess.Popen(command,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
        print(resultString+"\n")
        command2 = "%s x %s\%s -p%s -o\"%s/extracted1/%s\" -aoa"%(address_7z,UnZipPath,fileName,passes,UnZipPath,fileName)
        print(command2)
        resultString2 = str(subprocess.Popen(command2,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
        print(resultString2+"\n")