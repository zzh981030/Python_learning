# 生成器实现的第一种方法: 将生成式改写成生成器
nums = (i**2 for i in range(10000))
print(next(nums))
# 1/0
# 生成器实现的第2种方法:yield关键字
#   return: 函数遇到return就返回，return后面的代码并不会执行。
#   yield:遇到yield则停止执行代码， 当再次调用next方法时，会从上次停止的地方继续执行，遇到yield停止。。。。
def login():
    print('step 1')   # 'step 1'
    yield 1           # output 1
    print('step 2')
    yield  2
    print('step 3')
    yield 3
# 如果函数里面有yield关键字，函数的返回值就是一个生成器
g = login()
print(next(g))
print(next(g))
