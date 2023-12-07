# 1. map函数
result = map(lambda x: x ** 2, [1, 2, 4, 5])
print(list(result))
result = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(result))

# 2. reduce函数
from functools import reduce
# (((1+2)+3)+4)+5=reduce result
result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(result)

# 练习: 求1*2*..100的结果， 用reduce和匿名函数实现
result = reduce(lambda x,y: x*y, range(1, 11))
print(result)
# 3. filter:
# 筛选所有的偶数
result = filter(lambda x: x % 2 == 0, [1, 2, 4, 5, 8])
print(list(result))
# 筛选所有的奇数
result = filter(lambda x: x % 2 != 0, [1, 2, 4, 5, 8])
print(list(result))

# 4. sorted:
result = sorted([1, 29, 2, 3])
print(result)
result = sorted([0, 29, 2, 0], reverse=True)
print(result)
result = sorted([0, 8, 9, 0, 16], key=lambda x:0 if x==0 else 1)
print(result)


