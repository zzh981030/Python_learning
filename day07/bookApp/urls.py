from django.urls import path

from bookApp import views

urlpatterns = [
    #当用户访问路径是book/,执行views.index视图函数
    path(r'', views.index,name='index'),
    #显示书籍的详情页，接受一个int值并赋值给id
    path(r'<int:id>', views.detail,name='detail'),
]