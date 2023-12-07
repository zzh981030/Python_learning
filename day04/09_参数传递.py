"""
1. 形参和实参
2. 参数检查:isinstance(var, int)判断变量var是否为int
"""
# 2. 参数检查:
def get_max(num1:int, num2:int)->int:
    """
    求两数的最大值
    :param num1: 整型数1
    :param num2: 整型数2
    :return: 最大值
    """
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 if num1 > num2 else num2
    else:
        return  0
result = get_max(20, 30)
print(result)
print(help(get_max))