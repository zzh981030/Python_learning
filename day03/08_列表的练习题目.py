"""
编写一个云主机管理系统：
    - 添加云主机(IP, hostname,IDC)
    - 搜索云主机(顺序查找)
    - 删除云主机
    - 查看所有的云主机信息
"""
from collections import  namedtuple
menu = """
                云主机管理系统
        1). 添加云主机
        2). 搜索云主机(IP搜索)
        3). 删除云主机
        4). 云主机列表
        5). 退出系统
        
请输入你的选择: """

# 思考1. 所有的云主机信息如何存储?选择哪种数据类型存储呢?  选择列表
# 思考2: 每个云主机信息该如何存储?IP, hostname,IDC   选择命名元组
hosts = []
Host = namedtuple('Host', ('ip', 'hostname', 'idc'))
while True:
    choice = input(menu)
    if choice == '1':
        print('添加云主机'.center(50, '*'))
        ip = input("ip:")
        hostname = input("hostname:")
        idc = input('idc(eg:ali,huawei..):')
        host1 = Host(ip, hostname, idc)
        hosts.append(host1)
        print(f"添加{idc}的云主机成功.IP地址为{ip}")
    elif choice == '2':
        print('搜索云主机'.center(50, '*'))
        # 今天的作业: for循环(for...else),判断, break
    elif choice == '3':
        print('删除云主机'.center(50, '*'))
        # 今天的作业:(选做)
    elif choice == '4':
        print('云主机列表'.center(50, '*'))
        print("IP\t\t\thostname\tidc")
        count = 0
        for host in hosts:
            count += 1
            print(f'{host.ip}\t{host.hostname}\t{host.idc}')
        print('云主机总个数为', count)
    elif choice == '5':
        print("系统正在退出，欢迎下次使用......")
        exit()
    else:
        print("请输入正确的选项")

