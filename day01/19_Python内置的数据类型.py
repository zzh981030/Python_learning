"""
字符串str:单引号，双引号，三引号引起来的字符信息。
数组array：存储同种数据类型的数据结构。[1, 2, 3], [1.1, 2.2, 3.3]
列表list:打了激素的数组, 可以存储不同数据类型的数据结构. [1, 1.1, 2.1, 'hello']
元组tuple:带了紧箍咒的列表, 和列表的唯一区别是不能增删改。
集合set:不重复且无序的。 (交集和并集)
字典dict：{“name”:"westos", "age":10}
"""
# 1. 字符串str
s1 = 'hello'
s2 = "hello"
s3 = """
    *********************** 学生管理系统 ************************
"""
print(type(s1), type(s2), type(s3))

# 2. 列表List
li1 = [1, 2, 3, 4]
print(li1, type(li1))
li2 = [1, 2.4, True, 2e+5, [1, 2, 3]]
print(li2, type(li2))

# 3. 元组tuple
# 易错点: 如果元组只有一个元素，一定要加逗号。
t1 = (1, 2.4, True, 2e+5, [1, 2, 3])
print(t1, type(t1))
t2 = (1,)
print(t2, type(t2))


# 4. 集合set(无序，不重复)
set1 = {1, 2, 1, 2, 3, 1, 20}
print(set1)   # 不重复{1, 2, 20}
set2 = {1, 2, 3}
set3 = {2, 3, 4}
set4 = {}
print(type(set4))
print("交集:", set2 & set3)
print("并集:", set2 | set3)

# 5. 字典dict： {“name”:"westos", "age":10}
# key和value, 键值对， 通过key可以快速找到value值。
user = {"name":'westos', 'age':10}
print(user, type(user))
print(user['name'])
print(user['age'])
