import os
import subprocess
import time
import re
from winreg import *
def deleteRubbish(unZipFolderPath):
    with open("E:\@home\celestial\code\python\myTools\\rubbishFile",encoding="utf-8") as tempList:
        fileNameList = tempList.readlines()
        rubbishFileList = []
        for i in fileNameList:
            rubbishFileList.append(i[0:len(i)-1])
    with open("E:\@home\celestial\code\python\myTools\\urlList",encoding="utf-8") as tempList:
        fileNameList = tempList.readlines()
        urlList = []
        for i in fileNameList:
            urlList.append(i[0:len(i)-1])
    with open("E:\@home\celestial\code\python\myTools\\ambiguityFileList",encoding="utf-8") as tempList:
        aList = tempList.readlines()
        ambiguityFileList = []
        for i in aList:
            ambiguityFileList.append(i[0:len(i)-1])
    for root, dirs, files in os.walk(unZipFolderPath):
        for dirctory in dirs:
            # 先删除文件夹
            if dirctory in rubbishFileList:
                rubbishFilePath = os.path.join(root,dirctory)
                if (dirctory == "Tool") == True & os.path.exists(rubbishFilePath+"nw.exe"):
                    # 移除游戏文件夹内的mtool
                    rmdir(rubbishFilePath) # 自定义函数
                    continue
                rmdir(rubbishFilePath) # 自定义函数
        for filename in files:
            # 后删除文件
            if filename in rubbishFileList:
                rubbishFilePath = os.path.join(root, filename)
                # readme 特例
                # 设置严格限制以避免误杀开发者和汉化者的readme
                try:
                    if (filename in ambiguityFileList):
                        try:
                            with open(rubbishFilePath) as f:
                                readmeText = f.read()
                                for url in urlList:
                                    urls = len(re.findall(url,readmeText))
                                    if(urls != 0):
                                        f.close()
                                        os.remove(rubbishFilePath)
                                        break
                                continue
                        except UnicodeDecodeError:
                            with open(rubbishFilePath,encoding='utf-8') as f:
                                try:
                                    readmeText = f.read()
                                    for url in urlList:
                                        urls = len(re.findall(url,readmeText))
                                        if(urls != 0):
                                            f.close()
                                            os.remove(rubbishFilePath)
                                            break
                                except:pass
                                continue
                    os.remove(rubbishFilePath)
                except PermissionError:
                    os.chmod(rubbishFilePath, 436 )
                    os.remove(rubbishFilePath)
                    if os.path.exists(rubbishFilePath):
                        print("无法删除"+rubbishFilePath+"，需要手动干预")
                        continue
    return 1

def rmdir(path):
    # 删除整个文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            fileToRemove = os.path.join(root, name)
            os.chmod(fileToRemove, 436 )
            os.remove(fileToRemove)
        for name in dirs:
            fileToRemove = os.path.join(root, name)
            os.chmod(fileToRemove, 436 )
            os.rmdir(fileToRemove)
    os.rmdir(path)

def selectPath():
    pass

def envirnmentCheck():
    keys = [
        "SOFTWARE\\7-Zip-Zstandard",
        "SOFTWARE\\7-Zip",
    ]
    subKey = "Path"
    errorCount = 0
    for key in keys:
        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        try:
            registry = OpenKey(reg, key)
            addressOf7z = QueryValueEx(registry,subKey)
            recheck = os.path.exists(str(addressOf7z)+"7z.exe")
            zstandardFlag = os.path.exists(str(addressOf7z)+"7za.exe")
            if(recheck == True & zstandardFlag == True):
                return addressOf7z[0]+"\\7z.exe",zstandardFlag
            elif(recheck == True & zstandardFlag == False):
                return addressOf7z[0]+"\\7z.exe",zstandardFlag
            else:
                raise
        except:
            errorCount += 1
            if(errorCount == 2):
                print("未找到 7zip，请访问 https://www.7-zip.org/ 下载后重新运行")
                print("访问 https://github.com/mcmilk/7-Zip-zstd 获得可以解压 tar.zst 的 7zip")
                print("-------------------")
                print("如果电脑内安装有 7-zip 依旧出现这条信息，说明 7-zip 被移动过，请手动指定")
                confirmInput = input("请按下 enter 键进入手动指定模式\n")
                if(confirmInput == []):
                    selectPath()
                else:
                    return 0
    return addressOf7z[0]+"\\7z.exe"

def getFileList(unZipFolderPath):
    zipSuffix = ["rar","zip",".7z","001","tar","zst"]
    extractList = []
    multiFileList = []
    for fileName in os.listdir(unZipFolderPath):
        originalName = fileName
        fileName = fileName.replace(" ","_").replace("&","_and_").replace("～","_").replace("[","【").replace("]","】").replace("'","_")
        try:
            os.replace(unZipFolderPath+"/"+originalName,unZipFolderPath+"/"+fileName)
        except:
            print("读取文件夹出错，请关闭文件浏览器")
            return extractList,multiFileList
        # 重命名以避免脚本执行错误
        if(re.findall(r'part[\d].rar$',fileName) != []):
            if(fileName.endswith("part1.rar")):
                extractList.append(fileName)
                continue
            else:
                multiFileList.append(fileName)
                continue
        # 处理 rar 分卷
        elif(re.findall(r'[.][\d]{3}$',fileName) != []):
            if(fileName.endswith(".001")):
                extractList.append(fileName)
                continue
            else:
                multiFileList.append(fileName)
        # 处理普通分卷
        elif(re.findall(r'[.].{2,3}$',fileName) == []):
            if(os.path.isdir(os.path.join(unZipFolderPath,fileName)) == False):
                extractList.append(fileName)
                continue
        # 处理无后缀文件
        elif(fileName[-3:] in zipSuffix):
            extractList.append(fileName)
            continue
        else:
            pass
    return extractList,multiFileList

def extract(addressOf7z,filePath,fileName):
    with open("E:\@home\celestial\code\python\myTools\\passwdList",encoding="utf-8") as tempList:
        aList = tempList.readlines()
        passwdList = []
        for i in aList:
            passwdList.append(i[0:len(i)-1])
    folderName = fileName
    suffixName = re.findall(r'[.].{2,3}$',fileName)
    if suffixName != []:
        folderName = fileName.replace(suffixName[0],"")
    for passes in passwdList:
        testCommand = "%s t %s\%s -p%s"%(addressOf7z,filePath,fileName,passes)
        extractCommand = "%s x %s\%s -p%s -o\"%s/extracted/%s\" -aoa"%(addressOf7z,filePath,fileName,passes,filePath,folderName)
        extractTarCommand = "%s x %s\%s -p%s -o\"%s\" -aoa"%(addressOf7z,filePath,fileName,passes,filePath)
        try:
            testResult = str(subprocess.Popen(testCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
            print(testResult)
            extractable = len(re.findall(r"Everything is Ok",testResult))+len(re.findall(r"There are data after the end of archive",testResult))
            if fileName[-3:] == "zst":
                extractable += 98
            match extractable:
                case 1:
                    os.system("start powershell.exe cmd /k '%s' "%extractCommand)
                    print(fileName+"即将被解压")
                    print("密码是："+passes)
                    return 1
                case 99:
                    os.system("start powershell.exe cmd /k '%s' "%extractTarCommand)
                    print(fileName+"即将被解压，这是一个 .tar.zst 文件")
                    print("密码是："+passes)
                    fileName = fileName[:-4]
                    extractCommand = "%s x %s\%s -p%s -o\"%s/extracted/\" -aoa"%(addressOf7z,filePath,fileName,passes,filePath)
                    # 重构指令
                    time.sleep(10)
                    os.system("start powershell.exe cmd /k '%s' "%extractCommand)
                    time.sleep(10)
                    print(fileName)
                    os.remove(os.path.join(filePath,fileName))
                    return 1
                case 0:
                    continue
        except PermissionError:
            print("访问被限制，请关闭所有的文件浏览器")
        return 0
    print("未知密码/无密码")
    return 0

def main():
    debugFlag = 1
    clearFlag = 0
    addressOf7z,zstandardFlag = envirnmentCheck()
    if(addressOf7z == 0):
        return
    unZipFolderPath = "D:\@game\\new"
    # unZipFolderPath = "D:\@game/games"
    unZipFileList,multiFileList = getFileList(unZipFolderPath)
    doneFileList = []
    for f in unZipFileList:
        if debugFlag == 0:
            extractResult = extract(addressOf7z,unZipFolderPath,f)
            if extractResult == 0:
                print(f+"无法被解压")
            else:
                doneFileList.append(f)
        else:
            pass
    match len(doneFileList):
        case 0:
            print("\n------------------------\n没有文件被解压，程序一分钟后退出")
        case _:
            print("如下文件已被解压：")
            for fileName in doneFileList:
                print(fileName)
            print("\n------------------------\n请等待解压，同时程序正在删除垃圾文件")
            clearFlag = deleteRubbish(unZipFolderPath)
            print("已完成，一分钟后自动关闭")
            time.sleep(60)
            # 解压后将源文件挪入done里面，但不是立即移动
            # 而是等一分钟，防止没有解压完成就被杀死
            doneFileList.extend(multiFileList)
            for fileName in doneFileList:
                try:
                    os.replace(os.path.join(unZipFolderPath,fileName),os.path.join(unZipFolderPath+"/done/"+fileName))
                except:
                    print(fileName+" 无法移动")
                    pass
    if clearFlag == 0:
        deleteRubbish(unZipFolderPath)
    else:
        pass
    
main()
# todo 引擎判断
# todo 分离垃圾文件名单，添加垃圾文件计数
# todo 判断是否解压完成
# todo 文件日志