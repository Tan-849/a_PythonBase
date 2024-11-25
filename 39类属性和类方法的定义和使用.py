# 类属性和类方法的定义和使用
class Hero:
    # 类属性就是在类中定义的变量
    mana = 999

    def __init__(self, name, aggressivity, hp, Armor):
        self.name = name
        self.aggressivity = aggressivity
        self.hp = hp
        self.Armor = Armor

    def Release_skills(self, num1):  # self 也是代表对象本身
        print(f"你的英雄：{self.name}释放了{num1}技能")

    def Returning_to_the_city(self):
        print("开始回城")
        print("3")
        print("2")
        print("1")
        print("已经回城啦！")

    def move(self):
        print("开始移动")

    def attack(self):
        print("发起普通攻击")

    # 通过装饰器定义类方法
    @classmethod
    def singalling(cls): #cls 代表的时类名
        print("发送一条警告信号")

    # 通过装饰器定义类方法
    @staticmethod
    def plear(): # 静态方法没有self也没有cls
        print("我是一个静态方法已经被调用了！！")

# 通过创建对象时进行自定义属性传递实参
h1 = Hero("李白", 100, 200, 300)
h2 = Hero("韩信", 666, 888, 999)
# 类属性可以通过对象.类属性名
print(h1.mana)
print(h2.mana)
# 类也可以进行使用类属性
print(Hero.mana)
# 结论：类属性 对象可以使用，类也可以使用

# 类可不可以使用实例属性和实例方法？3
# 不可以使用！
# print(Hero.name)
# Hero.attack()

# 总结：对象可以使用类属性和类方法以及实例属性和实例方法
# 类只能用类属性和类方法，不能使用实例属性和实例方法

# 类方法的使用可以通过 类.类方法名()
Hero.singalling()
h1.singalling()
h2.singalling()


# 静态方法的调用
# 类和对象都可以调用静态方法
h2.plear()
Hero.plear()