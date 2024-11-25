# 案例场景：去购物，必须先登录再把商品添加到购物车
# 原来执行动作将商品添加到购物车，由装饰器实现登录功能

# 定义一个装饰器实现登录再购买

def check(func): # func =shopping
    def inner():
        print("开始进入登录页面")
        print("扫码登录")
        print("登录成功")
        print("将大金链子添加到购物车")
        func() # func() = shopping()

    return inner


# 原有的功能
def shopping():
    print("买一条大金链子")


# 调用装饰器，传递需要被装饰的函数作为实参
shopping = check(shopping) # 6 -> 7(inner函数不会被执行但会被加载到内存中) -> 14 ->23
# shopping = check(shopping)返回结果 inner
shopping() # shopping = inner 执行7---8-9-10-11-12
