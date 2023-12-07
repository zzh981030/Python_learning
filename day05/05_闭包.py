# import  time
# start_time = time.time()  # 时间戳:从1970年1.1到现在经历的秒数
# time.sleep(2)
# end_time = time.time()    # 时间戳:从1970年1.1到现在经历的秒数
# print(end_time-start_time)


# 闭包:
#   1. 函数里面嵌套函数
#   2. 外部函数的返回值是内部函数的引用
#   3. 内部函数可以使用外部函数的变量
def timeit(name):
    def wrapper():
        print('wrapper ' + name)
    print('timeit')
    return wrapper

in_fun = timeit(name='westos')  # wrapper函数， in_fun实质上就是wrapper函数
print(in_fun())

# in_fun()
