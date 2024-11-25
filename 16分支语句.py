# 场景：要求用户输入任意字符的一串密码
# 需求：
# 提示用户密码是否是纯数字组成
# 如果密码中出现数字6全部替换成数字7
# 将密码中所有的出现的小写字母转化为大写
# 将密码中出现的所有空格进行去除
# 统计密码中出现的数字8有几次
str1 = input("请输入任意字符的一串密码：")

if str1.isdigit():
    print("密码是纯数字")
    print("密码为：" + str1)
else:
    print("密码不是纯数字")
    print("密码为：" + str1)
if '6' in str1:
    print("密码中的6修改为7")
    str2=str1.replace("6","7")
    print("密码为：" + str2)
if " " in str1:
    print("去除所有空格")
    str1.replace(" ","")
    print("密码为：" + str1)
if "8" in str1:
    print("统计8出现的次数")
    print(f"8出现的次数为：{str1.count('8')}")
    print("密码为：" + str1)
else:
    print(f"8出现的次数为：0")


