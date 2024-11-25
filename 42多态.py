class Girl:
    def __init__(self):
        self.name = "刘亦菲"
        self.age = 18

    def show(self):
        print("演员开始拍摄仙剑奇侠传")


girl = Girl()
girl.show()


# 使用替身代替演戏
def fun1():
    print(girl.name)
    girl.show()


# func1是调用对象本身，但是内层次是通过实例对象调用方法属性实现的
fun1()
