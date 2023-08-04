import os
import subprocess
import time
import re
global passwdList
global zipSuffix
global debugSign
debugSign = 0
zipSuffix = [
    ".rar",
    ".zip",
    ".7z",
    ".001",
    ".tar",
    ".zst",
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
    ""
]
passwdList = [
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
    ""
]
global doneFileList
doneFileList = []

def moveDone(unZipPath):
    if(doneFileList !=[]):
        print("如下文件已被解压：")
        for fileName in doneFileList:
            print(fileName)
        print("\n------------------------\n请等待解压，一分钟后自动关闭")
        time.sleep(60)
        for fileName in doneFileList:
            try:
                os.replace(unZipPath+"/"+fileName,unZipPath+"/done/"+fileName)
                # 解压后将源文件挪入done里面，但不是立即移动
                # 而是等一分钟，防止没有解压完成就被杀死
            except:
                pass
    else:
        print("\n------------------------\n没有文件被解压，程序退出")

def extract(addressOf7z,filePath,fileName):
    # 尝试无密码解压
    testNoPasswdCommand = "%s t %s\%s "%(addressOf7z,filePath,fileName)
    try:
        testResultString1 = str(subprocess.Popen(testNoPasswdCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
        extraDataString = re.findall(r"There are data after the end of archive",testResultString1)
        okString = re.findall(r"Everything is Ok",testResultString1)
    except PermissionError:
        print("访问被限制，请关闭所有的文件浏览器")
    if(okString != []):
        print(fileName+"即将被解压\n没有密码\n")
        extractPowershellNoPasswd(addressOf7z,filePath,fileName)
        # doneFileList.append(fileName)
        # commandNoPasswd = "%s x %s\%s -o\"%s/extracted1/%s\" -aoa"%(addressOf7z,filePath,fileName,filePath,fileName)
        # os.system("start powershell.exe cmd /k '%s' "%commandNoPasswd)
    elif(extraDataString != []):
        print(fileName+"即将被解压\n没有密码\n请注意，压缩包内有额外数据")
        extractPowershellNoPasswd(addressOf7z,filePath,fileName)
    # 测试密码和解压文件
    else:
        for passes in passwdList:
            testPasswdCommand = "%s t %s\%s -p%s"%(addressOf7z,filePath,fileName,passes)
            testResultString2 = str(subprocess.Popen(testPasswdCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
            # 将指令转换为一个子进程，使用7z测试密码和完整性，并将执行的结果转化为字符串供后面使用
            okString = re.findall(r"Everything is Ok",testResultString2)
            if(okString != []):
                print(fileName+"即将被解压\n密码是"+passes+"\n")
                extensionName = re.findall(r'[.][\d]{3}',fileName[-4:])
                if(extensionName == []):
                    doneFileList.append(fileName)
                commandHasPasswd = "%s x %s\%s -p%s -o\"%s/extracted1/%s\" -aoa"%(addressOf7z,filePath,fileName,passes,filePath,fileName)
                os.system("start powershell.exe cmd /k '%s' "%commandHasPasswd)
                # 使用7z解压带密码的文件
                break

def extract(addressOf7z,fullPath):
    testNoPasswdCommand = "%s t %s "%(addressOf7z,fullPath)
    try:
        testResultString1 = str(subprocess.Popen(testNoPasswdCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
        extraDataString = re.findall(r"There are data after the end of archive",testResultString1)
        okString = re.findall(r"Everything is Ok",testResultString1)
    except PermissionError:
        print("访问被限制，请关闭所有的文件浏览器")

def extractPowershellNoPasswd(addressOf7z,filePath,fileName):
    doneFileList.append(fileName)
    strList = re.findall(r'\w*(.\w*)',fileName)
    for result in strList:
        if result in zipSuffix:
            stripedFileName = fileName.replace(result,"")
    if(debugSign == True):
        return
    else:
        commandNoPasswd = "%s x %s\%s -o\"%s/extracted1/%s\" -aoa"%(addressOf7z,filePath,fileName,filePath,stripedFileName)
        os.system("start powershell.exe cmd /k '%s' "%commandNoPasswd)

def check7z(home7z):
    addr = home7z+"/7z.exe"
    if (os.path.exists(addr)):
        pass
    else:
        print("未找到 7zip，请手动指定安装路径或访问\nhttps://www.7-zip.org/\n下载后重新运行")
        print("----------")
        print("也访问 https://github.com/mcmilk/7-Zip-zstd 获得可以解压 tar.zst 的 7zip")
        home7z = input("如果现在有7z，请输入它所在文件夹的路径\n")
        check7z(home7z)
    return home7z

def main():
    # 这个函数负责处理文件夹路径和7z路径
    home7z = "C:/apps/system/7-Zip"
    home7z = check7z(home7z)
    addressOf7z = home7z+"/7z.exe"
    # unZipPath = input("输入解压路径\n").replace("\\","/").rstrip("/")
    # 标记解压路径，如果路径最后一位带杠则去掉，方便处理
    unZipPath = "D:/@game/new/workshop"
    UnZipFiles = os.listdir(unZipPath)
    try:
        os.mkdir(unZipPath+"/done")
    except:
        pass
    for fileName in UnZipFiles:
        originalName = fileName
        fileName = fileName.replace(" ","_").replace("&","and").replace("～","_")
        print(fileName)
        # 将空格转换为下横杠
        # & 符号也会影响脚本执行，一起换掉
        try:
            os.replace(unZipPath+"/"+originalName,unZipPath+"/"+fileName)
        except:
            moveDone(unZipPath)
            print("权限出错，请移除没有权限的文件夹")
            return
        extensionName = re.findall(r'[.][\d]{3}',fileName[-4:])
        extensionName2 = re.findall(r'.zst',fileName[-4:])
        if (os.path.isdir(unZipPath+"/"+fileName) == True):
            print(fileName+" 是文件夹，跳过\n")
            continue
            # 过滤文件夹
        elif(extensionName2 != []):
            print(fileName+"是.tar.zst文件，需要手动解压，将移入 tar 文件夹")
            # .tar.zst使用7z命令行解压出来的是元数据，只能手动解一层再过脚本
            try:
                os.mkdir(unZipPath+"/tar")
            except:pass
            os.replace(unZipPath+"/"+fileName,unZipPath+"/tar/"+fileName)
            continue
        elif(extensionName != []):
            if(extensionName[0] == ".001"):
                extract(addressOf7z,unZipPath,fileName)
                for i in range(1,1000,1):
                    multiFileName = fileName.replace("1",str(i))
                    if(os.path.exists(unZipPath+"/"+multiFileName) == True):
                            doneFileList.append(multiFileName)
                            # 将所有分卷全部算作解压完成
                    else:
                        break
        # 处理文件夹和分卷
        else:
            extract(addressOf7z,unZipPath,fileName)
            # 为了防止在开始解压前文件就被移走
    moveDone(unZipPath)


main()
# 处理 文件名、目录名或卷标语法不正确 的问题

# ERROR: 文件名、目录名或卷标语法不正确。
# D:\@game\new\moon\私立さくらんぼ小学校_子作り練習授業_Love s_Right_セックスしないと即死刑_exeC84.7z -p半夏 -o D:\@game\new\moon\extracted1\私立さくらんぼ小学校_子作り練習授業_Loves_Right_セックスしないと即死刑_exeC84.7z