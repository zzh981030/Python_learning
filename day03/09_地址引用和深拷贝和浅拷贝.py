# 1. 值的引用
nums1 = [1, 2, 3]
nums2 = nums1
nums1.append(4)
print(nums2)   # 1, 2, 3, 4

# 2. 拷贝：浅拷贝和深拷贝
# 2-1). 浅拷贝
n1 = [1, 2, 3]
n2 = n1.copy()   # n1.copy和n1[:]都可以实现拷贝。
print(id(n1), id(n2))
n1.append(4)
print(n2)

# 2-2). 深拷贝
"""
可变数据类型(可增删改的): list
不可变数据类型:数值，str， tuple， namedtuple
"""
n1 = [1, 2, [1, 2]]
n2 = n1.copy()
# n1和n2的内存地址:的确拷贝了
print(id(n1), id(n2))
# n1[-1]和n2[-1]的内存地址:
print(id(n1[-1]), id(n2[-1]))
n1[-1].append(4)
print(n2)

import copy
n3 = copy.deepcopy(n1)
print(id(n1),id(n2),id(n3))