num1=int(input("请输入一个数字："))
num2=float(input("请输入一个小数："))
print(num1,num2)
print(type(num1),type(num2))

num1 =float(num1)
num2=int(num2)

print(num1,num2)
print(type(num1),type(num2))
str1=eval(input("请输入python中支持的数据类型："))
#eval内建函数的功能就是将获取的数据进行引号去除
print(str1)
print(type(str1))