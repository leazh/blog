from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# 引入创建好的 form 表单
from .form import UserLoginForm
# Create your views here.


def user_login(request):
    """
    用户登录
    """

    # 判断用户使用的请求方式
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)

        # 验证用户数据时候有效
        if user_login_form.is_valid():
            
            # 清理出合法数据
            data = user_login_form.cleaned_data
            
            #验证用户信息,并返回user对象
            user = authenticate(
                username = data['username'],
                paasword = data['password']
            )
            # 判断用户是否登录
            if user:
                # 已登录则将数据保存在session中,即实现了登录动作
                login(request, user)

                # 登录后则返回到文章页面
                return redirect("article:article_list.html")
            else:
                return HttpResponse("账户名或者密码有误,请重新输入")
        else:
            return HttpResponse("账号名或者密码不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {
            'form': user_login_form,
        }
        return render(request, 'user/login.html', context)
    else:
        return HttpResponse("请求方式有误,请使用 'GET' 或者 'POST'请求数据")