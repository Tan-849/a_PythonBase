# 自定义属性和方法
class Hero:
    # 魔法方法以及实例方法都可以使用任意的参数（位置参数，关键字参数，不定长参数，默认参数...）
    def __init__(self,name,aggressivity,hp,Armor):
        self.name = name
        self.aggressivity = aggressivity
        self.hp = hp
        self.Armor = Armor

    def Release_skills(self,num1): # self 也是代表对象本身
        # print("通过技能释放连招")
        # 实例方法中使用实例属性：通过se1f,属性名
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

# 通过创建对象时进行自定义属性传递实参
h1= Hero("李白",100,200,300)
h2= Hero("韩信",666,888,999)
print(h1.name, h1.aggressivity, h1.hp, h1.Armor)
print(h2.name, h2.aggressivity, h2.hp, h2.Armor)

# 通过对象调用实例方法，传递实参进行使用
h1.Release_skills(1)
h2.Release_skills(2)


str1="21321312"
# str是一个字符串对象，对象可以调用replace方法（需要被替换的字符，替换成功的字符），
str.replace("k","")