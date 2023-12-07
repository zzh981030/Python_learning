"""
类属性应用需求: 对于京东商城中显示电脑主机的列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，而是通过分页的功能局部显示，所以在向数据库中请求数据时就要显示的指定获取从第m条到第n条的所有数据 这个分页的功能包括：
- 根据用户请求的当前页和总数据条数计算出 m 和 n
- 根据m 和 n 去数据库中请求数据

from datetime import  datetime
"""

class Page(object):
    """
    [user1, user2, user3......user100]
    page=2, per_page=10
    第一页: start=0 end=10
    第二页: start=10 end=20
    第三页: start=20 end=30
    ....
    第page页: start=(page-1)*per_page end=page*per_page
    """
    def __init__(self, page, per_page=10):
        self.page = page
        self.per_page = per_page

    # 类属性: 将类方法变成类属性的过程。
    @property
    def start(self):
        return (self.page-1) * self.per_page

    @property
    def end(self):
        return  self.page * self.per_page

if __name__ == '__main__':
    goods = ['good'+str(i+1) for i in range(100)]
    page = Page(page=10, per_page=3)
    print(goods[page.start:page.end])
