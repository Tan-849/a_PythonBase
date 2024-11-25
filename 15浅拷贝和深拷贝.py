# from copy import copy
# # 浅拷贝
# str1="大家好，我是Thw"
# str2=copy(str1)
# print(str1)
# print(id(str1))
# print(str2)
# print(id(str2))
#
# # 对可变数据类型使用浅拷贝是无效的
# list1 = ["天秋"]
# list2_none = []
# copy_list1 = []
# copy_list1 = copy(list2_none)
#
# new_list1 = list2_none.extend([1, list1])
# copy_list2 = copy(list2_none)
# new_list2 = list2_none.extend([1, list1])
# copy_list3 = copy(list2_none)
# new_list3 = list2_none.extend([1, list1])
# copy_list4 = copy(list2_none)
# new_list4 = list2_none.extend([1, list1])
# copy_list5 = copy(list2_none)
# new_list5 = list2_none.extend([1, list1])
# print("列表数据备份完毕，查看数据内容")
# print(list1)
# # 数据备份完成之后，对原生需要备份的数据进行修改，备份之后的数据也会进行修改
# list1.append("百里")
# print(list2_none)
# print(copy_list1, id(copy_list1))
# print(copy_list2, id(copy_list2))
# print(copy_list3, id(copy_list3))
# print(copy_list4, id(copy_list4))
# print(copy_list5, id(copy_list5))


# 深拷贝
from copy import deepcopy
# 对可变数据类型使用浅拷贝是无效的
list1 = ["天秋"]
list2_none = []
copy_list1 = []
copy_list1 = deepcopy(list2_none)

new_list1 = list2_none.extend([1, list1])
copy_list2 = deepcopy(list2_none)
new_list2 = list2_none.extend([1, list1])
copy_list3 = deepcopy(list2_none)
new_list3 = list2_none.extend([1, list1])
copy_list4 = deepcopy(list2_none)
new_list4 = list2_none.extend([1, list1])
copy_list5 = deepcopy(list2_none)
new_list5 = list2_none.extend([1, list1])
print("列表数据备份完毕，查看数据内容")
print(list1)
# 数据备份完成之后，对原生需要备份的数据进行修改，备份之后的数据不会被修改
list1.append("百里")
print(list2_none)
print(copy_list1, id(copy_list1))
print(copy_list2, id(copy_list2))
print(copy_list3, id(copy_list3))
print(copy_list4, id(copy_list4))
print(copy_list5, id(copy_list5))
