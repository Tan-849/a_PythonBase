class A:
    def a(self):
        print("a方法被调用了")

    def b(self):
        print("b方法被调用了")

    def c(self):
        print("c方法被调用了")

    def d(self):
        print("d方法被调用了")


x = A()
y = A()
# # 对对象添加一个实例方法
# setattr(x,"e",print)
# x.e("e方法被调用了") # x.e("")=print()
# setattr(x,"f",input)
# num=x.f("请输入你的密码：") # x.f()=input("")
# print(num)
# # 反射添加的方法只针对被添加的对象，对其他对象并不会造成影响
# y.e("e方法被调用了") # x.e("")=print()

# # 对对象覆盖一个实例方法
# x.b()
# setattr(x,"b",print)
# x.b("这是通过反射覆盖之后的b方法")

# 删除
# x.a()
# print("通过反射删除之后")
# delattr(x,"a")
# x.a() # 报错

# # 通过反射判断对象是否有指定方法
# print(hasattr(x, "a"))  # True
# print(hasattr(x, "2"))  # False

# 通过反射读取方法
f = getattr(x, "a")  # 通过反射将x对象的a方法赋值给f
f()  # f() = a()

# 调用x对象的所有方法
for i in["a","b","c","d"]:
    f = getattr(x, i)
    f()
