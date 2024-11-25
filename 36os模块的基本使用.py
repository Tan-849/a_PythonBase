import os

# 重命名
# os.rename("tanhaowei3.txt","tanhaowei.txt")

# 删除
# os.remove("tanhaowei1.txt")
# 使用绝对路径
# os.remove(r"D:\WorkSpace\PythonTestCode\a_PythonBase\tanhaowei2.txt")

# 获取当前文件的路径信息
# print(os.getcwd())  # 绝对路径：D:\WorkSpace\PythonTestCode\a_PythonBase
# print(os.path.dirname(__file__))

# 删除文件夹
# os.rmdir("999")
# 注意：不能直接删除一个有内容的文件夹
# os.rmdir("999")

# 先将文件夹内容的所有文件删除，最后再删除文件夹
# 获取文件夹的所有文件名
# 返回结果是一个列表，列表中是文件名，以str类型存储
# print(os.listdir("888"))
#
# listdir1 = os.listdir("888")
# 由于对文件的操作有一定的局限性
# 只能操作当前项目中的文件，除非使用绝对路径
# path1=r"D:\WorkSpace\PythonTestCode\a_PythonBase\abd"
# for i in listdir1:
#     # 拼接文件的路径信息+文件的名字
#     print(path1+"\\"+i)
#     os.remove(path1+"\\"+i)
# else:
#     os.rmdir("888")

# 复制一张图片
# tanhaowei[副本].jpg
old_file_name = "tanhaowei.jpg"
old_file = open("tanhaowei.jpg", "rb")

# 通过.获取文件的前缀名字和后缀名字，然后中间加上[副本]
file_flag = old_file_name.rfind(".")
# print(file_flag)
file_flag_h = old_file_name[file_flag:]
file_flag_q = old_file_name[:file_flag]
print(file_flag_h)
print(file_flag_q)

# 组织新文件的名字
new_file_name = file_flag_q + "[副本]" + file_flag_h
print(new_file_name)

new_file = open(new_file_name, "wb")
for i in old_file.readlines():
    new_file.write(i)
else:
    old_file.close()
    new_file.close()
# 如果使用的是绝对路径，那么一定要在文件前加上路径信息
