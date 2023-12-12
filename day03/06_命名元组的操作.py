tuple = ("westos", 18, "西安")
print(tuple[0], tuple[1], tuple[2])

# 从collections模块中导入namedtuple工具。
from collections import namedtuple

# 1. 创建命名元组对象User
User = namedtuple('zzh', ('name', 'age', 'city'))#zzh表示此命名元组的名称，不做实际用处
# 2. 给命名元组传值
user1 = User("westos", 18, "西安")
# 3. 打印命名元组
print(user1)
# 4. 获取命名元组指定的信息
print(user1.name)
print(user1.age)
print(user1.city)
print(user1[0])
