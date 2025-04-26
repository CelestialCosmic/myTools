import os
import subprocess
import time
import re
from winreg import *

# 这个类包含了所有的文件操作
class File:
    # 删除整个文件夹（包含只读）
    def rmdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                fileToRemove = os.path.join(root, name)
                os.chmod(fileToRemove, 436)
                os.remove(fileToRemove)
            for name in dirs:
                fileToRemove = os.path.join(root, name)
                os.chmod(fileToRemove, 436)
                os.rmdir(fileToRemove)
        os.rmdir(path)
        return 1
    # 读取文件，返回列表
    def loadFile(filepath):
        tempList = []
        try:
            with open(filepath,encoding="utf-8") as file:
                tempList = file.read().splitlines()
                return tempList
        except:
            return tempList
    def extract(file,pathOf7z):
        for passes in Path.passwdList:
            testCommand = "%s t %s -p%s"%(pathOf7z,file,passes)
            p = subprocess.Popen(testCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
            if re.findall(r"Everything is Ok|There are data after the end of archive",str(p)):
                extractCommand = "%s x %s -p%s -o\"%s\" -aoa"%(pathOf7z,file,passes,Path.FilePath_extracted)
                os.system("start powershell.exe cmd /k '%s' "%extractCommand)
                return True
        return False
    def moveDone(fileList):
        for fileName in fileList:
            try:
                os.replace(os.path.join(Path.FilePath_toExtract,fileName),os.path.join(Path.FilePath_extracted+fileName))
            except:
                pass

# 这个类包含了文件路径读取和处理
class Path:
    FilePath_toExtract = "D:/game/download"
    FilePath_extracted = "D:/game/extracted"
    FilePath_toMove = "D:/game/done"
    FilePath_passwdList = "D:/code/tools/extract/passwdList"
    FilePath_rubbishList = "D:/code/tools/extract/rubbishList"
    FilePath_ambiguityList = "D:/code/tools/extract/ambiguityList"
    FilePath_urlList = "D:/code/tools/extract/urlList"
    passwdList = File.loadFile(FilePath_passwdList)
    rubbishList = File.loadFile(FilePath_rubbishList)
    ambiguityList = File.loadFile(FilePath_ambiguityList)
    urlList = File.loadFile(FilePath_urlList)
    def environmentCheck():
        keys = [
            "SOFTWARE\\7-Zip-Zstandard",
            "SOFTWARE\\7-Zip",
        ]
        for key in keys:
            try:
                reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
                registry = OpenKey(reg, key)
                addressOf7z = QueryValueEx(registry,"Path")
                if(addressOf7z[0] == "C:\\Program Files\\7-Zip\\"):
                    return "c:\\progra~1\\7-Zip\\7z.exe"
                return addressOf7z[0]+"\\7z.exe"
            except FileNotFoundError:
                pass
        return False
    def classify():
        extractList = []
        multiList = []
        zipSuffix = ["rar","zip",".7z","001","tar","zst"]
        specialSuffix = ["tar.zst.rar"]
        multiSuffix = ["002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025"]
        for file in os.listdir(Path.FilePath_toExtract):
            unzipFilePath = os.path.join(Path.FilePath_toExtract,file)
            if(os.path.isfile(unzipFilePath) == True):
                classifiedFlag = 0
                for suffix in zipSuffix:
                    if(file.endswith(suffix)):
                        extractList.append(unzipFilePath)
                        classifiedFlag = 1
                        break
                if(classifiedFlag != 1):
                    for suffix in multiSuffix:
                        if(file.endswith(suffix)):
                            multiList.append(unzipFilePath)
                            break
        return extractList,multiList
                
def main():
    pathOf7z = Path.environmentCheck()
    if(pathOf7z == False):
        return
    extractList,multiList = Path.classify()
    print(extractList)
    doneList = []
    for file in extractList:
        result = File.extract(file,pathOf7z)
        if(result == True):
            doneList.append(file)
    print(doneList)
    # time.sleep(50)
    if(len(extractList) == len(doneList)):
        File.moveDone(doneList)
        File.moveDone(multiList)
    elif(doneList != []):
        File.moveDone(doneList)
    else:
        return
main()