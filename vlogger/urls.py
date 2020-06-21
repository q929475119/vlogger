"""vlogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, re_path, include
from apps.message.search import search
from apps.message.small_post import small_post, like, oppose, collect
from apps.message.left_nav import getlikes, getcollect, getblock, gettopposts
from apps.message.views import getcreate_post
from apps.message.post_detail import post_detail,like as like1,put_post,createcomment
from apps.message.index import index,createpost
from apps.message.login import get_login, get_register, get_logout, get_index
from django.conf import settings             # 新加入
from django.conf.urls.static import static   # 新加入
urlpatterns = [
    path('admin/', admin.site.urls),
    # 帖子缩略视图+搜索栏+左导航栏
    path('search/<loginuser>', search),
    path('small_post/<id>/<loginuser>', small_post),
    path('small_post/<id>', small_post),
    path('like/', like),
    path('oppose/', oppose),
    path('collect/', collect),
    path('getlikes/<loginuser>', getlikes),
    path('getcollect/<loginuser>', getcollect),
    path('gettopposts/<loginuser>', gettopposts),
    # 个人中心的公共路径，剩余的路径去message.urls中匹配
    path('usercenter/', include('apps.message.urls')),
    path('create_post/', getcreate_post),
    path('post_detail/<int:post_id>/',post_detail),
    path('like1/',like1),
    path('put_posts/',put_post),
    path('index/<blockid>/<childblock>', index),
    path('index/', index),
    path('createpost/',createpost),
    path('createcomment/',createcomment),
    # 登陆注册
    path('login_index/', get_index),
    path('login/', get_login),
    path('register/', get_register),
    path('logout/', get_logout),
    path('captcha/', include('captcha.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
