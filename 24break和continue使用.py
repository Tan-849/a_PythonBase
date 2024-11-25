# while循环和for循环当中都可以使用break和continue

# for循环可以循环遍历所有的容器类型的数据：字符串，列表，元组，集合，字典
for i in "disio9adisioajds9ioa21931923DSADSA":
    if i == '9':
        print(f"元素值为：{i}跳出循环（continue）")
        continue
    print(i, end="-")
# print()
# for i in [1, 2, 3, 2, 1, 2, 1, 4, 5, 3, 2, 1]:
# print(i, end=""

print(" ")
print(" ")
i = 0
str1 = "disio9adisigaids9ioa21931923DSADSA"  # 34
while i < len(str1)-1:
    i += 1
    print(str1[i], end=" ")
    if str1[i]=="9":
        print(f"元素值为：{i}跳出循环（continue）")
        continue
