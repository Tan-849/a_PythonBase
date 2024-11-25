# 可变的数据类型
print("可变数据类型" + "-" * 20)
list1 = [1, 2, 3, 4, 5]
# 通过内建函数id()查看变量的内存地址
print(list1)
print(id(list1))
# 对数据类型进行操作后，再查看内存地址
print("对数据类型进行操作后，再查看内存地址" + "-" * 20)
list1.pop()
print(list1)
print(id(list1))
# 内存地址不变，所以list是可变数据类型


# 不可变的数据类型
print("不可变数据类型" + "-" * 20)
str1 = "我是一个字符串"
num1=666
print(str1)
print(id(str1))
print(num1)
print(id(num1))
print("对数据类型进行操作后，再查看内存地址" + "-" * 20)
str2=str1.replace("一","2")
num1+=1
print(str2)
print(id(str2))
print(num1)
print(id(num1))

dict1={"1":2}
dict2={1:2}
#dict3={[1,3]:2)
dict4={(1,3):2}
print(dict1)
print(dict2)
# print(dict3)
print(dict4)
