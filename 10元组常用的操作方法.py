t1 = (1, 123, 3, 22, 12, 3, 5, 7, 8, 5, 3, 12, 3)

print(t1[3])
print(t1[3:6])
print(t1)

# 常用的方法
# 统计次数
print(t1.count(3))
# 通过具体元素值获取索引（下标）
print(t1.index(12)) # 4
print(t1.index(5)) # 6
