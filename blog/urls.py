from django.urls import path
from blog.views import article_detail, article_list, create_article, delete_article, modify_article


app_name = 'blog'

urlpatterns = [
    path('article_list/', article_list, name='article_list'),
    path('article_detail/<int:blog_id>/', article_detail, name='article_detail'),
    path('create_article/', create_article, name='create_article'),
    path('delete_article/<int:blog_id>/', delete_article, name='delete_article'),
    path('modify_article/<int:blog_id>', modify_article, name="modify_article"),
]
