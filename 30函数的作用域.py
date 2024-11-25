# # 全局变量
# a=888
# def func():
#     b=66
#     # 函数里面使用局部变量
#     print(b)
#     # 函数里面使用全局变量
#     print(a)
#
# # 函数外面不能使用局部变量
# print(a)
# # print(b)

a = 888
def func():
    a = 66
    # 当函数的局部变量和全局变量重名，会优先使用局部变量
    print(a)
func()

# 局部变量和全局变量重名非得使用全局变量
# 使用关键字g1obal申明，进行使用全局变量
a = 888
def func1():
    global a
    a= 666
    # 当函数的局部变量和全局变量重名，会优先使用局部变量
    print(a)
print(f"函数调用之前全局变量a的值：{a}")
func()
print(f"函数调用之后全局变量a的值：{a}")
# 局部变量和全局变量重名非得使用全局变量
