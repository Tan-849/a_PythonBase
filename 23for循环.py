# 输出1-100之间所有的整数

i = 1  # 循环计数变量
print("开始进入循环代码")
while i <= 100:  # 进入循环的条件
    print(f"需要被循环执行的代码，第{i}次")
    i += 1  # 1=1+1#对计数变量进行累加
print("结束循环执行的代码")

# 使用for循环构造
# range(开始值，结束值的前一位)左闭右开的区间
for i in range(1, 10):
    print(i, end=",")
print("")

# 随机在列表中添加8个1-180之间的整数
import random

list1 = []
for i in range(8):
    num1 = random.randint(1, 100)
    list1.append(num1)
    if i==6:
        print("终止循环")
        # 符合条件终止循环：break
        break
# for循环可以结合else一起使用
# 如果循环正常结束，那么执行else里面的代码
# 如果不正常结束，那么不会执行
else:
    print(list1)
