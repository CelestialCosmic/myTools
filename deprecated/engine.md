复制自 https://ultrapre.github.io/clip/default/2019-10-15-1571153274/index.html#:~:text=Buriko%20Gen
电子小说相关工具
2019-09-01 11:25:09 | 笔记
电子小说（ADV / Visual Novel）领域的数据库、同好站点、开发引擎、相关转区、解包打包工具的列表。
注意，该列表并不完善，可能有错漏，仍在施工更新中。

主要程序
游戏引擎
包括业界使用较多，或知名厂牌使用的引擎。包括部分渐露头角的国内引擎，但完成度较低的自研程序不包括在内。

krkr
包括krkr2、krkrz等，也称为TVP引擎。比较老牌的引擎了（2004-），有很多插件。使用tjs/kag脚本语言。扩展名xp3。Yuzusoft都是用这个引擎。

NScripter
高橋直樹开发，2000年左右常见的系统，语法简单。特征是文件名像arc.nsa nscript.dat .env等。图像、声音没有经过特殊压缩。因为程序结构单一，被广泛移植到各种平台上。有兼容分支ONScripter。

ONScripter

SystemNNN
cyc系列

YU-RIS / ERIS
作者:たくみ。YU-RIS是AVG游戏引擎，ERIS是链接库。
代表作：Whirlpool社所有作品， CLOCKUP社所有作品。
数据文件扩展名.ypf。所有的档案都可以用ExtractData拆开

Buriko General Interpreter
即BGI引擎，作者Darios Sawm(Buriko)，又名为Ethornell。代表作:H2O(枕)， Lump of Sugar社所有作品、夜明け前より瑠璃色な(オーガスト)、キラ☆キラ(OVERDRIVE)、いつか届くあの空に(Lump of Suger)、蒼の彼方のフォーリズム(Sprite)。特征数据文件扩展名是.arc。

retouch/sketch/ExHIBIT
作者:薫。loader主程序ExHIBIT.exe。
sketch是这个引擎的核心系统，以retouch这个链接库环境来开发游戏，最后开发出来的游戏还要利用ExHIBIT来执行。系统本身不使用DirectX，画面的处理完全靠自己的核心系统。档案完全不打包，所以会有数量惊人的小文件。扩展名是.gyu(图像)+.v(声音)。图像格式.gyu用”ZZ’z Factor”的“ifgyu”对应，音声格式.v转换方法暂且不明。剧本档.rld用“notaエロゲ研究室”里面的“はるかぜどりに、とまりぎを”的拆解程序“harutoma_con.exe”可以解决。
代表作:空色の风琴(LOTUS)，エーテルの砂时计(Dreamsoft)，白银のソレイユ(SkyFish)，Clear(MOONSTONE)。

CatSystem2
Windmilll开发。另外有后续兼容版本CatSystem3

[Project NYANLIB]（http://www2s.biglobe.ne.jp/~tinyan/nyanlib/index.htm)
cyc 系ブランドで採用されている。

ISM
Production StarHole开发， 代表作ひとゆめ(STARLINK)

EntisGLS
作者Leshade Entis。实际上是一堆处理各种形式档案的链接库，开发难度较高。数据文件为.noa格式。拆开后是.eri格式的图片，.mio格式的声音。开发方自己提供了该引擎SDK及解包工具。代表作:颜のない月(Orbit)，Garden（CUFFS）、re-laive(KLEIN)，さくらむすび(CUFFS)，こんねこ(Marmalade)。

QLIE
FrontWing、Navel、ωstar、Windmill、Clochette使用。代表作：そして明日の世界より（etude）

FVP
Favorite View Point System。favorite社的引擎。 Xmoe曾宣布过其跨平台移植版xMemoria System，在后续消息中，该移植引擎可支持iOS/Android，但2014年后无动静

椎名里緒
Will社前身Forest开发。propeller、ruf、WILL社作品再用。代表作：あやかしびと（propeller)、残暑お見舞い申し上げます（めろめろキュート）

ADV32

EntisGLS
ま～まれぇど

DAI System
DAI 氏开发，詳細不明。 月面基地前のしすたぁえんじぇる、など、レイヤ演出系にこったシステムのはしりの印象。つくしてあげるのに(peassoft)

SiglusEngine
VA系列

RealLive
AVG32的演进版。有几个兼容分支，如わっふる(AVG32互換)、xkanon(AVG32互換)、xclannad（RealLive互換)。

AVG32
key社早期的引擎。注意，和ADV32不是一回事。由Visual Arts旗下的versammlen开发。

RPM ADV SYSTEM
すぺじゃに系列のブランドで使われるエンジン。

SFA
彩文館出版の系列ブランド（LiLiM/SugarPot）で使われるエンジン
主なファイルの拡張子がaos

Musica
minori开发和使用的引擎。给别的会社提供时，也可能更名。ましろ色シンフォニー（Palette）也是用Musica。

PENCIL Adventure Engine
ぱじゃまソフト系列のブランドで使われるエンジンで、名称の「PENCIL」部分が変わる事も。

AI6WIN
elfとその系列ブランドで使われるエンジン
主なファイルの拡張子がarc

WGL
Palette社

AdvHD

CMVS
Purple Software用的引擎，主程序为CMVS.exe。

GIGA

STUDIO SELDOM Adventure System

rUGP
AGE の独自システムですが、Overflow などに提供されてます。 高性能。代表作：君が望む永遠Latest Edition（アージュ）

System4.X
Alicesoft开发，使用类似C语言的高级语言。旧システム: System3.X

FFD
即Floating Frame Director，Little Witch社使用

RPM ADV SYSTEM
AXL（今はワムソフト製吉里吉里っぽい）

アトリエかぐやアプリケーション
アトリエかぐや系列

Zero-System
F&C系列

NeXAS
戯画および feat.戯画 なブランドの一部で利用されているシステム。 この青空に約束を（戯画）、ラッキー×クロス（コトノハ）

（不明）
WILL 系ブランド、およびそのパートナーブランドで使われているエンジン。 PULLTOP、HERMIT、しらたまなどが採用。実例 遙かに仰ぎ、麗しの(PULLTOP)、ままらぶ(HERMIT)

BLADE VISUAL NOVEL ENGINE
無礼堂开发。
Irrlicht Engine
AlterEgo

SystemC
インターハート（きゃんでぃそふととか）系列

C,system
TinkerBell系列

Nitroplus System 2.0
ニトロプラス系列

SystemC
インターハートの系列ブランドで使われるエンジン
主なファイルの拡張子がfpk

ADV+++
y or x project开发。

Livemaker
有限会社ヒューマンバランス开发。

TACS for Flash
鷹彰氏、 Ｃのアトリエ开发。Flash ベースの ADV 用フレームワーク

LemonNovel
LEMO开发。Flash ベースの ADV 用フレームワーク

Lucifen Library
Navel社早期作品（Shuffle等）用。现在Navel社已经开始用Ethornell和QLIE了。

Malie
light社用

NSystem
ブルームハンドル

Stuff
propeller（※Will系列）と関連ブランドで使われているエンジン
主なファイルの拡張子がmpk

Yuka System
パートナーブランド系列の一部（HOOKなど）、あるいは元パートナーブランドの一部で使われているエンジン。
主なファイルの拡張子がykc（※違うこともある）

SOFTPAL ADV System
ユニゾンシフト系列

STUDIO SELDOM Adventure System
すたじお緑茶

Lillian Adventure Engine
ティンクル☆くるせいだーす

Maid2
ApRicot系列

Willplus Engine
PULLTOP、ensemble等
拡張子：arc
実行ファイル：AdvHD.exe

Artemisエンジン
D:drive
真・恋姫†無双Android版
マルチプラットフォーム
lua使用可能

Tyrano Script
マルチプラットフォーム、ブラウザとかでも動く

Majiro
作者:越畑声太。 猫猫软件在NScripter之后用这个引擎，代表作：暁の護衛（しゃんぐりら）
ナギサの（コットンソフト）。
目前可以看到V1.000和V2.000两种版本。コットンソフト、しゃんぐりら使用。
扩展名为.arc，档案组成: system/sysgrp/sysprg.arc这三个是系统相关文件，其它的数据文件名称不定，但是通常是有序号的档名，例如data*.arc。V1版本要利用“Majiro Development kit”来拆解，V2版本要用ExtractData解包。

Unity 3D
U3D应该是通用的游戏制作工具吧。多用于3D游戏，但近年来有一些ADV也使用了U3D。
Xuseの新作がこれらしいので

Macromedia(Adobe) director
director系统的特点是容易开发跨平台(Mac系统)游戏。
扩展名.cxt(包装的数据文件)+.dxr(专案档)。
恋と選挙とチョコレート（Sprite）使用。

Macromedia(Adobe) Flash
てんしのかけら（I/O）等

O₂ Engine
HTML5 ベースのノベルゲームエンジン
ブラウザでも動く、マルチプラットフォーム
エロゲメーカーの体験版とか割と配布してる

AZSystem
casper 氏开发，CLOCKUP社用过。

Almight
HTML5で作られてる、マルチプラットフォーム、ブラウザ動作。DLsite.comと提携してる

LemoNovel

AIRNovel
《西暦２２３６》らしい

Ren’py
Python+pygame写的开源引擎，可以打包到各种平台。

BKEngine
C++写的非商用永久免费，可视化开发，可以部署到多平台。

nw.js
由node-webkit项目发展而来，是把node.js程序打包成桌面应用的第三方框架。 目前只见过两次，SORAHANE用过，bug百出。

Librian
国产引擎，基于CEFPython和wxpython。github 文档

增强技术
Live 2D

E-mote

第三方软件
请自行对工具的使用负责。此处仅介绍与电子小说运用高度相关的特有软件，通用软件（如虚拟光驱工具、汇编调试工具）不在此列。

转区、免CD等启动工具
Locale Emulator

ntleas
转区用的，是原来NTLEA的维护分支。

NTLEA全域通
已经停止开发。后被ntleas取代。

Microsoft Applocale
已经停止开发，后被NTLEA取代。有一个维护分支叫做piaip AppLocale。

piaip Applocale
即pAppLocale，原版Applocale的维护分支。

xmoeproject/FVPLoader
A simple GUI Loader which allow you to run FAVORITE’s game under none-Japanese OS
其实用别的转区工具也行，但非日语环境下 f社游戏会有显示立绘崩溃的老毛病。这个启动器进行了防崩处理。

xmoeproject/KrKrLoader
Allow you run some krkr2-based game on Windows8 OS and above.

AlphaRomDie
解决必须插着CD才能运行软件的机制。

SiglusCrack
Siglus / RealLive引擎通用一键解锁程序。一定程度上也支持其他引擎的锁区破解。

HarmoFavo
f社游戏通用和谐插件（？？？）

机器翻译工具
VNR
著名的多语种在线机翻/离线机翻/朗读/光学识别工具，用Python写的，功能全面强大，但已经停止维护了。有很多第三方修改版。代码维护在这里

喵翻AgthStart
2014年停止更新。

资源提取工具
gamepackid
引擎种类识别工具，通过相关文件特征码的检测来实现。不清楚支援度如何。

xmoeproject/KrKrExtract
Xmoe的作品，一个可以解包krkr2/krkrz的xp3资源包并重新打包的工具。 项目主页

xmoeproject/AlphaMovieDecoder

xmoeproject/SiglusExtract
A tool that can extract almost all resources used by SiglusEngine and repack some of them for translation.

westside

Susie
旧游戏Susie插件对应搜索
旧游戏对应的Susie插件搜索与下载

HCG Converter

ExtractData
提取krkr系引擎的通用工具，能很好地处理offset。

GameViewer

QuestLAB
GameViewer 的后续版本

CRASS
即CrageGUI

此分割线以下的工具我从来没有听说过，只是网上流传，请谨慎使用。

ZeaS
特别的CRASS插件

恵理ちゃんｃｌｕｂ（萌衣☆Player、noa32）
EntisGLS引擎的处理工具

asmodean

arc_conv

XP3 Viewer

Nitro+解包/封包工具

xp3dumper

m-akita

真美ツールズ

riox

Visual Novel tools

Grapholic

ffv 製圖樂園（KaguyaCut）

AnimED - VN Tools

HalTe2

halte3

BGIunpack
针对BGI新的格式解包工具，未成熟

fxckBGI
针对BGI新的游戏结构的解包工具。

BGI引擎资源解包封包工具

tachie

wolfextract

RPGDecrypter

NSDEC
Nscripter引擎的抽取工具

网站
仅收录有一定知名度的站点。过于小众、不知名的讨论站暂不列入。

数据库、维基站、标记站
-Tokuten(http://www.erogame-tokuten.com/)
查特典用的。

bangumi.tv
大陆广为人知的bangumi。另有备用域名bgm.tv

VGMDB
video game database

VNDB
visual novel database

批评空间 Erogame Scape
前丸户空间（现兰斯空间），圈子内最可靠的评分网站。

2dfan
里面关于新作的情报一应俱全。有许许多多的大佬来翻译附带人设图和CG预览的介绍，还会提供完美存档、攻略、修正补丁、汉化补丁、回避补丁等等。缺点是搜索引擎不好用，不用“标准名字”往往会搜不到，小众作品和2000年以前的作品也没有多少。

誠也の部屋
非常全面的攻略情报站，一般作品出来当天就会出路线攻略。

资源/贩售站
请注意相关法律。

忧郁的弟弟
现忧郁的loli

终点论坛

花火学园
即say花火

绯月
别名KF（该站前身为Kikyou Fans Club ：桔梗爱好俱乐部） ，前域名bbs.2dgal.com。目前常用的收生肉和CG的网站。生肉资源较全，CG资源也不少。还有画集，动画，漫画，小说音乐等资源。

nyaa
国外的资源站，原来后缀是.se，关站后域名后缀变成.si。只有生肉。R18分站

2DJGAME
门槛很高的资源站，邀请码注册。有时会有一手资源，在Nyaa上能找到其中发布的部分资源。有姐妹站mikocon。

Holyseal(http://holyseal.net)
圣封。

Comshop

DMM
俗称的大咪咪。

Toranoana
虎之穴。

Melonbooks
甜瓜。

Getchu
Getchu

Anime-Sharing
国际性的（英语语言）ACG分享论坛。国外辣鸡网盘居多，也有torrent。偶尔会比nyaa早放流。

参考资料
http://desertrain.sakura.ne.jp/kouryaku/s_engine.html
http://green.ribbon.to/~erog/Wide.html
http://ruriko.denpa.org/200612c.html#2801
http://t-yu.info/?page_id=276
http://desertrain.sakura.ne.jp/kouryaku/s_engine.html