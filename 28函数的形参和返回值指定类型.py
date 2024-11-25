def login(username: str, password: int) -> str:
    print("开始输入账号密码")
    print(f"开始验证账号：{username},密码：{password}")
    print("账号密码正确")
    print("欢迎登录成功")
    return "欢迎vip进入"


# 函数的形参和返回值指定类型
print(login("乔", 123213))
# 按照指定类型传参
print(login("Thw", 123213))
# 不按照指定类型传参
print(login(888, "123213"))