"""
相关的源码:from datetime import  datetime
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法， python解释器会自动将对象/实例传入方法。
    def get_age(self):
        print('self:', self)
        return self.age

    # 类方法:python解释器会自动将类传入方法。
    @classmethod
    def get_cls(cls):
        print('cls:', cls)

    # 静态方法:python解释器不会自动传入任何参数
    @staticmethod
    def get_info():
        print("static method信息")


if __name__ == '__main__':
    s = Student('张三', 18)
    s.get_age()
    s.get_cls()
    s.get_info()
