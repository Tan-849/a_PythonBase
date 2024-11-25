# # print(a)
#
# try:
#     print(1)
#     print(1)
#     print(1)
#     # print(a)
#     print(1)
#     print(1)
#     print(1)
# except:
#     print("try中出现异常啦！！！！！")
#     print("当try中捕获到异常之后会执行except.里面的代码1")
#     print("如果try的代码块没有出现异常，那么不会执行except里面的代码1")
# else:
#     print("如果try当中没有出现异常会执行的代码块2")
#     print("如果try当中没有出现异常会执行的代码块2")
#     print("如果try当中没有出现异常会执行的代码块2")
# finally:
#     print("不管try当中是否有异常，都会执行的代码块3")
#     print("不管try当中是否有异常，都会执行的代码块3")
#     print("不管try当中是否有异常，都会执行的代码块3")

# 异常与异常之间会相互传递
def func1():
    print(a)

def func2():
    print(2)
    func1()

def func3():
    print(3)
    func2()

func3()