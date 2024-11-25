# 用装饰器完成符号的实参传递，根据符号输出两个数的最终结果
# 如果一个装饰器需要携带参数进行使用
# 那么必须要在装饰器的外面再次嵌套一层函数来完成参数的接收


def mark(flag):  # flag用来接收装饰器的实参
    def out_func(fn):  # fn用来接收被装饰函数的引用的
        def inner_func(num1, num2):  # num1，num2接收需要被装饰函数的实参
            if flag == "+":
                print(f"你输入的装饰器实参是{flag},进行加法运算")
                result = fn(num1, num2)
            elif flag == "-":
                print(f"你输入的装饰器实参是{flag},进行减法运算")
                result = fn(num1, num2)
            else:
                result = "您输入的符号不支持"
            return result

        return inner_func

    return out_func
#带有参数的装饰器代码执行流程：
#6 -> 21 -> 7 -> 19 -> 8 -> 9(12) -> 10(13)(15) -> 11(14)(16) -> 17
#装饰器语法糖的调用过程
# mark mark("+") == mark=out_func
# add = out_func(add) = inner_func
# add() = inner_func()

@mark("+")
def add(a, b):
    result = a + b
    return result


@mark("-")
def sub(a, b):
    result = a - b
    return result


print(add(1, 2))
print(sub(3, 4))
