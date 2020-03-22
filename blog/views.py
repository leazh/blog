from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from blog.models import Article
import markdown
from .form import ArticleForm

# Create your views here.


def article_list(request):
    """
    文章列表页
    1.获取文章标题
    :param request:
    :return:
    """
    articles = Article.objects.all()
    return render(request, "article/article_list.html", {'articles': articles}, )


def article_detail(request, blog_id):
    """
    文章详情
    :param request:
    :param blog_id: 文章 ID
    :return:
    """
    # 取出相应的文章
    details = get_object_or_404(Article, id=blog_id)
    details.content = markdown.markdown(
        details.content,
        extensions={
            'markdown.extensions.extra',    # 包含 缩写、表格等常用扩展
            'markdown.extensions.codehilite',  # 语法高亮扩展
            'markdown.extensions.toc',
        })
    context = {
        'detail': details,
    }
    return render(request, 'article/article_details.html', context)


def create_article(request):
    """
    增加文章页面
    :return:
    """
    # 判断用户使用的是否为POST请求
    if request.method == "POST":
        # 将提交的数据赋值到表单中
        article = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的需求
        if article.is_valid():
            # 提交数据，但是不保存在数据库中
            new_article = article.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            new_article.author = User.objects.get(id=1)
            # 将编辑的文章写入数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("blog:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
        # 如果用户请求获取数据
    else:
        # 创建表单类实例
        post_article = ArticleForm()
        # 赋值上下文
        context = {
            "post_article": post_article
        }
        return render(request, "article/create_article.html", context)


def delete_article(request, blog_id):
    """
    删除文章页面
    1. 获取文章ID，然后进行删除
    2. 删除之后返回文章列表
    :param request:
    :param blog_id:
    :return:
    """
    del_article = Article.objects.get(id=blog_id)
    del_article.delete()
    return redirect("blog:article_list")

def modify_article(request, blog_id):
    """
    更新文章页面
    :param request:
    :return:
    """
    article = Article.objects.get(id=blog_id)
    if request.method == "POST":
        post_article = ArticleForm(data=request.POST)
        if post_article.is_valid():
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.save()
            return redirect("blog:article_detail", id=blog_id)
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        post_article = ArticleForm()
        context = {'article': article, 'post_article': post_article}
        return render(request, "article/update_article.html", context)
