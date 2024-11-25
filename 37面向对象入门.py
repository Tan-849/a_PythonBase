# 定义一个英雄类
# 1,如何定义一个类
# 使用c1a5s关键字定义，类名要符合标识符命名规则，尽量使用大驼峰命名法
class Hero:
    # 特征：
    # - 名字
    # - 攻击力
    # - 生命值
    # - 护甲值
    # - ....
    # 在类中定义实例属性
    # 在init魔法方法里面进行定义
    # 魔法方法：在特定的场景下自动执行的方法
    # 方法：类中的函数就叫做方法
    # init魔法方法叫做类构造方法
    # 当对象一旦被创建会自动执行init魔法方法
    # 实例属性全部会被自动创建
    def __init__(self):
        # 在类中定义实例属性
        # 特征：
        # - 名字
        self.name = "安琪拉"
        # = 攻击力：aggressivity
        self.aggressivity = 60
        # -生命值：HP
        self.hp = 370
        # - 护甲值：Armor
        self.Armor = 80

    # 在类中行为定义成实例方法
    # 方法就是类中的函数，不过方法的第一个参数，一定是self而且代表对象本身，来进行确定谁能调用该实例方法
    def Release_skills(self): # self 也是代表对象本身
        print("通过技能释放连招")

    # 行为：
    # - 放技能：1，2，3，4
    # - 回城
    def Returning_to_the_city(self):
        print("开始回城")
        print("3")
        print("2")
        print("1")
        print("已经回城啦！")
    # - 移动、
    def move(self):
        print("开始移动")
    # - 普通攻击
    def attack(self):
        print("发起普通攻击")

# 如何创建对象
# 通过类()实例化一个对象
# h1就是Hear类创建的对象
h1 = Hero()
# 对象如何调用实例属性？
# 通过对象.实例属性名进行调用
print(h1.name)
print(h1.Armor)
# 一个类可以创建无数个对象
h2 = Hero()
h3 = Hero()
h4 = Hero()
print(h2.name)
print(h3.Armor)
print(h4.aggressivity)
print(h4.hp)


# 调用实例方法
# 通过对象.实例方法名（）
# 只要类中定义的实例方法，并且是通过该类创建的实例对象都拥有该类的所有实例方法
h1.attack()
h2.Release_skills()
h3.move()
h4.Returning_to_the_city()