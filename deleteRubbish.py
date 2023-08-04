import os
global rubbishFileList
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
    "",
    "America.png",
    "更多免费资源（务必收藏）XP.txt",    
    ]

def rmdir(path):
    # 删除整个文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)

def main():
    homeDir = "F:/"
    for root, dirs, files in os.walk(homeDir):
        # 先删除文件夹
        for dirctory in dirs:
            if dirctory in rubbishFileList:
                rubbishFilePath = os.path.join(root,dirctory)
                if (dirctory == "Tool") == True & os.path.exists(rubbishFilePath+"nw.exe"):
                    # 移除游戏文件夹内的mtool
                    print("即将删除 " + root + " 内的 Mtool")
                    rmdir(rubbishFilePath) # 自定义函数
                    continue
                print("即将删除 " + rubbishFilePath)
                rmdir(rubbishFilePath) # 自定义函数
        # 后删除文件
        for filename in files:
            if filename in rubbishFileList:
                rubbishFilePath = os.path.join(root, filename)
                print("即将删除 " + rubbishFilePath)
                os.remove(rubbishFilePath)
                

main()