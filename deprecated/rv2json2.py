import io
import struct
import json
import yaml
from rubymarshal.reader import loads
from rubymarshal.classes import RubyObject, UserDef

def _serialize_obj(converted_obj, orig_obj):
	if type(orig_obj) != RubyObject:
		obj_type_name = orig_obj.__class__.__name__
	else:
		obj_type_name = orig_obj.ruby_class_name

	return {"val": converted_obj, "type": obj_type_name}

class Table:
	tile_size = 2

	dim = 0
	x = 0
	y = 0
	z = 0
	unknown = 0
	data = []

	def __init__(self, table_obj):
		self.table_obj = table_obj

		fd = io.BytesIO(table_obj._private_data)
		self.dim = struct.unpack("i", fd.read(4))[0]
		self.x = struct.unpack("i", fd.read(4))[0]
		self.y = struct.unpack("i", fd.read(4))[0]
		self.z = struct.unpack("i", fd.read(4))[0]
		self.unknown = struct.unpack("i", fd.read(4))[0]
		
		table_row = []
		row_size = self.tile_size * self.x
		for _ in range(self.y * self.z):
			table_row = struct.unpack("%dH" % self.x, fd.read(self.tile_size * self.x))
			self.data.append(table_row)

	def serialize(self):
		obj = {}
		obj["dim"] = self.dim
		obj["x"] = self.x
		obj["y"] = self.y
		obj["z"] = self.z
		obj["unknown"] = self.unknown
		obj["data"] = self.data

		for k in obj:
			obj[k] = _serialize_obj(obj[k], obj[k])

		return obj

class RVDataFile:
	_data = {}

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
			self._data = self._rvdata2dict(loads(open(input_file, "rb").read()))
		except IndexError:
			return

	def from_json(self, input_file):
		pass

	def to_rvdata(self, output_file):
		pass

	def to_json(self, output_file):
		with open(output_file, "w") as f:
			for x in self._data.items():
				f.writelines(str(x))
			
		# print(self._data)
		# json_data = json.dumps(self._data, indent=4, sort_keys=True)

	def to_yaml(self, output_file):
		with open(output_file, 'w') as f:
			yaml.dump(self._data, f, default_flow_style=False)

	def _rvdata2dict(self, rvdata_obj, serialize = True):
		res = {}

		if not hasattr(rvdata_obj, "attributes") and type(rvdata_obj) not in [dict, list]:
			return rvdata_obj

		child_nodes = []
		if hasattr(rvdata_obj, "attributes"):
			child_nodes = rvdata_obj.attributes
		else:
			child_nodes = rvdata_obj

		if type(child_nodes) == list:
			res = []

		for attr in child_nodes:
			if type(child_nodes) != list:
				inner_obj = child_nodes[attr]
			else:
				inner_obj = attr

			inner_obj_type = type(inner_obj)

			if not hasattr(inner_obj, "attributes") and not inner_obj_type in [dict, list]:
				converted_obj = inner_obj
				if inner_obj_type == bytes:
					converted_obj = repr(inner_obj)

				if type(child_nodes) != list:
					res[attr] = _serialize_obj(converted_obj, inner_obj)
				else:
					res.append(_serialize_obj(converted_obj, inner_obj))
				continue

			if type(inner_obj) == UserDef and inner_obj.ruby_class_name == "Table":
				table = Table(inner_obj)
				converted_obj = table.serialize()
			else:
				converted_obj = self._rvdata2dict(inner_obj, serialize = False)

			if type(child_nodes) != list:
				res[attr] = _serialize_obj(converted_obj, inner_obj)
			else:
				res.append(_serialize_obj(converted_obj, inner_obj))

		if serialize:
			return _serialize_obj(res, rvdata_obj)
		else:
			return res


class Config:
	inputpath='D:/game/extracted/mvmz-html/yonaoshi/unpacked/www/data'
	# 可文件夹可文件
	outputpath='D:/game/extracted/mvmz-html/yonaoshi/unpacked/www/data'
	# 必须是文件夹

import os
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