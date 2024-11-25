# 普通函数

def func():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)


func()


# 生成器：当函数中使用了yield关键字，那么该函数就是生成器
# yield关键字跟return功能一样，可以返回值，并且结束当前函数的执行
# 核心区别是下次调用该函数会从 yield 下继续执行代码

def func():
    print(1)
    print(2)
    yield "卡点1"
    print(3)
    print(4)
    yield "卡点2"
    print(5)


# 生成器的调用需要使用next内建函数运行
i = func()
print("生成器第一次被调用")
print(next(i))
print("-" * 20)
print("生成器第二次被调用")
print(next(i))
