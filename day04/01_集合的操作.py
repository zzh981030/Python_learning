# 1. 集合的创建
s = {1, 2, 3, 1, 2, 3} # {1, 2, 3}
print(s, type(s))
# 注意点1: 集合的元素必须时不可变数据类型。
# s = {1, 2, 3, [1, 2, 3]}
# print(s, type(s))
# 注意点2:空集合不能使用{}, 而要使用set()
# s = {}
# print(s, type(s))
s  = set()
print(s, type(s))

# 2. 集合的特性:
# 不支持+,*, index, slice(因为集合无序不重复的)
# 支持in和not in
print(1 in {1, 2, 3, 4})


# 3. 集合的常用操作
# 3-1). 增加
#       add: 添加单个元素
#       update: 添加多个元素
s = {1, 2, 3}
s.add(100)
print(s)
s = {1, 2, 3}
s.update({4, 5, 6})
print(s)


# 3-2). 删除
#       remove: 如果元素存在，删除，否则报错
#       discard: 如果元素存在，删除，否则do nothing
#       pop: 随机
#       删除元素，集合为空则报错
s = {1, 2, 3}
s.remove(3)
print(s)
s = {1, 2, 3}
s.discard(100)
print(s)
s = {1, 66, 2,99, 78, 3}
s.pop()
print(s)


# 3-3). 查看
#           差集: s1 - s2
#           交集: s1 & s2
#           对称差分: s1 ^ s2
#           并集: s1 | s2
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1 - s2)  # {3}
print(s1 & s2)  # {1, 2}
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1 ^ s2)  # {3, 4}, {1, 2, 3, 4} - {1, 2} = {3,4}
print(s1 | s2)  # {1, 2, 3, 4}
print(s1.issubset(s2))  # False
print(s1.isdisjoint(s2)) # False


# 4. 拓展: frozenset不可变的集合
s = frozenset({1, 2, 3})
print(s, type(s))