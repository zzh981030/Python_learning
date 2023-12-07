# 需求: 计算函数的运行时间
import time
from functools import wraps


def timeit(args='seconds'):
    def desc(f):
        """计时器的装饰器"""

        @wraps(f)  # 保留被装饰函数的属性信息和帮助文档
        def wrapper(*args, **kwargs):
            """wrapper内部函数"""
            start = time.time()
            result = f(*args, **kwargs)
            end = time.time()
            if args == 'seconds':
                print(f"函数{f.__name__}运行时间为{end - start}秒")
            elif args == 'minutes':
                print(f"函数{f.__name__}运行时间为{(end - start) / 60}秒")
            return result

        return wrapper

    return desc


@timeit(args='minutes')  # timeit()  @desc===> login=desc(login)
def login():
    """login desc"""
    print('login....')


@timeit
def crawl():
    import requests
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png'
    content = requests.get(url).content
    with open('doc/python.png', 'wb') as f:
        f.write(content)
        print("下载图片成功")


# print(help(login))
# login()
crawl()
