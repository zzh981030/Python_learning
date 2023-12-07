"""
1. 字典和集合
1). 集合(无序不重复)
- 创建
s = {}              # s是集合么?不是，空字典
s = set()            # 如何创建空集合?
- 集合的特性： in, not
- 集合的方法:
    增:add, update
    删:pop, remove(删除的value不存在会报错), discard(删除的value不存在不报错)
    删:pop, remove(if not exists, error), discard(if not exists, do nothing)
    查:交集(s1 & s1), 并集(s1|s2), 差集(s1-s2), issubset, issuperset, isdisjoint


2). 字典
- 创建:
d = {"name":"westos", "age":18, "city":"西安"}    # key-value对或者键值对
- 特性: in, not in(注意-判断是否为所有key的成员)
    print("name" in d)       # True
    print("westos" in d)     # False
- 常用方法
    增: d[key]=value, update, d.setdefault()，key存在do nothing， key不存在则增加
    删:pop, popitem, clear
    改:d[key]=value, d.setdefault()
        d[key]=value, key存在则修改， key不存在则增加
    查: keys(), values(), items(), d[key], d.get(key), d.get(key, default-value)
        d.get(key), 如果key不存在，则返回None.

2. 函数



3. 文件管理


"""

