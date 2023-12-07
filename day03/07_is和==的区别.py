"""
python语言:
    ==: 类型和值是否相等
    is: 类型和值是否相等， 内存地址是否相等

"""
print(1 == '1')   # False
li = [1, 2, 3]
li1 = li.copy()
print(li == li1)  # True

# 查看内存地址
print(id(li), id(li1))
print(li is li1)  # False