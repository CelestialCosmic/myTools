# tar.zst
import tempfile
import tarfile
import zstandard
# 其他
import subprocess
import os
import re
from multiprocessing import Pool
# 现成函数
def loadList(filepath):
    listA = []
    with open(filepath,encoding="utf-8") as file:
        listA = file.read().splitlines()
        return listA
    
def loadDict(filepath):
    d = {}
    with open(filepath,encoding="utf-8") as f:
        for line in f:
            if("#" in line):
                continue
            else:
                (key, val) = line.strip("\n").split(":")
                d[key] = val
    return d

def detection(file_list):
    if(len(file_list) > 100):
        new_file_list = file_list[-50:]
        new_file_list.extend(file_list[:50])
        file_list = new_file_list
    engineDetectFlag = 0
    engineType = "unknown"
    firstDircount = 0
    for file in file_list:
        counts = file.count("/")
        fileName = file.split("/")[-1]
        # 输出一级目录下面的东西
        if((fileName == "") & (counts == 1)):
            firstDircount += 1
        elif((fileName != "") & (counts == 0)):
            firstDircount += 1
            # 这个是为了处理一级文件夹只有一个，二级文件夹也只有一个的情况
        # 测试游戏引擎
        if(engineDetectFlag == 1):
            continue
        elif(fileName in Config.engines.keys()):
            engineType = Config.engines[fileName]
            engineDetectFlag = 1
        # 检测到引擎后停止，文件检测数量达到100个时停止，如果文件少于100个且没检测出来，自然停止
        # 发现有文件夹在最后面的，改成检测头尾50个文件，并取消100的限制，取消break
    if(firstDircount != 1):
        parentDir = Config.file_path.split("/")[-1].split(".")[0]
        output_path = os.path.join(Config.output_path,engineType,parentDir)
    else:
        output_path = os.path.join(Config.output_path,engineType)
    if(Config.extract_flag == True):
        try:
            os.makedirs(output_path)
        except FileExistsError:
            pass
    return output_path

def tarzst(file_path,passwd):
    with tempfile.TemporaryDirectory() as tempdir:
        cmd = """7z x "%s" -p%s -o%s -aoa"""%(file_path,passwd,tempdir)
        subprocess.run(cmd,capture_output=True, text=True)
        # 解压到临时目录，如果硬盘满了这里会报错
        for file in os.listdir(tempdir):
            dctx = zstandard.ZstdDecompressor()
            with tempfile.TemporaryFile(suffix=".tar") as ofh:
                with open(os.path.join(tempdir,file),"rb") as ifh:
                    dctx.copy_stream(ifh, ofh)
                # 将tar.zst转为tar
                ofh.seek(0)
                with tarfile.open(fileobj=ofh) as z:
                    output_path = detection(z.getnames())          
                    print(output_path)
                    z.extractall(output_path)

def common(file_path): 
    file_list = []
    for passwd in Config.password:
        cmd = """E:/software/7-Zip/7z.exe t "%s" -p%s"""%(file_path,passwd)
        output = subprocess.run(cmd,capture_output=True, text=True)
        if("Everything is Ok" in output.stdout):
            print(passwd)
            cmd = """E:/software/7-Zip/7z.exe l "%s" -p%s"""%(file_path,passwd)
            try:
                output = subprocess.getoutput(cmd).split("\n")
            except UnicodeDecodeError:
                print(file_path)
                continue
            output = reversed(output)
            for line in output:
                if re.match(r'^[\d]{4}',line) == None:
                    continue
                else:
                    file2 = re.sub(r'\\',"/",line[53:])
                    file_list.append(file2)
            file_list.pop(0)
            output_path = detection(file_list)
            if(Config.extract_flag == True):
                if(file_path.endswith("tar.zst.rar")):
                    # tarzst(file_path,passwd)
                    pass
                    return True
                else:
                    cmd = """E:/software/7-Zip/7z.exe x "%s" -p%s -o%s -aoa"""%(file_path,passwd,output_path)
                    subprocess.run(cmd,capture_output=True, text=True)
                    return True
    print(file_path)
    print("出错或未找到密码")
    return False


def main():
    numToDo = 0
    numDone = 0
    pool = Pool(Config.poolmax)
    Config.password = loadList("E:/code/tools/extract/passwdList")
    Config.engines = loadDict("E:/code/tools/extract/engineList")
    # 读取文件
    file_list = os.listdir(Config.input_path)
    numToDo = len(file_list)
    for file_name in file_list:
        file_path = os.path.join(Config.input_path,file_name)
        Config.file_path = file_path
        if(os.path.isfile(file_path)):
            if (file_path.endswith(tuple([".zip","z01",".exe","tar.zst.rar","rar",".001",".7z",".jpg"])) & (not file_path.endswith(tuple(["part2.rar","part3.rar","part4.rar","part5.rar"])))):
                result = pool.apply_async(common(file_path))
                if(result == False):
                    file_list.pop(file_name)
            elif file_path.endswith('.apk'):
                numDone += 1
                try:
                    os.makedirs(os.path.join(Config.output_path,"apk"))
                    os.replace(file_path,os.path.join(Config.output_path,"apk",file_name))
                except:
                    os.replace(file_path,os.path.join(Config.output_path,"apk",file_name))
    for file_name in file_list:
        file_path = os.path.join(Config.input_path,file_name)
        try:
            out = os.path.join(Config.output_path,"done",file_name)
            os.replace(file_path,out)
            numDone += 1
        except PermissionError:
            pass
        except FileNotFoundError:
            pass
        # 权限又出问题了
    return numToDo,numDone

def clear(p):
    # 权限和文件夹删除
    print("开始清理工作")
    numFile = 0
    numDir = 0
    if(p == None):
        clear_path = Config.output_path
    else:
        clear_path = p
    rubbishList = loadList("E:/code/tools/extract/rubbishlist")
    for root,dirs,files in os.walk(clear_path):
        for file in files:
            # print(file)
            if(file in rubbishList):
                numFile += 1
                path = (os.path.join(root,file))
                os.system(f"attrib -r -h -s \"{path}\" /s > {os.devnull}")
                os.remove(path)
        for dira in dirs:
            # print(dira)
            if(dira in rubbishList):
                path = (os.path.join(root,dira))
                os.system(f"attrib -r -h -s \"{path}\" /s > {os.devnull}")
                for root2, dirs2, files2 in os.walk(path, topdown=False):
                    for name in files2:
                        os.remove(os.path.join(root2, name))
                        numFile += 1
                    for name in dirs2:
                        numDir += 1
                        os.rmdir(os.path.join(root2, name))
                        # 非空文件夹rmdir无效
    return numDir,numFile

# 基础配置
class Config:
    mode = 1
    input_path = "E:/game/download"
    output_path = "E:/game/extracted2"
    extract_flag = True
    password = []
    engines = []
    poolmax = 24
    file_path = ""

if __name__ == "__main__":
    if(Config.mode == 0):
        Config.input_path = input("输入路径\n")
        numToDo,numDone = main()
        numDir,numFile = clear(Config.output_path)
        print("需处理%d个文件,%d个已处理"%(numToDo,numDone))
        print("清理了%d个文件,%d个文件夹"%(numFile,numDir))
    elif(Config.mode == 1):
        path = input("输入清理路径\n")
        if path == " ":
            numDir,numFile = clear(path)
        else:
            numDir,numFile = clear(Config.output_path)
        print("清理了%d个文件,%d个文件夹"%(numFile,numDir))
    else:
        print("无行动，结束")
