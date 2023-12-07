class date(object):
    # 正常的方法: 将对象作为参数传给self
    def get_self(self):
        print('self:', self)

    # 类方法: 将类名作为参数传给cls
    @classmethod
    def get_cls(cls):
        print('cls:', cls)

    # 静态方法:不自动传递任何参数
    @staticmethod
    def get_static(name, age):
        print("静态方法", name, age)


d = date()
d.get_self()
d.get_cls()
d.get_static("张三", 18)
