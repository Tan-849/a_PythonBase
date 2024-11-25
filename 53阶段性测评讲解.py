# 单选题：1-5: ADBCC 6-10: CACBA
# 多选题：11-15: BD BCD ABD ABD ABD
from random import random, randint

# 3
# a = ('a', 'b', 10, 30, 'a', 'b', 10, 30)
# a.index('b', 2, 6)

# 16
# print("-"*20+"a")
# # a.随机生成8个的0-10（范围包含0和10）之间的数字存入列表。
# list1=[]
# for i in range(0,8):
#     list1.append(randint(0,10))
# print(list1)
# print("-"*20+"b")
# # b.设计一个函数，定义一个形参，并且调用改函数传递一个实参列表（随机生成的列表），返回这个列表中8个数字出现的次数
# def count_list_8(list1):
#     print(f"数字8出现的次数{list1.count(8)}")
# count_list_8(list1)
# print("-"*20+"c")
# #  c. 然后调用函数并传入该列表，进行测试，打印出最终结果。比如【2,3,4,2,5,6,4,1】
# #     ⅰ. 2出现的次数2次
# #     ⅱ. 1出现的次数1次
# #     ⅲ. 3出现的次数1次
# def count_list(list1):
#     temp = set(list1)
#     for i in temp:
#         print(f"数字{i}出现的次数{list1.count(i)}")
# count_list(list1)

# 17
# a.手动在当前项目根目录下创建singer.txt文件，内容如下：沉默是金，张国荣少女的祈祷，杨千嬅暗里着迷，刘德华难念的经，周华健
# 沉默是金,张国荣
# 少女的祈祷,杨千嬅
# 暗里着迷,刘德华
# 难念的经,周华健
# b.定义一个singer类（歌手类），包含初始化init方法：
# class singer:
#     # ⅰ.实例属性：歌曲名 歌手名字
#     def __init__(self, song_name, singer_name):
#         self.song_name = song_name
#         self.singer_name = singer_name
#
#     # ⅱ.实例方法：fans(): 打印XXX歌手的YY歌曲持续打榜，粉丝为喜欢的歌手打call”备注：XXX为对象的歌手名字，YYY为对象的歌曲名
#     def fans(self):
#         print(f"{self.singer_name}歌手的{self.song_name}歌曲持续打榜，粉丝为喜欢的歌手打call")
#
#     # ⅲ.附加功能：在歌手类外面完成以下功能：
#     # 1.通过程序逐行读取singer.txt文件内容，根据每行数据创建对应歌手对象并赋值，依次将歌手对象存入列表。
#     # 2.遍历列表，获取元素并调用对象的fans方法.
#
# with open("singer.txt", "r", encoding="utf-8") as f:
#     readline = f.readlines()
#     for line in readline:
#         line = line.strip("\n")
#         line = line.split(",")
#         temp_singer=singer(line[0], line[1])
#         temp_singer.fans()

# 列表推导式
# list_i = [i for i in range(5)]
# print(list_i)
# # for循环in后面可以使用容器类型的数据
# list_a = [a for a in "python"]
# print(list_a)
# # 列表推导式可以结合if进行判断
# # if b % 2 == 0 判断数字是否为偶数
# list_b = [b for b in range(10) if b % 2 == 0]
# print(list_b)

# 字典推导式
# 因为字典的key是唯一的，所以最后的value值都是1
dict_a={key:value for key in "python" for value in range(2)}
print(dict_a)

# 可以根据键来构造值
dict_b={key:key*key for key in range(6)}
print(dict_b)

# 集合推导式
set_a = {value for value in "有人云淡风轻，有人负重前行"}
print(set_a)
# 集合是无序的不重复的数据类型，就算定义的时候有重复的数据那么在使用之前也会进行默认去重
