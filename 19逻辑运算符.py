# and or not
# and:只有2个条件都满足最终结果为真True,其他情况结果都为False假
# print(1==1and1==2）
print(1 == 1 and 1 == 1)
print(1 == 2 and 1 == 1)

# or：2个条件只要其中任意一个为真，最终结果就位真，只有2个条件都为假最终结果才是假
print(1 == 1 or 1 == 2)
print(1 == 30 or 1 == 2)
print(1 == 3 or 1 == 1)

#not:取反，真变假，假变真
print(not 1 == 2)