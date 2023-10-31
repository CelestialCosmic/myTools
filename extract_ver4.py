import os
import subprocess
import time
import re
from winreg import *

class Base:
    upath = "D:\@game\\new"
    epath = "D:\@game\\new\extracted"
    logFile = "E:\@home\celestial\code\python\myTools\\log.txt"
    passwdFile = "E:\@home\celestial\code\python\myTools\\passwd.txt"
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
    def loadFile(filepath):
        tempList = []
        try:
            with open(filepath,encoding="utf-8") as file:
                tempList = file.read().splitlines()
                return tempList
        except:
            return tempList
    rubbishList = loadFile("E:\@home\celestial\code\python\myTools\\rubbishList")
    passwdList = loadFile("E:\@home\celestial\code\python\myTools\\passwdList")
    urlList = loadFile("E:\@home\celestial\code\python\myTools\\urlList")
    ambiguityList = loadFile("E:\@home\celestial\code\python\myTools\\ambiguityList")
        
class Log:
    def writeFile(content):
        with open(Base.logFile,"a",encoding="utf-8") as log:
            log.write(content+"\n")
    def recordSuccess(fileName,passwd):
        with open (Base.passwdFile,'a',encoding="utf-8") as log:
            log.write("|"+fileName +" | "+ passwd+"|")


def extract(file):
    enginedict = {
            "data.xp3":"majiro",
            # kr
            "SiglusEngine.exe":"siglus",
            # siglus
            "Engine":"Unreal",
            # UE
            "www":"mvmz-html", # 常规 html,大部分非单文件的 rpgmaker
            "nw.dll":"mvmz-html", # nwjs(mz)
            "app.asar":"mvmz-html", # tyrano
            # rpgmaker/html
            "UnityPlayer.dll":"unity", # 通用文件
            "Assembly-CSharp.dll":"unity", # mono
            "GameAssembly.dll":"unity", # cpp2il
            # unity
            "rgss3a":"vx-vxace", # vxace,龙头
            "rvproj2":"vx-vxace",
            "rgss2a":"vx-vxace", # vx,马头
            # vx/vxace
            "player.dll":"pgm",
            # pixelmakerMV
            "__init__.py":"renpy",
            # renpy
            "data.win":"gamemaker",
            # gamemaker
            ".pck":"godot", # 项目密钥文件
            # godot
            "cmvs":"cmvs", # 只见过一个游戏用的东西
            # cmvs
            "live.dll":"livemaker",
            # livemaker
            "nscript.dat":"nscripter",
            # nscripter
            "runtime.rts":"srpgstudio",
            # srpgstudio
            ".wolf":"wolf",
            # wolf
            ".swf":"flash", # flash
            ".cxt":"flash", # flash projector
            # flash
            ".ymv":"yuris",
            # YU-RIS Script Engine
            ".tad":"unknown",
            # 暂时未知的引擎
            "xaudio2_9redist.dll":"unknown",
            # 暂时未知的引擎
            }
    filepath = os.path.join(Base.upath,file)
    listCommand = "%s l %s"%(System.path7z,filepath)
    unzipObj = subprocess.Popen(listCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 列出文件列表
    engine = "unknown"
    engineFoundFlag = 0
    for line in iter(unzipObj.stdout.readline, b''):
        # 这种方式效率不高，但是不这么做无法分析完
        # 从文件列表中分辨引擎
         if(engineFoundFlag == 1):
             break
         else:
             for traits in enginedict.keys():
                 if(re.findall(traits,str(line)) != []):
                     engine = enginedict[traits]
                     engineFoundFlag = 1
    # 初始化解压指令
    for passes in Base.passwdList:
        testCommand = "%s t %s -p%s"%(System.path7z,filepath,passes)
        # testCommand = "%s t %s -p%s"%(System.path7z,filepath,passes)
        testResult = str(subprocess.Popen(testCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
    # 测试压缩包完整性和密码
    # 总在这卡住
        if(len(re.findall(r"Everything is Ok",testResult)) +
            len(re.findall(r"There are data after the end of archive",testResult))!= 0):
            outputpath = os.path.join(Base.epath,engine,os.path.splitext(file)[0])
            extractCommand = "%s x %s -p%s -o\"%s\" -aoa"%(System.path7z,filepath,passes,outputpath)
            # 构造解压指令
            # extractTarCommand = "%s x %s -p%s -o\"%s\" -aoa"%(System.path7z,filepath,passes,)
            break
    try:
        extractCommand = "%s x %s -p%s -o\"%s\" -aoa"%(System.path7z,filepath,passes,outputpath)
    except:
        print(filepath)
        return
    os.system("start powershell.exe cmd /k '%s' "%extractCommand)

class System:
    path7z = ""
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
                return addressOf7z[0]+"\\7z.exe"
            except FileNotFoundError:
                pass
        return False

    def getFileList():
        zipSuffix = ["rar","zip",".7z","001","tar","zst"]
        multiSuffix = ["002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020","021","022","023","024","025"]
        # 为了减少循环不使用for
        blackSuffix = ["exe","apk"]
        extractList = []
        multiFileList = []
        for fileName in os.listdir(Base.upath):
            originalName = fileName
            fileName = fileName.replace(" ","_").replace("&","_and_").replace("～","_").replace("[","【").replace("]","】").replace("'","_")
            # 重命名以避免执行错误
            Log.writeFile("文件原名"+originalName)
            Log.writeFile("文件现名"+fileName)
            try:
                os.replace(Base.upath+"/"+originalName,Base.upath+"/"+fileName)
            except:
                print("读取文件夹出错，请关闭文件浏览器")
                return extractList,multiFileList
            suffix = fileName[-3:]
            # 处理可解压但不是目标的文件
            if suffix in blackSuffix:
                continue
            # 处理 rar 分卷
            if suffix == zipSuffix[0]:
                if ((re.findall(r'part[\d].rar$',fileName) != []) == True & fileName.endswith("part1.rar")):
                    extractList.append(fileName)
                    continue
                else:
                    multiFileList.append(fileName)
                    continue
            elif suffix in zipSuffix:
                extractList.append(fileName)
                continue
            # 处理普通分卷
            if suffix in multiSuffix:
                multiFileList.append(fileName)
                continue
            # 处理无后缀文件
            elif(os.path.isdir(os.path.join(Base.upath,fileName)) == False):
                    extractList.append(fileName)
                    continue
            else:
                pass
        return extractList,multiFileList
    def deleteRubbish():
        encodingList = ["utf-8","gbk","shift-jis"]
        for root, dirs, files in os.walk(Base.epath):
            for dirctory in dirs:
                # 先删除文件夹
                if dirctory in Base.rubbishList:
                    rubbishFilePath = os.path.join(root,dirctory)
                    if (dirctory == "Tool") == True & os.path.exists(rubbishFilePath+"nw.exe"):
                        # 移除游戏文件夹内的mtool
                        Base.rmdir(rubbishFilePath) # 自定义函数
                        continue
                    Base.rmdir(rubbishFilePath) # 自定义函数
            for filename in files:
                # 后删除文件
                rubbishFilePath = os.path.join(root, filename)
                if filename in Base.rubbishList:
                    os.chmod(rubbishFilePath, 436)
                    os.remove(rubbishFilePath)
                elif (filename in Base.ambiguityList):
                    for lang in encodingList:
                        try:
                            with open(rubbishFilePath,encoding=lang) as f:
                                text = f.read()
                                for url in Base.urlList:
                                    if(len(re.findall(url,text)) != 0):
                                        f.close()
                                        os.remove(rubbishFilePath)
                                        break
                        except UnicodeDecodeError:
                            continue
                        except FileNotFoundError:
                            pass

    def moveDone(fileList):
        for fileName in fileList:
            try:
                os.replace(os.path.join(Base.upath,fileName),os.path.join(Base.upath+"/done/"+fileName))
            except:
                Log.writeFile(fileName+" 无法移动")
                pass

def main():
    System.path7z = System.environmentCheck()
    if System.path7z == False:
        Log.writeFile("没找到7z环境！")
        return
    extractList,multiFileList= System.getFileList()
    doneList = []
    readflag = 0
    for file in extractList:
        print(file)
        if(extract(file) == False):print(file+" error")
        else:doneList.append(file)
        readflag = 1
    if(doneList != []):
        time.sleep(60)
        System.moveDone(doneList)
        System.moveDone(multiFileList)
    System.deleteRubbish()



main()
# todo 分辨分卷压缩包
# todo 解决7z编码问题 (x崩溃了不解决了)