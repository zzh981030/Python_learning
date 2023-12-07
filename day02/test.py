'''需求: 用户输入Y或者y都继续继续代码'''
# choice = input("请确认是否继续安装(y|Y):")
# if choice.lower() == "y":
#     print("正在安装中.....")

'''startswith:'''
# url = 'http://www.baidu.com'
# if url.startswith('http'):
#     print(f'{url}是一个正确的网站')
# else:
#     print(f'不支持的网站格式')

'''endswith:'''
# 常用的场景: 判断文件的类型
# filename = input('请输入一个文件(必须加上后缀名)：')
# if filename.endswith('png'):
#     print(f"{filename}是一个图片文件")
# elif filename.endswith('mp3'):
#     print(f"{filename}是一个音乐文件")
# else:
#     print('不支持的文件格式')

'''需求:IP地址的合法性-将ip的每一位数字拿出， 判断每位数字是否在0-255之间。'''
# ip = "172.25.254.100"
# print(ip)
# items = ip.split('.')
# print(items)
# items1 = '-'.join(items)
# print(type(items1))

'''需求: 生成100个验证码， 每个验证码由2个数字和2个字母组成。'''
# import random
# import string
# for num in range(0,100):
#     yanzhengma = random.sample(string.digits + string.ascii_letters, 6)
#     yanzhengma = "".join(yanzhengma)
#     print(f"第{num+1}个验证码是{yanzhengma}")

"""
 设计一个程序，用来实现帮助小学生进行算术运算练习，
 它具有以下功能：
 提供基本算术运算(加减乘)的题目，每道题中的操作数是随机产生的，
 练习者根据显示的题目输入自己的答案，程序自动判断输入的答案是否正确
 并显示出相应的信息。最后显示正确率。
1+2=?
3*6=?
"""
