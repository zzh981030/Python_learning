# 类(Class)
class Cat:
    def __init__(self, name, kind):  # 形参
        """
        1. 构造方法，实例化对象时自动执行的方法
        2. self是什么? self实质上是实例化的对象
        3. 类方法中, python解释器会自动把对象作为参数传给self
        """
        print('正在执行__init__构造方法')
        print('self:', self)
        # 属性：一般是名词，eg: name, age, gender.....
        # 封装: self.name将对象和name属性封装/绑定
        self.name = name
        self.kind = kind

    # 方法: 一般情况是动词, eg: create, delete, eating, run......
    def eat(self):
        print('cat %s like eating fish.....' % (self.name))


# 对象(Object):对类的实例化(具体化)
fentiao = Cat("粉条", "美短虎斑")
print(fentiao.name)
print(fentiao.kind)
fentiao.eat()
