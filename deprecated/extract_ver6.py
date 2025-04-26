import os,stat
import re
import time
import subprocess
import shutil

class ZipFile:
    archievetype = ""
    filename = ""
    passwd = ""
    input_path = ""
    output_path = ""
    args = ""
    engine_type = "unknown"
    pkgs = []
    one_folder = 0

def collect(route):
    print("开始测试工作")
    enginedict = InputFiles.loadDict(InputFiles.engineList)
    passwdList = InputFiles.loadList(InputFiles.passwdList)
    extract_list = []
    for file in os.listdir(route):
        file_properties = ZipFile()
        file_route = os.path.join(route,file)
        file_properties.input_path = file_route
        file_properties.filename = file
        # 测试密码
        for passwd in passwdList:
            cmd = """7z t "%s" -p%s"""%(file_route,passwd)
            output = subprocess.run(cmd,capture_output=True, text=True)
            if("Everything is Ok" in output.stdout):
                file_properties.passwd = passwd
                cmd = """7z l "%s" -p%s"""%(file_route,file_properties.passwd)
                try:
                    output = subprocess.getoutput(cmd)
                except UnicodeDecodeError:
                    # 处理 shift-jis 压缩包
                    # 这个并不准确，因为可能不报
                    try:
                        print(cmd)
                        output = subprocess.getoutput(cmd+" -mcp=932") 
                    except:
                        print(cmd)
                        output = subprocess.getoutput(cmd+" -mcp=936") 
                        file_properties.args += " -mcp=936"
                    else:
                        file_properties.args += " -mcp=932"
                # 收集压缩包内结构
                zip_structure = re.findall(r'D[.]{4}|[.]{4}A',output)
                if(len(zip_structure) >= 2):
                    if ((zip_structure[0] == "D....") & (zip_structure[1] == "....A")):
                        file_properties.one_folder = 1
                # 收集压缩包类型
                try:
                    file_properties.archievetype = re.findall(r'Type = [\S]{1,}',output)[0].split(" ")[2]
                except:
                    pass
                # 收集分卷
                # 跳掉分卷
                if(file_properties.archievetype == "Split"):
                    filename = file_properties.filename.split(".")[0]
                    for file in os.listdir(route):
                        if(re.findall(filename,file) != []):
                            filepath = os.path.join(route,file)
                            file_properties.pkgs.append(filepath)
                # 收集引擎信息
                for key in enginedict:
                    if(len(re.findall(key,output))!=0):
                        file_properties.engine_type = enginedict[key]
                        break
                # 设置输出路径
                if(file_properties.archievetype != "zstd"):
                    file_properties.output_path = \
                        os.path.join(InputFiles.output_route,file_properties.engine_type,
                                    file_properties.filename.replace(" ","_").replace("&","_"))
                elif(file_properties.one_folder == 1):
                        file_properties.output_path = \
                        os.path.join(InputFiles.output_route)
                else:
                    file_properties.output_path = \
                        os.path.join(InputFiles.output_route,
                                    file_properties.filename.split(".")[0].replace(" ","_").replace("&","_"))
                extract_list.append(file_properties)
                p = file_properties.passwd
                if(p == ""):p = "无"
                info = """
                文件名：%s
                压缩包类型：%s
                引擎类型：%s
                密码：%s
                """%(
                    file_properties.filename,
                    file_properties.archievetype,
                    file_properties.engine_type,
                    p
                )
                print(info)
                break
            else:continue
    print("""共测试 %d 个文件"""%(len(os.listdir(route))))
    return extract_list

def extract(pkgs):
    print("开始解压文件")
    donepkgs = []
    for obj in pkgs:
        print(obj.filename)
        # 针对zst专门处理
        if(obj.archievetype == "zstd"):
            cmd = """7z x "%s" -p%s -o%s -aoa"""%(obj.input_path,obj.passwd,obj.output_path)
            zst_e = subprocess.run(cmd,capture_output=True, text=True)
            if("Everything is Ok" in zst_e.stdout):
                tar_input_path = os.path.join(obj.output_path,obj.filename[0:-4])
                tar_output_path = obj.output_path
                print(tar_input_path)
                print(tar_output_path)
                cmd2 = """7z x "%s" -o%s -aoa"""%(tar_input_path,tar_output_path)
                tar_e = subprocess.run(cmd2,capture_output=True, text=True)
                if("Everything is Ok" in tar_e.stdout):
                    os.remove(tar_input_path)
                    donepkgs.append(obj)
                    pass
        else:
            cmd = """7z x "%s" -p%s -o"%s" -aoa %s"""%(obj.input_path,obj.passwd,obj.output_path,obj.args)
            output = subprocess.run(cmd,capture_output=True, text=True)
            if("Everything is Ok" in output.stdout):
                donepkgs.append(obj)
    print("开始转移文件")
    try:
        os.mkdir(InputFiles.output_route)
        os.mkdir(os.path.join(InputFiles.output_route,"done"))    
    except:pass
    for obj in donepkgs:
        # 处理分卷
        if(obj.archievetype == "Split"):
            for filepath in obj.pkgs:
                output = os.path.join(InputFiles.output_route,"done",obj.filename)
                os.replace(filepath,output)
        else:
            output = os.path.join(InputFiles.output_route,"done",obj.filename)
            os.replace(obj.input_path,output)
    print("""共解压 %d 个文件"""%len(pkgs))
def clear(p):
    # 权限和文件夹删除
    print("开始收尾工作")
    if(p == None):
        clear_path = InputFiles.output_route
    else:
        clear_path = p
    rubbishList = InputFiles.loadList(InputFiles.rubbishList)
    try:
        for root,dirs,files in os.walk(clear_path):
            for file in files:
                if(file in rubbishList):
                    path = (os.path.join(root,file))
                    os.chmod(path,stat.S_IRWXU)
                    os.remove(path)
            for dir in dirs:
                if(dir in rubbishList):
                    path = (os.path.join(root,dir))
                    for root2, dirs2, files2 in os.walk(path, topdown=False):
                        for name in files2:
                            os.remove(os.path.join(root2, name))
                        for name in dirs2:
                            os.rmdir(os.path.join(root2, name))
                            # 非空文件夹rmdir无效
    except:
        print("清理未成功")
class InputFiles:
    # 配置部分
    engineList = "D:/code/tools/extract/engineList"
    # 引擎特征文件
    rubbishList = "D:/code/tools/extract/rubbishList"
    # 垃圾文件
    passwdList = "D:/code/tools/extract/passwdlist"
    # 密码文件
    urlList = "D:/code/tools/extract/urlList"
    # 文件所包含的url
    ambiguityList = "D:/code/tools/extract/ambiguityList"
    # 专杀长得和游戏文件名字差不多的留痕文件
    input_route = "D:/game/download" 
    # 文件输入路径
    output_route = "D:/game/extracted"
    # 程序解压完毕后，输出本体和移走压缩包的路径
    mode = 1
    # 0：测试模式
    # 1：解压模式
    # 2: 清理模式
    # 其他: 测试模式
    def loadList(filepath):
        tempList = []
        with open(filepath,encoding="utf-8") as file:
            tempList = file.read().splitlines()
            return tempList
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

match InputFiles.mode:
    case 0:
        collect(InputFiles.input_route)
    case 1:
        pkgs = collect(InputFiles.input_route)
        extract(pkgs)
        time.sleep(30)
        clear(p = None)
    case 2:
        path = str(input("输入清理路径，输入 exit 直接退出\n"))
        if(path != "exit"):
            clear(path)
print("程序正常结束")