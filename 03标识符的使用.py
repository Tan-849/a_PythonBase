"""
由数字，字母，下划线组成，不能以数字开头；不能是关键字
  关键字的含义：Python 中已经被使用的名字叫做关键字
  每个关键字都有自己的作用
  显示橙色高亮
不建议使用不符合规范的命名
区分大小写
"""

# 查看关键字
import keyword
print(keyword.kwlist)

# 命名
# 小驼峰
yourName="Thw"
print(yourName)
# 大驼峰
YourName="Thw"
print(yourName)
# 下划线
your_name="Thw"
print(your_name)