# Pycharm常用的快捷键:
#       格式化代码符合PEP8编码风格(Ctrl+Alt+L)
# 1. 连接操作符和重复操作符
name = 'westos'
print('hello ' + name)
# 1元 + 1分 = 1元 + 0.01元 = 1.01元
print('hello' + str(1))
print("*" * 30 + '学生管理系统' + '*' * 30)

# 2. 成员操作符
s = 'hello westos'
print('westos' in s)  # True
print('westos' not in s)  # False
print('x' in s)  # False

# 3. 正向索引和反向索引
s = 'WESTOS'
print(s[0])  # 'W'
print(s[3])  # 'T'
print(s[-3])  # 'T'

# 4. 切片
"""
回顾: 
    range(3):[0, 1, 2]
    range(1, 4): [1, 2, 3]
    range(1, 6, 2): [1, 3, 5]
切片: 切除一部分的内容
    s[start:end:step]
    s[:end]:
    s[start:]:
总结: 
    s[:n]: 拿出前n个元素
    s[n:]: 除了前n个元素， 其他元素保留
    s[:]:从头开始访问一直到字符串结束的位置
    s[::-1]: 倒序输出
"""
s = 'hello westos'
print(s[1:3])  # 'el'
print(s[:3])  # 'hel'
print(s[:5])  # 拿出字符串的前5个字符
print(s[1:])  # 'ello westos'
print(s[2:])  # 'llo westos'
print(s[:])  # 拷贝字符串
print(s[::-1])

# 5. for循环访问
s = 'westos'
count = 0
for item in s:
    count += 1
    print(f"第{count}个字符:{item}")
