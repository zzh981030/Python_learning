"""
必选参数:必须要传递的参数
默认参数:
可变参数:*args - 元组
关键字参数:**kwargs - 字典
"""


# 1. 必选参数:必须要传递的参数
def get_max(num1: int, num2: int) -> int:
    return num1 if num1 > num2 else num2


result = get_max(20, 30)
print(result)


# 2. 默认参数:可传可不传的参数
def pow(x, y=2):
    return x ** y


result = pow(3)  # x=3, y=2, result=9
print(result)
result = pow(2, 4)  # x=2,y=4, result=2**4=8
print(result)


# 3. 可变参数: 参数的个数会变化，可以传0，1，2，3，......n
# args是元组
# args=arguments
def my_sum(*args):
    return sum(args)

result = my_sum(4, 5, 6)  # 15
print(result)

# 4. 关键字参数:可以传递key和value
# kwargs存储在字典中
def enroll(name, age=18, **kwargs):
    print(f"""
        入学信息
    1. 姓名:{name}
    2. 年龄:{age}
    3. 其他:{kwargs}
    """)

enroll('张三', country='china', english='GRE', sports=['篮球', '羽毛球'])

from collections import  namedtuple