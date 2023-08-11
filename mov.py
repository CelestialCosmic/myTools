import os
fileNameList = [
"炼金术师艾玛的还债物语.7z",
"清秀公主.zip",
"田园诗般的日子.zip",
"バースト♀バスターズ.zip",
"金发萝莉电脑.zip",
"JK_LIVE_HAX.zip",
"迷宮ノ花ver1.14.zip",
"蕾米莉亚睡眠姦.zip",
"ひな子と帰ろう.zip",
"拯救小魅魔电脑.zip",
"【PC＋joi云翻RPG】退治女学生的鬼魂.7z",
"【PC日文RPG】エロッ娘モンスターズVer2.5.7z",
"【PC＋joi机翻RPG】色情女孩怪物2_Ver2.0.7z",
"【PC＋Tyranor云翻SLG】尽情享受与Jk女仆的夏天.7z",
"【PC＋KR日文ADV】Black__and__White.7z",
"【PC官中ADV】白色相簿：编缀的冬日回忆.7z",
"巧克甜恋2.zip.001",
"BlazingAngel_Mistletear.7z.002",
"Amusement_Parklust_v1.0.1.7z.002",
"巧克甜恋2.zip.002",
"巧克甜恋2.zip.003",
]
for fileName in fileNameList:
    try:
        os.replace("D:\@game/new\downloaded/"+fileName,"D:\@game/new\done/"+fileName)
    except:
        print(fileName+"出错")
        pass