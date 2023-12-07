"""
代码需求:
    1. 用户输入用户名和密码
    2. 判断用户名和密码是否正确(用户名=admin, 密码=westos)
    3. 如果正确: "用户admin登录成功"
    3. 如果不正确: "用户admin登录失败"
"""

name = input("用户名:")
password = input("密码:")
if name == 'admin' and password == 'westos':
    print(f'用户{name}登录成功')
else:
    print(f'用户{name}登录失败')