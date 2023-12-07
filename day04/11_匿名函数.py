"""
匿名函数指一类无须定义标识符的函数或子程序。Python用lambda语法定义匿名函数，
"""

# def get_max(num1: int, num2: int) -> int:
#     return num1 if num1 > num2 else num2
get_max = lambda num1, num2: num1 if num1 > num2 else num2
print(get_max(10, 20))

# def pow(x, y=2):
#     return x ** y
pow = lambda x, y=2: x ** y
print(pow(4))
print(pow(2, 3))
