# num1就是变量
# num1数据类型是整数类型
from turtle import TurtleGraphicsError

num1 = 666
num1 = 888
# 变量名重名时，变量的值可以进行覆盖
# 在使用变量的时候以最后一次变量名的赋值为准
print(num1)

# 如果需要查看一个变量的类型可以使用内建函数type()
# type 只能查看不能输出

# int:代表整数类型
num1 = 849
print(type(num1))

# 浮点数类型：float
num2 = 3.14
print(num2)
print(type(num2))

# 字符串类型：str
str1="Hello World"
print(str1)

# 布尔类型：bool
bool1=True
print(bool1)

# 列表类型：list
list1=[1,2,3,4]
print(list1)

# 元组类型：tuple
tuple1=(1,2,3,4)
print(tuple1)

# 集合类型：set
set1={1,2,3,4,4,4,4,4,}
print(set1)

# 字典类型：dict
dict1={"name":"Thw"}
print(dict1)



