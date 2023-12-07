"""
模块的分类:
- 内置模块:time,datetime,random, string
- 第三方模块: requests, pandas, colorama, faker
- 自定义模块: 自己编写的python文件(模块)或者包

Windows配置全局pip镜像源: https://blog.csdn.net/u011627161/article/details/92766340
如何安装模块?>pip install colorama -i https://pypi.douban.com/simple
"""

"""
import  time
print(time.time())  # 计算时间戳
print(time.ctime()) # 字符串的时间, Sun Feb  7 17:09:55 2021
tuple_time = time.localtime()  # 元组类型的时间
print(tuple_time.tm_year)
"""

"""
from datetime import date, datetime, timedelta
print(date.today())  # 获取今天的日期
print(datetime.now())  # 获取当前时间2021-02-07 17:13:17.170345
print(date.today() + timedelta(days=3))  # 获取3天后的日期
print(date.today() - timedelta(days=3))  # 获取3天前的日期
print(datetime.now() + timedelta(minutes=10))  # 获取10分钟之后的时间信息
print(datetime.now() - timedelta(minutes=10))  # 获取10分钟之前的时间信息
"""


"""
import  random
print(random.random())  # 生成0-1之间的小数
print(random.randint(1, 10)) # 生成1-10之间的整数
print(random.choice(['赵妍', '张宏宇', '张仟军'])) # 随机选择一个元素
print(random.sample(['赵妍', '张宏宇', '张仟军'], 2)) # 随机选择n(n=2)个元素
print(random.choices(['赵妍', '张宏宇', '张仟军'], weights=[100, 10, 10]))  # 随机选择一个元素，可以指定权重

"""

"""
import  string
print(string.digits)  # 获取所有的数字
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
"""

# 颜色模块
from colorama import Fore
print(Fore.RED + 'Error: 主机不存在')
print(Fore.GREEN + 'Success: 主机创建成功')


# 生成测试信息的模块
from faker import  Faker
fake = Faker('zh-cn')
print(fake.name())
print(fake.address())
print(fake.email())