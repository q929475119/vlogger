# -*- coding: utf -8 -*-

from django.shortcuts import render, redirect
from . import models
from .models import User
from .models import Like
from .forms import UserForm
from .forms import RegisterForm

from apps.message.UserCenter_Views import hash_password


# Create your views here.

def get_index(request):
    pass
    return render(request, 'login_index.html')


def get_login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(account=username)
                if user.password == hash_password(password):  # # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_account'] = user.account
                    request.session['ProfilePicture'] = user.ProfilePicture

                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'user_login.html', locals())

    login_form = UserForm()
    return render(request, 'user_login.html', locals())


def get_register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            nickname = register_form.cleaned_data['nickname']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login_register.html', locals())
            else:
                same_name_user = models.User.objects.filter(account=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login_register.html', locals())
                same_nickname_user = models.User.objects.filter(nickname=nickname)
                if same_nickname_user:  # 昵称唯一
                    message = '该昵称已经存在，请重新选择昵称！'
                    return render(request, 'login_register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login_register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.account = username
                new_user.nickname = nickname
                new_user.password = hash_password(password1)  # 使用加密密码
                new_user.email = email
                new_user.ProfilePicture = '/media/avatar/default.jpg'  # 由于新建的用户没有上传头像，采用默认头像
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login_register.html', locals())


def get_logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")
