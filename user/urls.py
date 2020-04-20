from django.urls import path
from . import views

app_name = "user"

urlpatterns =[
    path(r'login/', views.user_login, name='login'),
    path(r'logout/', views.user_logout, name='logout'),
    path(r'register/', views.user_register, name='register'),
]
