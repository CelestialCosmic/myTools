import os
import subprocess
import time
import re
global passwdList
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
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    ""
]
global doneFileList
doneFileList = []

def extract(addressOf7z,filePath,fileName):
    # 尝试无密码解压
    testNoPasswdCommand = "%s t %s\%s "%(addressOf7z,filePath,fileName)
    testResultString1 = str(subprocess.Popen(testNoPasswdCommand,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read())
    okString = re.findall(r"Everything is Ok",testResultString1)
    extraDataString = re.findall(r"There are data after the end of archive",testResultString1)
    if(okString != []):
        print(fileName+"即将被解压\n没有密码\n")
        doneFileList.append(fileName)
        commandNoPasswd = "%s x %s\%s -o\"%s/extracted1/%s\" -aoa"%(addressOf7z,filePath,fileName,filePath,fileName)
        os.system("start powershell.exe cmd /k '%s' "%commandNoPasswd)
    elif(extraDataString != []):
        print(fileName+"即将被解压\n没有密码\n请注意，压缩包内有额外数据")
        doneFileList.append(fileName)
        commandNoPasswd = "%s x %s\%s -o\"%s/extracted1/%s\" -aoa"%(addressOf7z,filePath,fileName,filePath,fileName)
        os.system("start powershell.exe cmd /k '%s' "%commandNoPasswd)
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

def main():
    # 这个函数负责处理文件夹路径和7z路径
    addressOf7z = "C:/Users/root/Desktop/7z/7-Zip/7z.exe"
    # unZipPath = input().replace("\\","/").rstrip("/")
    # 标记解压路径，如果路径最后一位带杠则去掉，方便处理
    unZipPath = "D:/@game/new"
    UnZipFiles = os.listdir(unZipPath)
    try:
        os.mkdir(unZipPath+"/done")
    except:
        pass
    for fileName in UnZipFiles:
        originalName = fileName
        fileName = fileName.replace(" ","_")
        # 将空格转换为下横杠
        os.replace(unZipPath+"/"+originalName,unZipPath+"/"+fileName)
        extensionName = re.findall(r'[.][\d]{3}',fileName[-4:])
        extensionName2 = re.findall(r'.zst',fileName[-4:])
        if (os.path.isdir(unZipPath+"/"+fileName) == True):
            print(fileName+" 是文件夹，跳过\n")
            continue
            # 过滤文件夹
        elif(extensionName2 != []):
            print(fileName+"是.tar.zst文件，需要手动解压，跳过")
            # .tar.zst使用7z命令行解压出来的是元数据，只能手动解一层再过脚本
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
    
    if(len(list(doneFileList)) != 0):
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
main()