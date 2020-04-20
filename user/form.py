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


class UserRegisterForm(forms.ModelForm):
    # username = forms.CharField()
    password = forms.CharField()
    # 确认密码
    repassword=forms.CharField()
    class Meta:
        model=User
        fields = ('username', 'email')
    # 检查密码

    def clean_repassword(self):
        data = self.cleaned_data
        if data.get('password') == data.get('repassword'):
            return data.get('password')
        else:
            raise forms.ValidationError("两次密码输入不一致,请重新输入")