import os
import subprocess
import time
import re
def rmdir(path):
    # 删除整个文件夹
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            fileToRemove = os.path.join(root, name)
            os.chmod(fileToRemove, 436 )
            os.remove(fileToRemove)
        for name in dirs:
            fileToRemove = os.path.join(root, name)
            os.chmod(fileToRemove, 436 )
            os.rmdir(fileToRemove)
    os.rmdir(path)

unZipFolderPath = "D:\@game/new/extracted"
for folder in os.listdir(unZipFolderPath):
    f = os.path.join(unZipFolderPath,folder)

    if(os.path.isdir(f)):
        print(len(os.listdir(f)))
        print(os.listdir(f))
        if(len(os.listdir(f)) == 0):
            print(f)
            rmdir(f)
