# 1.查询数据
# list1=["a","b","c","d",1,2,3,4,5]
# print(len(list1))
# # 列表也可以进行切片操作
# print(list1[3])
# print(list1[-1])
# print(list1[:])
# print(list1[2:6])
# print(list1[-1:-5:-1])
# # 如果列表的步长为-1，可以实现列表的反转
# # 切片的操作不会对原生数据产生影响，会生成一个新的数据
# print(list1[::-1])

# 2.修改数据
# list1 = ["a", "b", "c", "d", 1, 2, 3, 4, 5]
# # 通过索引（下标）进行修改
# print(list1)
# list1[2] = "cc"
# print(list1)

# # 3.删除数据
# print("-"*20+"pop")
# # 1.使用pop方法进行删除
# list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
# print(list1)
# print(list1[2])
# name=list1.pop(1)
# print(name) # 默认删除最后一个数据，也可以通过下表指定删除
# print(list1)
# print(list1[2])
#
# print("-"*20+"remove")
# # 2.使用remove方法指定删除某个元素
# list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
# print(list1)
# list1.remove("吴彦祖")
# print(list1)
#
# print("-"*20+"del")
# # 3.使用关键字del删除
# list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
# print(list1)
# del list1[0]
# print(list1)
#
# print("-"*20+"clear")
# # 4.使用clear清空列表
# list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
# print(list1)
# list1.clear()
# print(list1)

# 增加数据
print("-"*20+"增加单个元素")
# 1.增加单个元素
list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
print(list1)
list1.append("陈冠希")
print(list1)

print("-"*20+"增加多个元素")
# 2.增加多个元素，将整个列表添加成一个元素
list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
print(list1)
list1.append(["杨紫","肖战"])
print(list1)
# 2.1列表嵌套取值
print(list1[5][0])


print("-"*20+"extend拆分添加")
# 3.extend拆分添加，前提是容器类型数据
list1=["晴天","彭于晏","吴彦祖","刘亦菲","胡歌"]
print(list1)
list1.extend(["杨紫","肖战"])
print(list1)

