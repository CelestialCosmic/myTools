import os
import re
def loadFile(filepath):
        tempList = []
        try:
            with open(filepath,encoding="utf-8") as file:
                tempList = file.read().splitlines()
                return tempList
        except:
            return tempList

urlList = loadFile("E:\@home\celestial\code\python\myTools\\urlList")
with open("D:/@game/new/extracted/unity/RJ344652/read me.txt",encoding="utf-8") as f:
    a = f.read()
    for url in urlList:
        b = re.findall(url,a)
        print(b)
        c = re.findall(url,f.read())
        print(c)
