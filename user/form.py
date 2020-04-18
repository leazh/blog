# -*- coding: utf-8 -*
# Author Seichung


# 引入表单类
from django import forms
# 引入 django 的 User 模型
from django.contrib.auth.forms import User

class UserLoginForm(forms.Form):
    """
    登陆表单,继承 forms.form
    """
    username = forms.CharField()
    password = forms.CharField()