def func_out(num1):
    def func_inner(num2):
        result = num1+num2
        print(f"外部函数的值{num1}，内部函数的值{num2}，相加的结果为{result}")

    return func_inner

# 闭包函数的执行流程
f= func_out(100) # 1->2(会将func_inner加载在内存) -> 5 -> 9
f(200) # 2 -> 3 -> 4 -> 10