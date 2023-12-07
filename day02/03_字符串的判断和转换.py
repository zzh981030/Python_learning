# 1. 类型判断
s = 'HelloWESTOS'
print(s.isalnum())  # True
print(s.isdigit())  # Flase
print(s.isupper())  # False

# 2. 类型的转换
print('hello'.upper())
print('HellO'.lower())
print('HellO WOrld'.title())
print('HellO WOrld'.capitalize())
print('HellO WOrld'.swapcase())

# 需求: 用户输入Y或者y都继续继续代码
# yum install httpd
choice = input('是否继续安装程序(y|Y):')
if choice.lower() == 'y':
    print("正在安装程序......")


