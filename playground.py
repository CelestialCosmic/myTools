import os
import subprocess
import time
import re
import winreg
# import chardet
from winreg import *
readmeText = "D:\@game/new\extracted\蕾米莉亚睡眠姦\蕾米莉亚睡眠姦\MonoBleedingEdge/readme.txt"
readmeText = "D:\@game/new\extracted\バースト♀バスターズ\バースト♀バスターズ/バスバス【起動できない方へ】.txt"
with open(readmeText) as txt:
    text = txt.read()
    print(txt)
    print(text)