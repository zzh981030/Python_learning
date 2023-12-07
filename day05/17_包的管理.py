# 1. 包实质上是包含__init__.py文件的目录。
# 2. 导入包实质是在做什么? 执行包里面的__init__.py的内容。
# 3. 导入包的方式:
"""
方法1：
from sdk import  ali
from sdk import  huawei
ali.create_ecs()
huawei.create_ecs()

方法2： 相对麻烦一些， 需要在包的__init__.py添加导入信息。
import  sdk
sdk.ali.create_ecs()
sdk.huawei.create_ecs()
"""


