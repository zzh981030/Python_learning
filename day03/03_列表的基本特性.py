# 1. 连接操作符和重复操作符
print([1, 2] + [2, 3]) # [1, 2, 2, 3]
print([1, 2] * 3) # [1, 2, 1, 2, 1, 2]

# 2. 成员操作符(in, not in)
print(1 in [1, 2, 3]) # True
"""
布尔类型:
    True: 1
    False:0
"""
print(1 in ["a", False, [1, 2]])  # False

# 3. 索引
li = [1, 2, 3, [1, 'b', 3]]
print(li[0])  # 1
print(li[-1]) # [1, 'b', 3]
print(li[-1][0])  # 1
print(li[3][-1])  # 3

# 4. 切片
li = ['172', '25', '254', '100']
print(li[:2])
print(li[1:])
print(li[::-1])
# 需求: 已知['172', '25', '254', '100']， 输出: "100-254-25"
li = ['172', '25', '254', '100']
print("-".join(li[1:][::-1]))

# 5. for循环
names = ["粉丝", '粉条', '粉带']
for name in names:
    print(f"西部开源猫大佬的姓名是:{name}")



