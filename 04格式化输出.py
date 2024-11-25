name="秋天"
age =18
height=19.8
print("我的年龄是age")
#使用占位符进行格式化输出
#不同类型的数据要求占位符也不一样
#整数：%d
#浮点数：%f默认情况保留六位小数：%.2f
#字符串类型：%s
print("我的年龄是%d"%age)
print("我的身高是%.2f"%height)
print("我的名字是%s"%name)
#一次输出多个变量
print("我的年龄是%d,我的身高是%.2f,我的名字是%s。"% (age,height,name))

#第二种方式
name="秋天"
age=18
height=9.8
print("我的年龄是{}，我的身高是{}，我的名字是{}。".format(age,height,name))
#优化简写方式
print(f"我的年龄是{age},我的身高是{height},我的名字是{name}。") #最常用的方式