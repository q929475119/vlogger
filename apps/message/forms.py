# _*_ coding:utf-8 _*_
from apps.message.models import User

from django import forms  # 引入django表单
from captcha.fields import CaptchaField


class PasswordForm(forms.Form):
    # 表单用于验证密码数据
    password0 = forms.CharField(max_length=20, min_length=6)
    password1 = forms.CharField(max_length=20, min_length=6)
    password2 = forms.CharField(max_length=20, min_length=6)


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9a-zA-Z]+',
               'title': '用户名只能是数字和英文字母!'}))
    nickname = forms.CharField(label="昵称", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=20, min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '6-20位非中文字符'}))
    password2 = forms.CharField(label="确认密码", max_length=20, min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '6-20位非中文字符'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')
