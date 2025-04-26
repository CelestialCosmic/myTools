import subprocess
fileRoute = "D:/SteamLibrary/steamapps/common/Malware/clue.jpg"
for i in range(0,100000):
    passwd = ("{:0>5d}".format(i))
    cmd = """7z t "%s" -p%s"""%(fileRoute,passwd)
    output = subprocess.run(cmd,capture_output=True, text=True)
    if("Everything is Ok" in output.stdout):
        print(passwd)