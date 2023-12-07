import pandas
hosts = [
    {'host':'1.1.1.1', 'hostname':'test1', 'idc':'ali'},
    {'host':'1.1.1.2', 'hostname':'test2', 'idc':'ali'},
    {'host':'1.1.1.3', 'hostname':'test3', 'idc':'huawei'},
    {'host':'1.1.1.4', 'hostname':'test4', 'idc':'ali'}
]
# 1. 转换数据类型
df = pandas.DataFrame(hosts)
print(df)

# 2. 存储到excel文件中
df.to_excel('doc/hosts.xlsx')
print('success')

"""
如何安装pandas?
> pip install pandas -i https://pypi.douban.com/simple
如何安装对excel操作的模块?
> pip install openpyxl -i https://pypi.douban.com/simple
"""



