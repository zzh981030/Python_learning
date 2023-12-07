 # 1. 字典的创建dict
# key-value对或者键值对
d = {"name":"westos", "age":18, "city":"西安"}
print(d, type(d))
d = {}
print(d, type(d))

# 2. 字典的特性
# 不支持+,*, index, slice(因为集合无序不重复的)
# 支持in和not in
d = {"name":"westos", "age":18, "city":"西安"}
print('name' in d)  # True， 判断是否为所有key值得成员
print("westos" in d) # False

# 3. 字典的常用方法
# 3-1). 查看
"""
查看所有: keys, values, items
查看局部: d[key], d.get(key), d.get(key, default-value)
"""
d = {"name":"westos", "age":18, "city":"西安"}
print(d.keys())  # 查看字典所有的key值
print(d.values())  # 查看字典所有的value值
print(d.items()) # 查看字典所有的key-value值(item元素)
print(d['name'])   # 查看key为name对应的value值
# print(d['province'])   # 查看key对应的vlaue值，如果不存在会报错。
print(d.get('province'))  # 查看key对应的vlaue值， 如果存在则返回，如果不在在则返回None.
print(d.get('province', "陕西"))  # 查看key对应的vlaue值， 如果存在则返回，如果不在在则返回默认值.

# 3-2). 增加和修改
d = {"name":"westos", "age":18}
d['city'] = "西安"   # key不存在就添加
print(d)
d['city'] = "北京"   # key存在则修改value值
print(d)

d = {"name":"westos", "age":18}
d.setdefault('city', "西安")  # key不存在就添加
print(d)
d.setdefault('city', "北京") # key存在，则do nothing
print(d)

# 3-3). 删除
d = {"name":"westos", "age":18}
d.pop('name')
print(d)
d = {"name":"westos", "age":18}
del d['name']
print(d)


# 4. 遍历字典(for)
d = {"name":"westos", "age":18, "city":"西安"}
# 默认情况下，字典只会遍历key值
for item in d:
    print(item)

# 如果遍历字典的key和value呢?(特别特别重要)
for key,value in d.items():  # [('name', 'westos'), ('age', 18), ('city', '西安')]
    print(f"key={key}, value={value}")



