# if 6 > 2:
#     print("条件成立")
# else:
#     print("条件不成立")

# 目前if判断只有条件成立或者不成立执行代码块
# 多种选择如何处理？
# 要求用户输入对应节日名称，输出对应传统习俗
# day = input("请输入节日的名称：")
# if day == "端午节":
#     print("划龙舟，吃粽子")
# elif day == "七夕节":
#     print("送玫瑰花，送礼物")
# elif day == "中秋节":
#     print("吃月饼，赏月")
# elif day == "国庆节":
#     print("海南7日游")
# else:
#     print("您输入的节日不在范围之内，或者您输入的节日不正确。")

name=input("请输入你的姓氏：")
match name:
    case"李":
        print("排名第1位")
    case"周":
        print("排名第57位")
    case"柳":
        print("排名第18位")
    case"王":
        print("排名第20位")