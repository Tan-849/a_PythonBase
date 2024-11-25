def fun1():
    def func2():
        print(666)
    #外面的函数返回里面的函数的名字
    #函数的名字就是函数的引用
    return func2

f=fun1() # 返回fun2函数的引用

# fun1c()=func2 --> f=func2 -> f()
f()
fun1()()