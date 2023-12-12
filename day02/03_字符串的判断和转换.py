# 1. 类型判断
s = 'HelloWESTOS'
print(s.isalnum())  # True,是否是字符或数字
print(s.isdigit())  # Flase
print(s.isupper())  # False

# 2. 类型的转换
print('hello'.upper())#全部转换成大写
print('HellO'.lower())#全部转换成小写
print('HellO WOrld'.title())#字符串每个单词的首字母大写
print('HellO WOrld'.capitalize())#字符串首字母大写，其他都小写
print('HellO WOrld'.swapcase())#切换大小写

# 需求: 用户输入Y或者y都继续继续代码
# yum install httpd
choice = input('是否继续安装程序(y|Y):')
if choice.lower() == 'y':
    print("正在安装程序......")


