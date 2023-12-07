import  os
import platform
# 1. 获取操作系统类型
print(os.name)
# 2. 获取主机信息，windows系统使用platform模块， 如果是Linux系统使用os模块
"""
try: 可能出现报错的代码
excpt: 如果出现异常，执行的内容
finally:是否有异常，都会执行的内容
"""
try:
    uname = os.uname()
except Exception:
    uname = platform.uname()
finally:
    print(uname)

# 3.获取系统的环境变量
envs = os.environ
# os.environ.get('PASSWORD')
print(envs)

# 4. 目录名和文件名拼接
# os.path.dirname获取某个文件对应的目录名
# __file__当前文件
# join拼接, 将目录名和文件名拼接起来。
BASE_DIR = os.path.dirname(__file__)
setting_file = os.path.join(BASE_DIR, 'dev.conf')
print(setting_file)