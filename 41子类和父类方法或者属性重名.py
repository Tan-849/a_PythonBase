class A:
    money = 1000

class B:
    money = 2000

class C(A,B):
    money = 200
    # 通过在子类中定义一个实例方法使用父类的属性即可
    def use_money(self):
        #使用父类的money
        # 通过内建函数super().父类属性名即可使用
        print(super().money)


c1=C()
print(c1.money)
print("-"*20)
c1.use_money()