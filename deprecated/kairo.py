global strArray
strArray = []
global resultList
resultList = []
import re
def main():
    str_slice()
    str_delete_duplicate()
    str_output()
    print(strArray)

def str_delete_duplicate():
    resultList.sort()
    [strArray.append(i) for i in resultList if not i in strArray]
        

def str_slice():
    with open("C:/Users/root/Desktop/ka.txt",encoding = "utf-8")as f:
        for line in f:
            # print(line)
            result = re.findall(r'[\s\S]{1,}[\d]{2}',line)
            for i in result:
                resultList.append(i)
        return

def str_output():
    with open("./output.txt","w+") as f:
        for each in strArray:
            f.write(str(each))
            f.write("\n")
        f.close()
    return

main()