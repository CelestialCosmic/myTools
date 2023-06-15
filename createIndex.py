import re
import os
def main():
    directory = ""
    OverallIndexHtml = directory+"/index.html"
    path = os.listdir(directory)
    open(OverallIndexHtml,"w")
    # 清空之前的内容
    for i in path:
        if os.path.isdir(directory+"/"+i) == True:
            Situation = 0
            try:
                # 正常情况
                GameIndexHtml = directory+"/"+i+"/www/index.html"
                # 合成 index.html 的绝对路径
                GameHtmlFile = open(GameIndexHtml,encoding='UTF-8')
            except:
                # 处理 project/www/index.html 的情况
                GameIndexHtml = directory+"/"+i+"/project/www/index.html"
                try:
                    GameHtmlFile = open(GameIndexHtml,encoding='UTF-8')
                    Situation = 1
                except:
                    # 处理没有 www 的情况
                    GameIndexHtml = directory+"/"+i+"/index.html"
                    try:
                        GameHtmlFile = open(GameIndexHtml,encoding='UTF-8')
                        Situation = 2
                    except:
                        print(i+" 中没有游戏或者不是 RPGMaker-MV/MZ")
                        print("也可能程序进行了封包，没有 index.html\n")
            GameTitle = re.findall(r'<title>[\d\s\S\D]{1,}</title>',GameHtmlFile.read())
            # 读取并过滤title标签
            with open(OverallIndexHtml,"a+",encoding='gb18030') as indexFile:
            # 写文件
                for j in GameTitle:
                    if Situation == 0:
                        indexFile.write("<div><a href=\"./%s/www/index.html\">%s</a></div>\n"%(i,j[7:-8]))
                    elif Situation == 1:
                        indexFile.write("<div><a href=\"./%s/project/www/index.html\">%s</a></div>\n"%(i,j[7:-8]))
                    elif Situation == 2:
                        indexFile.write("<div><a href=\"./%s/index.html\">%s</a></div>\n"%(i,j[7:-8]))
                    else:
                        pass
                    # <div><a href="./xxx/www/index.html"><title>xxxxxxx</title></a></div>
main()