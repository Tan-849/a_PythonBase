class X:
    name = "我是X类属性name"

    def __init__(self):
        self.age = 18

    def a(self):
        print("我是实例方法a")

    @classmethod
    def b(cls):
        print("我是类方法b")

    def c(self):
        print("我是实例方法c1")


# Y类继承X类
class Y:
    name2 = "我是Y类的类属性name2"

    def __init__(self):
        self.age2 = 18

    def a2(self):
        print("我是实例方法a2")

    @classmethod
    def b2(cls):
        print("我是类方法b2")

    def c(self):
        print("我是实例方法c2")


# 在定义类的括号里面写上父类的名字即可实现继承
class Z(X, Y):
    pass


z1 = Z()
print(z1.name)
print(z1.name2)
z1.a()
z1.a2()

# 多个父类拥有相同的属性和方法
# 多个父类拥有相同的属性和方法，会优先使用先继承（第一个参数）的父类同名方法
# 多继承的情况下，会有优先级
# 可以通过魔法属性__mro__查看继承关系的优先级
z1.c()
print(Z.__mro__)
# (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)
# 总结：当类发生继承关系之后，通过子类创建的对象调用属性和方法时，
# 会先从自己的类中找然后再按照继承顺序找到对应方法或者属性