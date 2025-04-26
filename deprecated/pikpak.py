import subprocess

def main():
    pkclipath = "D:\software\pikpak/pikpakcli.exe"
    pkfolder = "3"
    pkfile = "異種姦レミフラSRPG ～レミリアとフランが色んなコスプレで魔物を逆レイプするシミュレーションRPG～"
    pkfile_type = 1
    # 1 == 文件夹，2 == 单文件
    output = "D:\game\pikpak"
    args = "-g"
    match pkfile_type:
        case 1:
            cmd = pkclipath + " download" + " " + "-p " + "\"" + pkfolder + "\\" + pkfile + "\"" + " -o " + output + " " +args
        case 2:
            cmd = pkclipath + " download" + " " + "-p " + "\"" + pkfolder + "\" "+ "\"" + pkfile + "\"" + " -o " + output + " " +args
    print(cmd)

main()