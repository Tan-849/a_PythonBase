# # in / not in 关键字的使用
# list1 = [1, 2, 3]
# if 1 in list1:
#     print("有该数据")
# else:
#     print(print("没有该数据"))
#
# str1 = "abcdef"
#
# if "fa" not in str1:
#     print("没有")
# else:
#     print("有")
#
# # 容器类型的数据如果要判断某个具体的元素是否在该容器的数据类型中，那么可以使用in或者not in进行判断
# # 字典，集合，元组，列表，字符串
#
# # 列表的排序方法
# list2 = [1, 4, 6, 7, 3, 2, 1, 23, 5, 6, 8]
# # 将列表的元素进行升序排列 （从小到大）
# list2.sort()
# print(list2)
# # 将列表的元素进行升序排列 （从大到小）
# list2.sort(reverse=True)
# print(list2)
# # 将列表的元素进行反转
# list2.reverse()
# print(list2)
import copy

###########################

# # 场景：要求用户输入任意字符的一串密码
# # 提示用户密码是否为纯数字组成
# # 如果密码中出现数字6全部替换成数字7
# # 将密码中所有的出现的小写字母转化为大写
# # 将密码中出现的所有空格进行去除
# # 统计密码中出现的数字8有几次
# password = input("请输入你的密码：")
# print(f"密码是{password},该密码是否为纯数字：{password.isdigit()}")
# print("所有6更换为7")
# password1=password.replace("6","7")
# print(password1)
# print("小写转换成大写")
# password2=password.upper()
# print(password2)
# print("去除空格")
# password3=password.replace(" ","")
# print(password3)
# print(password3.count("8"))

# # 定义一个函数，传递一个字符串，和一个具体字符，返回这个字符串具体某个字符出现的次数
# str1="21382183821883218"
# def counts(str1,s1):
#     count=0
#     for i in str1:
#         if i==s1:
#             count+=1 # 统计8出现的次数，每次条件成立+1
#     else:
#         return count
# print(counts(str1, "2"))

###########################

# # 已知条件
# # 1. 北凡用代码表示如下
# # 北凡={
# # "语文"：70，
# # "数学"：65，
# # "英语"：66，
# #
# # "生物"：69，
# # "政治"：78，
# # "跳远"：[1.2,1.3,1.2]
# # }
# # 2. 百里的语文成绩比北凡高20，跳远成绩最后一次是1.5，其他成绩与北凡一样
# # 3. 星瑶的语文成绩比北凡高10，其他成绩与北凡一样
# # 请用最少的代码完成数据处理，使下面的代码可以同时打印3人的成绩
# 北凡={
#     "语文":70,
#     "数学":65,
#     "英语":66,
#
#     "生物":69,
#     "政治":78,
#     "跳远":[1.2,1.3,1.2]
#     }
# # 2. 百里的语文成绩比北凡高20，跳远成绩最后一次是1.5，其他成绩与北凡一样
# 百里 = copy.deepcopy(北凡)
# 百里["语文"] += 20
# 百里["跳远"][2]=1.5
# print(百里)
# # 3. 星瑶的语文成绩比北凡高10，其他成绩与北凡一样
# 星瑶 = copy.deepcopy(北凡)
# 星瑶["语文"] += 10
# print(星瑶)

# # 注册账号密码时：
# #1,要求账号为纯英文，否则无法注册，并且提示用户首字母必须是大写，如果用户输入的不是首字母大写帮用户改位大写并输出账号信息
# #2,要求密码长度为6-12位
# #3,如果密码正常，，那么提示密码的长度，以及密码的后四位输出给用户
# #4,如果密码不符合需求那就提示用户注册失败请重新输入
#
# # 用户如果注册失败，一直提示用户输入正确的范围密码，正确之后关闭程序
# while True:
#     username = input("请输入账号：")
#     if username.isalpha():
#         print("您输入的账号为纯英文")
#     else:
#         print("您输入的账号不是纯英文无法注册")
#     username1 = username.capitalize()
#     print(f"您的账号需要首字母大写，最终账号结果为：{username1}")
#     if len(username1) < 12 and len(username1) > 6:
#         print("密码长度合法")
#         print(f"密码的长度为{len(username1)},密码的后四位为{username1[-4:]}")
#         break
#     else:
#         print("密码长度不合法")
#         print("注册失败")

######################

# # 1.使用whi1e和for循环分别输出12456810
# # while
# i = 1
# while i <= 10:
#     if i == 3 or i == 7 or i == 9:
#         i += 1
#         continue
#     print(i)
#     i += 1
# # for
# for i in range(11):
#     if i == 3 or i == 7 or i == 9:
#         continue
#     print(i)

# # 函数的基本使用：
# # 1,定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行
# # 2,定义一个函数，完成前2个数完成动加法运算，然后对第3个数，进行减法；然后调用这个函数
# # 3,定义一个函数实现设置3个形参，传递过去完成计算器的加减乘除(+-*/)功能
# # ps：通过判断符号进行不同的运算得到结果返回出来并且打印
#
# # 1,定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行
# def output_name_age():
#     print("姓名是Thw，年龄是24岁")
# output_name_age()
#
# # 2,定义一个函数，完成前2个数完成动加法运算，然后对第3个数，进行减法；然后调用这个函数
# def add_sub(a,b,c):
#     return a+b-c
# num1=1
# num2=2
# num3=34
# result=add_sub(num1,num2,num3)
# print(result)
#
# # 3,定义一个函数实现设置3个形参，传递过去完成计算器的加减乘除(+-*/)功能
# def calculate(flag,a,b):
#     if flag=="+":
#         return a+b
#     elif flag=="-":
#         return a-b
#     elif flag=="*":
#         return a*b
#     elif flag=="/":
#         return a/b
#     else:
#         print("计算符号不合法")
#
# result=calculate("6",num2,num3)
# print(result)

####################

# # 2. 创建一个函数，可以接收3~10个参数
# # 创建一个函数，可以接收3~无数个参数
# # 创建一个函数，可以接收无数个参数
# # 创建一个函数，不可以接收参数
# # 以上的函数，不需要写逻辑，只要定义符合规范的形参即可，返回值必须是None,代码数量必须是最少
#
# # 2. 创建一个函数，可以接收3~10个参数
# def func1(a,b,c,d=None,e=None,f=None,g=None,h=None,i=None,j=None):
#     pass
# func1(1,2,3)
# func1(1,2,3,4,5,6,7,8,9)
#
# # 创建一个函数，可以接收3~无数个参数
# def func2(a,b,c,*args):
#     pass
#
# # 创建一个函数，可以接收无数个参数
# def func3(*args,**kwargs):
#     pass
#
# # 创建一个函数，可以接收无数个参数
# def func4():
#     pass

###########################
# # 定义一个电影类：
# # 定义3实例属性(（在_init_方法里面初始化实例属性，并且要求用户自己输入属性值（使用input函数获取）)：
# # 电影名称：name
# # 电影导演：director
# # 电影时长：time
# # 定义3个实例方法
# # 分别打印电影名称，电影导演，电影时长
# # 用户手动输入属性
# # 创建对象
# # 调用方法
# class movie:
#     def __init__(self,name,director,duration):
#         self.name=name
#         self.director=director
#         self.duration=duration
#
#     def movie_name(self):
#         print(self.name)
#
#     def movie_director(self):
#         print(self.director)
#
#     def movie_duration(self):
#         print(self.duration)
#
# name=input("请输入电影名字：")
# director=input("请输入导演名字：")
# duration=input("请输入电影时长：")
#
# print(f"电影名字：{name}")
# print(f"导演名字：{director}")
# print(f"电影时长：{duration}")
#
# # #2.定义程序类(coder)
# # 定义工作(work)、睡觉(sleep)、幻想(imagine)方法
# # --------------------------------------------------------------
# # 存款(money)属性
# # 3.定义小王类(xiaowang)继承自程序员类，并覆盖程序员codeer的work方法
# # 4,小王类添加一个属性：公司(company),值为"程序员”
# # 5,小王类中添加show_company方法，显示属性company的值
# # 所有的属性和方法的定义可以使类属性类方法也可以是实例属性和实例方法
#
# class coder:
#
#     def __init__(self,money):
#         self.money=money
#
#     def work(self):
#         print("工作方法")
#
#     def sleep(self):
#         print("睡觉方法")
#
#     def imagine(self):
#         print("幻想方法")
#
# class xiaowang(coder):
#     company="程序员"
#
#     def work(self):
#         print("小王工作")
#
#     def show_company(self):
#         print(f"小王公司为：{self.company}")
#
#
# xw=xiaowang("456")
# xw.work()
# xw.sleep()
# xw.imagine()
# xw.show_company()

# 私有属性和方法
class X():
    __num =666
    def __show__num(self):
        print(self.__num,"我是私有方法，被调用啦")
    def show(self):
        print(f"我的私有类属性是{self.__num}")
        print(f"调用私有方法__show_num")
        self.__show__num()


# 私有属性不能直接使用，并且不能被继承
# 通过定义一个普通方法里面使用私有属性和方法

x1=X()
# print(x1.__num) # 私有属性无法使用
x1.show_num()

# 私有属性和私有方法的特性是不能被继承，也不能在类外面直接调用，只能在类内部使用


















