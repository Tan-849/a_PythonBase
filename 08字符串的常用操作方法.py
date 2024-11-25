str1 = "abcDEFG!@#$,123后知后觉FJIA0JFIS0AJSI0D!@!@!dwjiwdajio"

# 查找字符串中具体某个元素返回索引值
# 从左往右
print(str1.find('G'))
# 从右往左
print(str1.rfind('G'))

# 查找字符串中具体某个元素返回索引值
print(str1.index("2"))
print(str1.rindex("2"))

# 2.统计字符串中的元素出现的次数
print(str1.count("J"))
print(str1.count("后"))

# 3. 替换
str1 = "abacDEFG!@#$,123a后a知后a觉aFaJaIA0 aJFIaS0 aAJaSI0aDGI@aI@!dwjiwdaajio"
str2 = str1.replace("a", "*")
print(str2)
# 注意：字符串的所有操作方法不会对原生的数据进行修改
# 只会生成新的字符串
print("-" * 20)
print(str1)

# 4.切片方法
str1 = "abacD EFG!@#$,123a后a知后a觉aFa JalA0 aJF IaS0 aAJa SI0aDG!@a!@!dwjiwdaajio"
print(str1.split(" "))
# 方法操作完之后返回一个列表，里面是切完之后的字符串内容
print(str1.split(" ", 2))
print(str1.split("4", ))

# 5.大小写
print("-" * 20 + "大小写")
print(str1)
print(str1.capitalize()) # 返回首字母大写字符串
print(str1.title())# 字符串的以空格为分隔首字母大写
print(str1.upper())
print(str1.lower())

# 6.是否以某个元素开头或者结尾
print(str1.startswith("a"))
print(str1.endswith("o"))

# 7.去除字符串中的空格
str1 = "     abacD EFG!@#$,123a后a知后a觉aFa JalA0 aJF IaS0 aAJa SI0aDG!@a!@!dwjiwdaajio"
print(str1)
print(str1.strip()) # 去除字符串左右两边的空格
print(str1.rstrip()) # 右边空格
print(str1.lstrip()) # 左边空格
print(str1.replace(" ",""))

# 8.判断字符串是不是纯数字组成
str2="jdisoajdisao"
str3="2142189321838912"
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())

# 9.字符拼接
print("-".join(str3))

