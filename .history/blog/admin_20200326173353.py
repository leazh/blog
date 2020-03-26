from django.contrib import admin
from blog.models import Article

# Register your models here.


class ArticleDisplay(admin.ModelAdmin):
    """
    后台页面显示字段
    """
    list_display = ('id', 'author', 'title', 'create_time', 'update_time')


admin.site.register(Article, ArticleDisplay)
