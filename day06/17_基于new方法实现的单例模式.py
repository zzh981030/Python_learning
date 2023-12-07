class People(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        """创建对象之前执行的内容"""
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return  cls._instance

    def __init__(self):
        """在new方法之后执行， 将属性和对象封装在一起"""
        print("正在执行构造方法init......")

p1 = People()
p2 = People()
print(p1, p2)
