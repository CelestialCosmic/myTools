import os
import subprocess
import time
import re
from winreg import *

def deleteRubbish(unZipFolderPath):
    rubbishFileList = [
    "【重要必须看】更多免费资源.txt",
    "合作资源",
    "本资源来自萌站：himengzhan.com  其他皆为山寨盗链，谨防被骗.url",
    "地址发布页（务必收藏好呀）",
    "1W＋免费游戏分享，加入莱茵图📖书馆 【黄油、RPG、GAL、SLG、ADV、ACT、3D......】",
    "1W＋免费游戏分享，加入莱茵图📖书馆 【黄油、RPG、GAL、SLG、ADV、ACT、3D......】.url",
    "超多涩涩视频，加入莱茵放映室🎥 【里番、3D、动态漫、同人......】",
    "MTool_MapDataCache",
    "点击此处开启汉化.bat",
    "谨防被骗.png",
    "翻墙软件及教程 .7z",
    "翻墙软件及教程.7z",
    "翻墙软件及教程.rar",
    "更多游戏请点击.url",
    "资源说明.txt",
    "点击Game.exe启动游戏.txt",
    "汉化留言，禁止删除.txt",
    "萌站最新网址发布.url",
    "游戏动漫资源网站【务必收藏}.url",
    "萌站网址发布器V1.7.7.apk",
    "萌影在线.apk",
    "1W＋免费游戏分享，加入莱茵图书馆.txt",
    "莱茵放映室🎥 【里番、3D、动态漫、同人......】.png",
    "莱茵图📖书馆 【黄油、RPG、GAL、SLG、ADV、ACT、3D......】.png",
    "超多涩涩视频，加入莱茵放映室🎥 【里番、3D、动态漫、同人......】.url",
    "了解最详细解压码请加入我们.txt",
    "Tool",
    "quzimingyue",
    "免费游戏资源点这.url",
    "本资源来自爱社：isyx001.cc 其他皆为司马盗链，谨防被骗 - 副本",
    "此游戏由黄油中心（老婆社）免费分享，电报搜索@LPS99.txt",
    "点击购买机场用于翻墙.lnk",
    "点击加入免费黄游频道（需要翻墙）.lnk",
    "更多安卓黄油点击下载.lnk",
    "更多免费黄油下载地址（记得收藏）.txt",
    "更多资源（请务必收藏）1 - 副本.lnk",
    "请先读我 - 副本.txt",
    "wodeshujia",
    "破解VIP方法.txt",
    "游玩前需注意事项.txt",
    "琉璃神社 ★ HACG.me.url",
    "游戏如果无法打开 使用帮助.txt",
    "e3388342@eyny",
    "游戏汉化版启动方法必须看.txt",
    "与工具一同启动.bat",
    "此游戏由老婆社免费分享，电报搜索@LPS99.txt",
    "点击购买机场用于翻墙.url",
    "点击加入免费黄游频道（需要翻墙）.url",
    "启动机翻.bat",
    "MTool_MapDataCache",
    "嘿嘿.txt",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "America.png",
    "更多免费资源（务必收藏）XP.txt",    
    ]

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
                os.remove(rubbishFilePath)

def rmdir(path):
    # 删除整个文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
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
    zipSuffix = [
    "rar",
    "zip",
    ".7z",
    "001",
    "tar",
    "zst",
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
    # ""
    ]
    extractList = []
    multiFileList = []
    for fileName in os.listdir(unZipFolderPath):
        originalName = fileName
        fileName = fileName.replace(" ","_").replace("&","_and_").replace("～","_").replace("[","【").replace("]","】")
        os.replace(unZipFolderPath+"/"+originalName,unZipFolderPath+"/"+fileName)
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
            
    
    print(extractList)
    # print(multiFileList)
    return extractList,multiFileList

def extract(addressOf7z,filePath,fileName):
    passwdList = [
    "",
    "半夏",
    "莱茵",
    "https://t.me/RhineLibrary",
    "dayuyu",
    "xiaoli",   
    "ShirleyGames",
    "lt.gkdacg.com",
    "telegram@tgwebdrive",
    "天堂巴比伦",
    "LaiYin",
    "逍遥2048",
    "阿蕾",
    "ed2k",
    "指尖绅士",
    "zx",
    "三次郎",
    "QW333",
    "QW444",
    "91acg.xyz",
    "飞雪ACG论坛",
    "@HanaYuki",
    "哥特动漫王国@游龙逍遥",
    "ashin791209@eyny",
    "mengzhan-text",
    "himengzhan.com",
    "https://t.me/Zhzbzx",
    "awacg.com@黄瓜侠",
    "GG汉化组",
    "昨晚晚安",
    "iiacg.cc",
    "951",
    "MyRealDesire",
    "jdt",
    "频道关注@Zhzbzx",
    "杏铃天下第一可爱",
    "t.me/XLDTGPD",
    "⑨",
    # "",
    # "",
    # "",
    # "",
    ]
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
            extractable = len(re.findall(r"Everything is Ok",testResult))+len(re.findall(r"There are data after the end of archive",testResult))
            print(extractable)
            if fileName[-3:] == "zst":
                extractable += 98
            print(extractable)
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
                    pass
        except PermissionError:
            print("访问被限制，请关闭所有的文件浏览器")
        return 0
    return 0

def main():
    debugFlag = 0
    addressOf7z,zstandardFlag = envirnmentCheck()
    if(addressOf7z == 0):
        return
    unZipFolderPath = "D:\@game/new"
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
            print("\n------------------------\n请等待解压，一分钟后自动关闭")
            # 解压后将源文件挪入done里面，但不是立即移动
            # 而是等一分钟，防止没有解压完成就被杀死
            time.sleep(60)
            doneFileList.extend(multiFileList)
            for fileName in doneFileList:
                try:
                    os.replace(os.path.join(unZipFolderPath,fileName),os.path.join(unZipFolderPath+"/done/"+fileName))
                except:
                    pass
    deleteRubbish(unZipFolderPath)
    
main()
# todo 添加tar.zst支持