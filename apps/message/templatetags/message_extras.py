# django自定义模板，实现从后台获取点赞、反对、收藏的状态
from django import template
from django.db.models import Q
from apps.message import models

register = template.Library()


@register.simple_tag(name="post_color_like")
def post_color_like(loginuser, post_id):
    post = models.Post.objects.get(id=post_id)  # 通过帖子id找到帖子
    user = models.User.objects.get(account=loginuser)  # 通过登陆用户找到用户
    likedone = models.Like.objects.filter(Q(post=post) & Q(useraccount=user))
    if len(likedone):
        return "#eb7350"
    else:
        return "#808080"


@register.simple_tag(name="post_color_oppose")
def post_color_oppose(loginuser, post_id):
    post = models.Post.objects.get(id=post_id)  # 通过帖子id找到帖子
    user = models.User.objects.get(account=loginuser)  # 通过登陆用户找到用户
    opposedone = models.Oppose.objects.filter(Q(post=post) & Q(useraccount=user))
    if len(opposedone):
        return "#eb7350"
    else:
        return "#808080"


@register.simple_tag(name="post_color_collect")
def collect_color_oppose(loginuser, post_id):
    post = models.Post.objects.get(id=post_id)  # 通过帖子id找到帖子
    user = models.User.objects.get(account=loginuser)  # 通过登陆用户找到用户
    collectdone = models.Collect.objects.filter(Q(post=post) & Q(useraccount=user))
    if len(collectdone):
        return "#eb7350"
    else:
        return "#808080"


# 以下样式存在重复查询，没有想到好的解决方法，从后台获取颜色和样式。。。
@register.simple_tag(name="post_style_like")
def post_style_like(loginuser, post_id):
    post = models.Post.objects.get(id=post_id)  # 通过帖子id找到帖子
    user = models.User.objects.get(account=loginuser)  # 通过登陆用户找到用户
    likedone = models.Like.objects.filter(Q(post=post) & Q(useraccount=user))
    if len(likedone):
        return "fa fa-thumbs-up"
    else:
        return "fa fa-thumbs-o-up"


@register.simple_tag(name="post_style_oppose")
def post_style_oppose(loginuser, post_id):
    post = models.Post.objects.get(id=post_id)  # 通过帖子id找到帖子
    user = models.User.objects.get(account=loginuser)  # 通过登陆用户找到用户
    opposedone = models.Oppose.objects.filter(Q(post=post) & Q(useraccount=user))
    if len(opposedone):
        return "fa fa-thumbs-down"
    else:
        return "fa fa-thumbs-o-down"


@register.simple_tag(name="post_style_collect")
def collect_style_oppose(loginuser, post_id):
    post = models.Post.objects.get(id=post_id)  # 通过帖子id找到帖子
    user = models.User.objects.get(account=loginuser)  # 通过登陆用户找到用户
    collectdone = models.Collect.objects.filter(Q(post=post) & Q(useraccount=user))
    if len(collectdone):
        return "fa fa-star"
    else:
        return "fa fa-star-o"
