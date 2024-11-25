# 匿名函数可以没有名字，也可以有名字
# 通过lambda 关键字进行定义
func1 = lambda x, y: x + y
print(func1)  # func1就是匿名函数的引用（名字）
print(func1(666, 888))
