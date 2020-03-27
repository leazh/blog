from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'article_list/', views.article_list, name='article_list'),
    path(r'article_detail/<int:blog_id>/', views.article_detail, name='article_detail'),
    path(r'create_article/', views.create_article, name='create_article'),
    path(r'delete_article/<int:blog_id>/', views.delete_article, name='delete_article'),
    path(r'update_article/<int:blog_id>/', views.modify_article, name="update_article"),
]
