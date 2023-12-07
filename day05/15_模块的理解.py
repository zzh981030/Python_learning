# 1. python模块实质上是一个python文件。
# 2. 注意: 自定义的python文件的文件名一定不要和已有的模块冲突。
# 3. 导入模块实质上是加载并执行模块的内容。
# 4. 导入模块的几种方式:
"""
import  hello
print(hello.digits)
hello.login()

from hello import login
login()


from hello import  login as l
l()
"""

from hello import  *
print(digits)
# 5. 模块的其他信息
"""
import  sys
print(sys.path)  # 模块的查询路径

import  hello
print(dir(hello)) # 查看hello模块可以使用的变量和函数....

print(hello.__doc__)  # 查看模块的说明文档
print(hello.__file__) # 显示模块的绝对路径
print(hello.__name__) # __name__当模块被导入时，显示的是模块的名称。
"""


