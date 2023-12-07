
class Student:
    """父类Student"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def learning(self):
        print(f'{self.name}正在学习')

    def choice_course(self):
        print('正在选课中'.center(50, '*'))

class MathStudent(Student):
    """MathStudent的父类是Student"""
    def choice_course(self):
        # 需求: 先执行父类的choice_course方法， 在个性化执行自己的方法。
        # Student.choice_course(self)  # 解决方法1: 直接执行父类的方法，但不建议
        # 解决方法2： 通过super找到父类，再执行方法(建议且生产环境代码常用的方式)
        super(MathStudent, self).choice_course()

        info = """
                    课程表
            1. 高等数学
            2. 线性代数
            3. 概率论
        """
        print(info)

# 实例化
m1 = MathStudent("粉条博士", 8)
m1.choice_course()

s1 = Student("粉条博士", 8)
s1.choice_course()
