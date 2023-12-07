"""
装饰器的万能模板:
def 装饰器名称(f):
    @wraps(f)  # 保留被装饰函数的属性信息和帮助文档
    def wrapper(*args, **kwargs):
        # 执行函数之前做的事情
        result = f(*args, **kwargs)
        # 执行函数之后做的事情
        return  result
    return  wrapper
"""

# 需求: 计算函数的运行时间
import time
from functools import wraps


def timeit(f):
    """计时器的装饰器"""

    @wraps(f)  # 保留被装饰函数的属性信息和帮助文档
    def wrapper(*args, **kwargs):
        """wrapper内部函数"""
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"函数{f.__name__}运行时间为{end - start}秒")
        return result

    return wrapper


@timeit
def login():
    """login desc"""
    print('login....')

@timeit
def crawl():
    import requests
    url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic1.zhimg.com%2Fv2-8f51c35f5e8e48d3c8616a4353178689_1440w.jpg%3Fsource%3D172ae18b&refer=http%3A%2F%2Fpic1.zhimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1652966157&t=2aab95a477f8d65b890487ec22b91505'
    content = requests.get(url).content
    with open('doc/python.png', 'wb') as f:
        f.write(content)
        print("下载图片成功")


# print(help(login))
# login()
crawl()
