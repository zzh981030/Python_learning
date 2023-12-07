"""
什么是单例模式?
一个类只能实例化一个对象的设计模式称为单例模式。
"""

class People(object):
    pass

p1 = People()  # object
p2 = People()  # object
print(p1, p2)  # 每个对象的内存地址不同，肯定不是单例模式