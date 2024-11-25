set1 = {1, 2, 3, 1, 2, 2, 3, 1, 2, 3, 12, 1, 2, 1, 2}
print(set1)

# 集合添加已存在的数据无效
set1.add(1)
print(set1)
set1.add(13)
print(set1)

# 删除数据
set1.remove(2)
print(set1)
