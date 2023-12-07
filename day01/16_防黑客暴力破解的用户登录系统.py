"""
需求:
根据输入用户名和密码，判断用户名和密码是否正确。
为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 报错提示。
数据库信息:
	name='root'	passwd='westos'
"""

try_count = 1  # 用户尝试登录的次数
while try_count <= 3:
    print(f'用户第{try_count}次登录系统')
    try_count += 1  # 用户尝试登录的次数+1
    name = input("用户名:")
    password = input("密码:")
    if name == 'root' and password == 'westos':
        print(f'用户{name}登录成功')
        exit()   # 退出程序
    else:
        print(f'用户{name}登录失败')
else:
    print("尝试的次数大于3次")