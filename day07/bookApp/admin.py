from django.contrib import admin
from bookApp.models import Book,Hero
# Register your models here.

class HeroInline(admin.StackedInline):
    model = Hero
    extra = 3


#列表页展示——书籍
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','pub_date']
    list_filter = ['pub_date']
    search_fields = ['name']
    list_display_links = ['id','name']
    list_per_page = 5
    inlines = [HeroInline]

#列表页展示——人物
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender']
    list_filter = ['gender']
    search_fields = ['name','content']
    list_display_links = ['name']
    list_per_page = 5

    #增加和编辑页的设置
    fieldsets = [('必填信息', {'fields': ['name','book_id']}),
                 ('选填信息', {'fields': ['gender','content']}), ]

admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)
