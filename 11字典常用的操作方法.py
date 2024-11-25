# dict1={"name":"天秋","age":18,"sex":"男"}
#
# # 通过字典的键取值
# print(dict1["age"])
# print(dict1["sex"])
# print(dict1["name"])
#
# # 获取所有的键
# print(dict1.keys())
#
# # 获取字典所有的值
# print(dict1.values())
#
# # 获取字典的所有键值对
# print(dict1.items())

# 增加数据
dict1 = {"name": "天秋", "age": 18, "sex": "男"}

# 快速创建一个字典
dict2 = dict(a=1, b=2, c=3)
print(dict2)
print(type(dict2))
dict2.update({"d": 4})
print(dict2)
dict2.update({"d": 4, "e": 5, "f": 6})
print(dict2)
# 如果增加键值对是，键存在，会覆盖键对应的原来的值
dict2.update({"d": 44, "e": 55, "f": 66})
print(dict2)

# 如果字典中存在这个键，那么使用默认值，不会进行覆盖
dict2.setdefault("a", 666)
print(dict2)
# 如果字典中不存在这个键，那么会新增键值对
dict2.setdefault("h", 888)
print(dict2)

# 修改数据
# 通过键修改值
dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 44, 'e': 55, 'f': 66, 'h': 888}
dict2["d"] = 666
print(dict2)

# 删除数据
dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 44, 'e': 55, 'f': 66, 'h': 888}
# 通过键删除键值对
dict2.pop("f")
print(dict2)

# clear清空字典
dict2.clear()
print(dict2)
