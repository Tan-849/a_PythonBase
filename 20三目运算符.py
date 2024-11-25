#构造一个随机整数
#导包
import random
#调用模块中的函数或者方法
#随机生成范围内的所有整数：左闭右闭的区间
print(random.randint(1,3))
num1=int(input("请输入一个1-10之间的整数："))

num2= random.randint(1,3)

print(f"用户输入的数字是：{num1},电脑生成的数字是：{num2},两个值的较大是{num1 if num1>num2 else num2}")