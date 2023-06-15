def main():
    flag = '''
    选择模式：
    1:gbk 转 shitf-jis
    2:shift-jis 转 gbk
    '''
    mode = int(input (flag))
    user_input = input("输入需要转化的字符串")
    if mode == 1:
        try:
            encoded = user_input.encode('gbk')
            output = encoded.decode('shift-jis')
            print("结果为:\n", output)
        except:
            print("错误")
            pass
    elif mode == 2:
        try:
            encoded = user_input.encode('shift-jis')
            output = encoded.decode('gbk')
            print("结果为:\n", output)
        except:
            print("错误")
            pass
main()