import re
import os
class Config:
	path=os.path.join('D:\game\extracted\mvmz-html\[220428][ルさんちまん]_聖少女シェリーと寝取られの村_[RJ382644]_[Ver1.05].zip\[220428][ルさんちまん] 聖少女シェリーと寝取られの村 [RJ382644] [Ver1.05]\聖少女シェリーと寝取られの村 Ver.1.05\data')
	# 必须是文件夹

def findscene():
	results = []
	for file in os.listdir(Config.path):
		txt = open(os.path.join(Config.path,file),encoding="utf-8").read()
		re1 = "\$savec.set\([\s\S\d\D]{1,}?[)]"
		# vx-vxace，必须解密rvdata2文件
		re2 = "Saba.Collection.saveCollectionFlag\([\d]{1,}\)"
		# mv
		re3 = "\$gameSystem.addEro\([\d\s\S\D]{1,}?[)]"
		# mv
		# {"code":357,"indent":1,"parameters":["Nore_Tes","Run","実行",{"id":"回想全解放_01"}]},
		# {"code":657,"indent":1,"parameters":["ファイル名 = 回想全解放_01"]},{"code":111,"indent":1,"parameters":[0,20,0]},
		# {"code":355,"indent":2,"parameters":["this.recoAll()"]},{"code":357,"indent":2,"parameters":["Nore_Tes","Run","実行",{"id":"回想全解放_02"}]},
		# {"code":657,"indent":2,"parameters":["ファイル名 = 回想全解放_02"]},
		re4 = "this.recoAll();"
		# mv Nore_Tes
		results.extend(re.findall(re3,txt))
	print("找到"+str(len(results))+"个结果")
	results.sort()
	for result in results:
		print(result+";")



findscene()
# decrypt()