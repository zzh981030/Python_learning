"""
可变数据类型:list, dict,set
不可变数据类型: 数值型, str, tuple
"""

# 1. 全局变量: 全局生效的变量。函数外面的变量。
name = 'admin'
def login():
    print(name)
login()

# 2. 局部变量: 局部生效的变量。函数内部的变量。
age = 20
def logout():
    age = 19
    print(age)
logout()
# print(age)


# 3. 函数内部修改全局变量.
# 1). money是局部变量还是全局变量? 全局变量
# 2). 如果要在函数中修改全局的变量，不能直接修改。 需要用global关键字声明修改的变量是全局变量。
# 3). 不可变数据类型修改全局变量一定要global声明， 可变数据类型不需要。
def hello():
    global money
    money += 1
    users.append('user1')
    print(money, users)
money = 100  # 不可变数据类型
users = []  # 可变数据类型
hello()
print(money)