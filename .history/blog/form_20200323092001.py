# -*- coding: utf-8 -*
# Author Meszhang

from django import forms
from blog.models import Article


class ArticleForm(forms.ModelForm):
    """
    编写文章表单类
    """
    # 格式需要是Meta，否则会报错
    class Meta:
        # 数据模型来源
        model = Article
        # 表单涉及的字段
        fields = ('title', 'content')
