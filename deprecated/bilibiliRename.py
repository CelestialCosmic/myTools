import json
import os


def Rename(route, des):
    try:
        pdir = os.listdir(route)
    except FileNotFoundError:
        print("文件夹不存在")
        return 0
    errlist = []
    for i in pdir:
        sdir = route + "/" + i
        pfiles = os.listdir(sdir)
        pfiles.remove('danmaku.xml')
        pfiles.remove('entry.json')
        pfile = pfiles[0]
        with open(route + "/" + i + "/entry.json", 'r') as raw:
            data = json.load(raw)
            sfiles = os.listdir(sdir + "/" + pfile)
            sfiles.remove('index.json')
            try:
                sfile = sfiles[0]
            except IndexError:
                errlist.append(int(i))
                print("第%sP视频文件已不存在" % i)
                continue
            try:
                os.rename(os.path.join(sdir + "/" + pfile, sfile),
                          os.path.join(des, data['page_data']['part']+".mp4"))
                print(i + "成功")
            except FileNotFoundError:
                errlist.append(int(i))
                print(i + "失败")
    print("如下分P未能成功：")
    errlist.sort()
    std = 0
    for i in errlist:
        if std == 5:
            std = 0
            print()
        print("%-4s" % str(i), end="")
        std += 1
    print("\n请手动重命名")


def main():
    print("输入视频文件夹的路径，精确到 av 号，如/home/user/114514")
    route = input()
    print("输入文件输出的路径")
    des = input()
    Rename(route, des)


main()
