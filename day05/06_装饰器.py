# 1. 装饰器: 用来装饰函数的工具。
# 2. 功能: 在不改变源代码的情况下， 添加额外功能(eg: 计算运行时间, 记录日志，权限判断)的工具.
# 3. 如何实现装饰器? 基于闭包的

import time

def timeit(f):  # f=add
    def wrapper(x, y):
        start = time.time()
        result = f(x, y)  # f实质上是add函数
        end = time.time()
        print("函数运行的时间为: %.4f" % (end - start))
        return result

    return wrapper


@timeit  # 1. 语法糖， add=timeit(add)
def add(x, y):
    return x + y


result = add(1, 3)
print(result)

#
# def max(x, y):
#     return x if x > y else y
#
#
# def my_sum(*args):
#     return sum(args)
