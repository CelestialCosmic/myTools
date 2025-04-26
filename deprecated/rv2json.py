# -*- coding: utf-8 -*-
import os
import re
import json
import yaml
from rubymarshal.reader import loads
from rubymarshal.writer import writes
from rubymarshal.classes import RubyObject

class RVDataFile:
	_data = {}
	ruby_class_name=None
	def rvdata2json(self, input_file, output_file):
		self.from_rvdata(input_file)
		self.to_json(output_file)
	def json2rvdata(self, input_file, output_file):
		self.from_json(input_file)
		self.to_rvdata(output_file)

	def __init__(self):
		pass

	def from_rvdata(self, input_file):
		try:
			rvdata_obj = loads(open(input_file,"rb").read())
		except IndexError:
			return
		except UnicodeDecodeError:
			return
		if hasattr(rvdata_obj, "attributes"):
			self._data = rvdata_obj.attributes
		else:
			self._data = rvdata_obj
	def from_json(self, input_file):
		self._data =json.loads(open(input_file, "r").read())

	def to_rvdata(self, output_file):
		print("to_rvdata: ")
		print(type(self._data))
		for x in list(self._data.items()):
			print(type(x[0]),type(x[1]))
		rvdata_obj=RubyObject(self.ruby_class_name,self._data)
		open(output_file,'wb').write(writes(rvdata_obj))

	def to_json(self, output_file):
		with open(output_file, 'w',encoding="utf-8") as f:
			try:
				for x in list(self._data.items()):
					f.writelines(str(x))
			except AttributeError:
				return

	def to_yaml(self, output_file):
		with open(output_file, 'w') as f:
			yaml.dump(self._data, f, default_flow_style=False)


class Config:
	inputpath='D:/game/extracted/vx-vxace/[S]Vibration!/Data'
	# 可文件夹可文件
	outputpath='D:/game/extracted/vx-vxace/[S]Vibration!/decrypted'
	# 必须是文件夹

import os
import re
def decrypt():
	if(os.path.isdir(Config.inputpath)):
		filelist = os.listdir(Config.inputpath)
		for file in filelist:
			r=RVDataFile()
			r.rvdata2json(\
				os.path.join(Config.inputpath,file),\
				os.path.join(Config.outputpath,file))
	elif(os.path.isfile(Config.inputpath)):
		r=RVDataFile()
		r.rvdata2json(Config.inputpath,os.path.join(Config.outputpath,file))
	else:
		print("文件输入不符合要求")


def findscene():
	results = []
	for file in os.listdir(Config.outputpath):
		txt = open(os.path.join(Config.outputpath,file),encoding="utf-8").read()
		results.extend(re.findall(r"\$savec.set\([\s\S\d\D]{1,}?[)]",txt))
	print("找到"+str(len(results))+"个结果")
	for result in results:
		print(result+";")



# findscene()
decrypt()