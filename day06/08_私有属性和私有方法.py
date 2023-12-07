class Student:
    """父类Student"""
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        # 私有属性，以双下划线开头。
        # 工作机制: 类的外部(包括子类)不能访问和操作，类的内部可以访问和操作。
        self.__score = score

    def learning(self):
        print(f'{self.name}正在学习')

    def get_score(self):
        self.__modify_score()
        return  self.__score

    # 私有方法是以双下划线开头的方法,
    #工作机制: 类的外部(包括子类)不能访问和操作，类的内部可以访问和操作。
    def __modify_score(self):
        self.__score += 20

class MathStudent(Student):
    """MathStudent的父类是Student"""
    def get_score(self):
        self.__modify_score()
        return  self.__score

# 报错原因: 子类无法继承父类的私有属性和私有方法。
s1 = MathStudent('张三', 18, 100)
score = s1.get_score()
print(score)

