from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# 引入创建好的 form 表单
from .form import UserLoginForm, UserRegisterForm
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
            
            # 验证用户信息,并返回user对象
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            # 判断用户是否登录
            if user:
                # 已登录则将数据保存在session中,即实现了登录动作
                login(request, user)

                # 登录后则返回到文章页面
                return redirect("blog:article_list")
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


def user_logout(request):
    """
    用户登出
    """
    logout(request)
    return redirect("blog:article_list")


def user_register(request):
    """
    用户注册
    """
    if request.method == "POST":
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            add_user = user_register_form.save(commit=False)

            # 设置密码
            add_user.set_password(user_register_form.cleaned_data['password'])
            add_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, add_user)
            return redirect("user:login")
        else:
            return HttpResponse("注册表单有误，请重新输入")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {
            "form": user_register_form
        }
        return render(request, 'user/register.html', context)
    else:
        return HttpResponse("非法请求数据")
    