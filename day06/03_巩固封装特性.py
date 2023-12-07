"""
创建一个类People,
拥有的属性为姓名， 性别和年龄，
拥有的方法为购物,玩游戏,学习;

实例化 对象,执行相应的方法。

显示如下:
小明,18岁,男,去西安赛格购物广场购物
小王,22岁,男,去西安赛格购物广场购物
小红,10岁,女,在西部开源学习

提示:
属性:name,age,gender
方法:shopping(), playGame(), learning()

"""


class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def shopping(self):
        print(f'{self.name},{self.age}岁,{self.gender},去西安赛格购物广场购物 ')

    def learning(self):
        print(f'{self.name},{self.age}岁,{self.gender},在西部开源学习')


p1 = People('小明', 18, '男')
p2 = People('小王', 22, '男')
p3 = People('小红', 10, '女')

p1.shopping()
p2.shopping()
p3.learning()
print(p1.name)
