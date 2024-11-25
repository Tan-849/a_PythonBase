import time
# time 模块中有获取时间戳的函数

print(time.time())
# 结果：1730934944.603025
# 是1970年1月1日到此刻的秒数

def get_time(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print(f"被装饰的函数执行的时间为{end - begin}")
        return end - begin
    return inner

@get_time
def func1():
    for i in range(1,1000000):
        print(i)

list1 = []
for i in range(5):
    list1.append(func1())
else:
    print(list1)
