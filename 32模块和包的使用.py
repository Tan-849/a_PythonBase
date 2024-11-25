# # 系统自带或者安装的第三方包或者模块，可以直接进行使用
# # 导包通过 from 关键字集合 import 进行导入
# # 导包的2中形式，导入的方式不一样那么使用方式也不一样
#
#
# # 第一种，从具体模块导入具体的函数或者方法
# from random import randint
# # 使用的时候直接写函数名()进行调用
# print(randint(1, 10))
# # 从模块导入所有的方法，*代表所有模块中函数属性
# from random import *
#
# # 第二种，直接导入模块
# import random
# # 使用的时候通过模块名.函数名()进行调用
# print(random.randint(1, 10))


import time as t
print(1)
# time.sleep(5) # 起别名后报错
t.sleep(5)
print(2)

