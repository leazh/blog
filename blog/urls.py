from django.urls import path
from blog.views import article_detail, article_list, create_article, delete_article, modify_article


app_name = 'blog'

urlpatterns = [
    path(r'article_list/', article_list, name='article_list'),
    path(r'article_detail/<int:blog_id>/', article_detail, name='article_detail'),
    path(r'create_article/', create_article, name='create_article'),
    path(r'delete_article/<int:blog_id>/', delete_article, name='delete_article'),
    path(r'update_article/<int:blog_id>/', modify_article, name="update_article"),
]
