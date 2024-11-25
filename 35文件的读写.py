# # 通过内建函数 open() 打开文件传递实参进行文件读写
# # open(第一个参数：具体需要打开的文件名，第二个参数：读写模式（r/w）不指定默认为r，第三个参数：编码格式（通过关键字传参）)
#
# file = open("tanhaowei.txt","r",encoding="utf-8")
# # 通过被打开的文件对象读取内容
# # result = file.read() # 一次性读取文件所有内容 返回结果是str类型
# # result = file.readlines() # 一行一行读取 返回内容是list类型
# result = file.readline() # 读取一行数据
#
# print(result)
# print(type(result))
#
# list1 = []
# for i in result:
#     list1.append(i.strip()) # strip() 去除空格和换行符
# else:
#     print(list1)
#
# # 关闭文件
# file.close()


# 文件写入
# 可以通过上下文管理器关键字wth,进行读写，不需要进行手动关闭文件，使用完会自动关闭
# 如果打开一个文件的写入模式，该文件存在那么会覆盖内容，如果不存在会新建一个文件
# 如果以读的方式打开一个文件，文件不存在会直接报错
# with open("tanhaowei2.txt","w",encoding="utf-8") as file2:
#     file2.write("1\n664645645645646546\n888\n我是需要被写入的内容")
#
# with open("tanhaowei2.txt","a",encoding="utf-8") as file2:
#     file2.write("1\n664645645645646546\n888\n我是需要被写入的内容")
#
#
# with open("3123123.txt","r",encoding="utf-8") as file3:
#     file3.read()

# 二进制读写
#如果使用绝对路径，信息里面有\这种转义字符，那么路径前面加上保证是原生字符串路径信息即可
with open(r"D:\WorkSpace\PythonTestCode\a_PythonBase\tanhaowei.jpg","rb")as f:
    print(f.read())

# 报错
with open(r"D:\WorkSpace\PythonTestCode\a_PythonBase\tanhaowei.jpg","rb",encoding='utf-8')as f:
    print(f.read())