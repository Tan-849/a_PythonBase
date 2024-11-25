def check(func):  # func =shopping
    def inner():
        print("开始进入登录页面")
        print("扫码登录")
        print("登录成功")
        print("将大金链子添加到购物车")
        func()  # func() = shopping()

    return inner


# 原有的功能
# 使用check装饰器装饰shopping函数
@check #解读：shopping=check(shopping)
def shopping():
    print("买一条大金链子")

# shopping() = inner()
shopping()

# 被装饰的函数赋值给了func形参
# func = shopping
# 装饰器被调用完返回结果是inner
# shopping=inner