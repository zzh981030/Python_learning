"""
新式类: 广度优先算法
经典类： 深度优先算法(py2中的部分类属于经典类)

python3所有的类都属于新式类。新式类的继承算法是广度优先。

# 分析多继承的相关代码
>pip install djangorestframework
from rest_framework import viewsets
viewsets.ModelViewSet
"""


class D(object):
    def hello(self):
        print('D')


class C(D):
    # def hello(self):
    #     print('C')
    pass


class B(D):
    pass
    # def hello(self):
    #     print('B')


class A(B, C):
    pass
    # def hello(self):
    #     print('A')


a = A()
a.hello()
