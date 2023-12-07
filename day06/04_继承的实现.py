
class Student:
    """父类Student"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def learning(self):
        print(f'{self.name}正在学习')

class MathStudent(Student):
    """MathStudent的父类是Student"""
    pass

# 实例化
m1 = MathStudent("粉条博士", 8)
print(m1.name)
print(m1.age)
m1.learning()           # 不报错，子类里没有，但父类有该方法
# m1.choice_course()   # 报错, 子类里没有，父类也没有的方法
