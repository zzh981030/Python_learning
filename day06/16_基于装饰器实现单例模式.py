from functools import  wraps
def singleton(cls):
    # 通过一个字典存储类和对象信息{"Class":"object"}
    instances = {}
    @wraps(cls)
    def wrapper(*args, **kwargs):
        # 为了保证单例模式， 判断该类是否已经实例化为对象
        # 1. 如果有对象，直接返回存在的对象
        # 2. 如果没有则实例化对象， 并存储类和对象到字典中， 最后返回对象
        if instances.get(cls):
            return instances.get(cls)
        object = cls(*args, **kwargs)
        instances[cls] = object
        return  object
    return  wrapper

@singleton
class People(object):
    pass


p1 = People()
p2 = People()
print(p1, p2)
print(p1 is p2)  # 判断是否为单例模式(p1和p2内存地址是否相同)