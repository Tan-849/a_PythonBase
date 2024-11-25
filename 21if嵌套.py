#地铁站过安检
#地铁票，行李物品没有危险品
piao = 1
dangerous = 0
if piao ==1:
    print("欢迎进入地铁站")
    if dangerous !=0:
        print("请勿携带危险物品进入地铁站")
    else:
        print("顺利通过，进入车站")
else:
    print("请购买地铁票再进站")