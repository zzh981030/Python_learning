from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 视图：对用户的骑请求(request)进行业务逻辑操作，最终返回给用户一个相应(response)
from bookApp.models import Book


def index(request):
    # print('用户请求的路径：', request.path)
    books = Book.objects.all()
    # return HttpResponse('<h1 style="color:green">图书管理系统</h1>')
    # return HttpResponse(books)
    #渲染过程，将上下文context{'books': books}填充到book/index.html代码的过程
    return render(request, 'book/index.html', {'books': books})

def detail(request,id):
    '''书籍详情页信息'''
    book = Book.objects.filter(id=id).first()
    # pub_date = book.pub_date
    heros = book.hero_set.all()
    return render(request, 'book/detail.html',
                  {'book':book,'heros':heros})