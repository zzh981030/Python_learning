# 0.常用的内置函数: max,min,sum, divmod
# 函数必须有输入和输出。
# max_num = max(1, 2, 3)
# print(max_num)

# 1.如何创建函数?定义函数，函数内容并不会执行
# 函数的输入专业叫参数， 函数的输出叫返回值。
# 重点:
#       - 形参: 形式参数，不是真实的值(定义函数时的参数)
#       - 实参：实际参数， 是真实的值(调用函数时的参数)
def get_max(num1, num2):
    result = num1 if num1 > num2 else num2
    return result
# 2. 如何调用函数?
max_num = get_max(30, 80)
print(max_num)


