import zipfile
import rarfile
import py7zr
import os
import re
global PasswdList
PasswdList = [
    "",
    "半夏",
    "莱茵",
    "dayuyu",
    "xiaoli",
    "ShirleyGames",
    "lt.gkdacg.com",
    "telegram@tgwebdrive",
    "天堂巴比伦",
    "LaiYin",
    "逍遥2048",
    "阿蕾",
    "ed2k"
]
def main():
    # UnZipPath = input("输入需要解压的文件夹\n")
    global UnZipPath
    UnZipPath = "/home/celestial/storage/game/games/04/"
    if(UnZipPath[-1] == "/"):
        UnZipPath = UnZipPath.rstrip("/")
    UnZipFiles = os.listdir(UnZipPath)
    rarMulti = [
        "part2.rar",
        "part3.rar",
        "part4.rar",
        "part5.rar",
        "part6.rar",
        "part7.rar",
        "part8.rar",
        "part9.rar",
    ]
    errorList = []
    for i in UnZipFiles:
        if os.path.isdir(UnZipPath+"/"+i) == True: # 过滤文件夹
            print(i+" 为文件夹，即将跳过")
            continue
        if(i[-3:] == ".7z"): # 解压常规的压缩包类型
            print("以 7z 方式解压 "+i)
            extract7z(i) #[:-3]
        elif(i[-3:] == "zip"):
            print("以 zip 方式解压 "+i)
            extractZip(i) #[:-4]
            continue 
        elif(i[-3:] == "rar"):
            print("以 rar 方式解压 "+i)
            extractRar(i) #[:-4]
        elif(i[-3:] == "001"):
            print("以分卷压缩方式解压 "+i)
            extract001(i) #[:-8]
        else:
            try:
                if(int(i[-3:]) - 1000 < 0):  # 检测非 001 的分卷
                    continue
            except(ValueError): # 处理非分卷压缩的文件
                errorList.append(i)
                continue
            errorList.append(i)
    for j in errorList: # 输出无法处理的文件
        print(j+"不是常规文件，需要单独处理")
def extract001(i):
    if(i[-7:] == ".7z.001"):
        extract7z(i)
    elif(i[-7:] == "zip.001"):
        extractZip(i)
    print(i+" 解压完成")
def extractRar(i):
    for passes in PasswdList:
        try:
            with rarfile.RarFile(UnZipPath+"/"+i,"r") as RarCompressedFile:
                RarCompressedFile.extractall(pwd=passes,path=UnZipPath+"/extracted/%s" %i[:-4])
            print(i+" 解压完成")

        except(rarfile.NeedFirstVolume):
            print(i+" 为分卷的一部分，跳过") # 处理 NeedFirstVolume 报错
            break
    pass
def extractZip(i):
    for passes in PasswdList:
        with zipfile.ZipFile(UnZipPath+"/"+i,"r") as ZipCompressedFile:
            ZipCompressedFile.extractall(pwd=passes,path=UnZipPath+"/extracted/%s" %i[:-4])
    pass
    print(i+" 解压完成")
def extract7z(i):
    for passes in PasswdList:
        try:
            with py7zr.SevenZipFile(UnZipPath+"/"+i, mode='r', password=passes) as SevenZipFile:
                    SevenZipFile.extractall(path=UnZipPath+"/extracted/%s" %i[:-3])
        except(py7zr.UnsupportedCompressionMethodError):
            pass # 无视 UnsupportedCompressionMethodError 报错
        except(py7zr.Bad7zFile):
            print("检测到是 7z 分卷压缩包，使用其他处理方式")
            SevenZipFileList = []
            for j in range(1,100):
                MultiFilePath = UnZipPath+"/"+i[:-1]+str(j)
                if(os.path.exists(MultiFilePath) == True):
                    SevenZipFileList.append(MultiFilePath)
                elif(os.path.exists(MultiFilePath == False)):
                    break
            with open('result.7z', 'ab') as outfile:  # append in binary mode
                for fname in SevenZipFileList:
                    with open(fname, 'rb') as infile:        # open in binary mode also
                        outfile.write(infile.read())
                        # https://stackoverflow.com/questions/73832254/why-am-i-getting-this-error-when-trying-to-unzip-this-7z-file-using-python
            with py7zr.SevenZipFile("result.7z", "r") as archive:
                archive.extractall()
            os.unlink("result.7z")
    print(i+" 解压完成")
main()