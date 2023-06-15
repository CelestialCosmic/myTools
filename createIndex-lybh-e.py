import re
import os
directory = ""
path = os.listdir(directory)
for i in path:
    with open("D:/@game/ero/mv-mz/index.html",'a+',encoding = "utf-8") as file:
        index = directory+i+"/index.html"
        try:
            with open(index,encoding = "utf-8") as html:
                file.write('<div><a href="%s">'%("./lybh-e/"+i+"/index.html"))
                texts = html.read()
                result = re.findall(r'<title>[\d\s\S\D]{1,}</title>',texts)
                for j in result:
                    file.write(str(j))
                file.write("</a></div>\n")
                html.close()
        except:pass
