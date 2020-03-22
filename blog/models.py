from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Article(models.Model):
    """
    文章信息数据表：包含作者，文章标题，正文，创建时间，更新时间
    on_delete:用于指定数据删除的方式，避免两个关联表的数据不一致
    保存大量文本使用 TextField
    default=timezone.now:指定其在创建数据时将默认写入当前的时间
    auto_now=True:指定每次数据更新时自动写入当前时间
    """
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    title = models.CharField('文章标题', max_length=100)
    content = models.TextField('文章内容', )
    create_time = models.DateTimeField('创建时间', auto_now=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class meta:
        """
        内部类 class Meta 用于给 model 定义元数据
        ordering 指定模型返回的数据的排列顺序
        '-created' 表明数据应该以倒序排列
        """
        ordering = ('created_on', )

    def __str__(self):
        return self.title
