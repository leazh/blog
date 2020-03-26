from django import forms
from django.contrib.auth.models import User


class UserLoginForm(form.forms):
    """
    form.forms:不需要对数据库进行任何改动
    """
    username = forms.CharField()
    password = forms.CharField()