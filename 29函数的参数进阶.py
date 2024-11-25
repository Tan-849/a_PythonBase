# def func1(x, y):
#     print(x, y)
#     # 使用return返回多个值的时候数据会以元组的类型进行存储
#     return x, y
#
# print(func1(6, 8))
# print(type(func1(6, 8)))


# # X,y,Z函数形参的关键字
# def func2(x, y, z):
#     print("x:的值", x)
#     print("y:的值", y)
#     print("z:的值", z)
#
# func2(z=666, x=1, y=2)
# # 形参不能重复传参
# func2(1, 2, x=5)
# # 如果位置参数和关键字参数需要结合使用的前提是
# # 不能重复传参以及关键字参数要在位置参数的后面
# func2(1, Z=6, y=2)
# func2(1, y=6, Z=2)

# def func3(a,b,c=666,d=777,e="9"):
#     print("a的值：",a)
#     print("b的值：",b)
#     print("c的值：",c)
#     print("d的值：",d)
#     print("e的值：",e)
# #使用位置参数和默认参数结合可以控制实参的传递范围
# #最少要传递2个-5个实参
# func3(1,2,)
# func3(1,2,3,4,5)


# 不定长参数和位置参数（必须使用关键字传参进行）结合一起使用
# def func5(*args, a=-1, b=-1):
#     print(args)
#     print(a)
#     print(b)
# func5(1, 2, 3, 4, 5,)
# func5(1, 2, 3, 4, 5,a=8,b=9)


#不定长关键字参数
def func6(**kwargs):
    print(kwargs)
    print(type(kwargs))
func6()
func6(name="薰衣草",a=1,b=2,c=[12,32])
