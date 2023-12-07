"""
用户登录成功进入系统， 登录失败，继续登录。 并且统计登录次数。
"""
try_count = 1  # 用户尝试登录的次数
while True:
    print(f'用户第{try_count}次登录系统')
    try_count += 1  # 用户尝试登录的次数+1
    name = input("用户名:")
    password = input("密码:")
    if name == 'admin' and password == 'westos':
        print(f'用户{name}登录成功')
        exit()   # 退出程序
    else:
        print(f'用户{name}登录失败')