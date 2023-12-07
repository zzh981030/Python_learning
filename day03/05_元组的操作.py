# 元组tuple(戴了紧箍咒的列表, 不能修改元素)
# 1. 元组的创建
t1 = ()    # 空元组
print(t1, type(t1))
t2 = (1,)   # 重要(易错点):元组只有一个元素时一定要加逗号
print(t2, type(t2))
t3 = (1, 1.2, True, [1, 2, 3])
print(t3, type(t3))

# 2. 特性
print((1, 2, 3) + (3,))
print((1, 2, 3) * 2)
print(1 in (1, 2, 3))
t = (1, 2, 3)
print(t[0])
print(t[-1])
print(t[:2])
print(t[1:])
print(t[::-1])

# 3. 常用方法: 元组是不可变数据类型(不能增删改)
# 查看: 通过索引和切片查看元素。 查看索引值和出现次数。
t = (1, 2, 3, 1, 1, 3)
print(t.count(1))   # 3
print(t.index(3))   # 2
