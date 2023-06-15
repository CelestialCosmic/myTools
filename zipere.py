import zipfile
def dict(z,passfile):
	with open(passfile, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			passwd = x.split("\n")[0]
			try:
				z.extractall(pwd=str.encode(passwd))
				print("密码是:%s"%(passwd))
				exit()
			except:
				pass

def brute(z):
	length = input("输入密码位数\n")
	i_min = 1
	i_max = 1
	for a in range(int(length)):
		i_max *= 10
	i_min = i_max / 10
	for id in range(int(i_min),i_max,1): 
		passwd = str(id)
		try:
			z.extractall(pwd=str.encode(passwd))
			print("密码是:%s"%(passwd))
			exit()
			break
		except:
			pass

def main():
	passfile = "/home/celestial/code/ZIP-Password-BruteForcer/pass.txt"
	filepath = "/home/celestial/code/ZIP-Password-BruteForcer/File.zip"
	z =zipfile.ZipFile(filepath, 'r')
	print("1 为字典破解\n2 为暴力破解")
	mode = input("输入模式\n")
	if(mode == "1"):
		dict(z,passfile)
	elif(mode == "2"):
		brute(z)
main()