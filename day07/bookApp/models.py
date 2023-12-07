from django.db import models

'''
名词：
    ORM(object relationship mapping)对象关系映射

一对多关系：外键写在多的一端
book:hero = 1:n
'''


# Create your models here.

# 类对应数据库表，表明默认为bookApp_book
class Book(models.Model):
    # 属性对应数据库表的列名，默认会添加id这一列
    name = models.CharField(max_length=40, verbose_name="书籍名称")
    pub_date = models.DateField(verbose_name="出版日期")

    def __str__(self):
        return self.name

    class Meta:
        #单数时显示
        verbose_name = "图书管理"
        #复数时显示
        verbose_name_plural = verbose_name


# 类对应数据库表，表明默认为bookApp_hero
class Hero(models.Model):
    gender_choice = [
        (1, "男"),
        (2, "女")
    ]
    name = models.CharField(max_length=20, verbose_name="人物名称")
    gender = models.IntegerField(choices=gender_choice, verbose_name="性别")
    content = models.TextField(max_length=1000, verbose_name="人物描述")
    book_id = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, verbose_name="书籍id")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "人物管理"
        verbose_name_plural = verbose_name
