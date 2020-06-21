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


@register.simple_tag
def custom_paginator(page, num_total_pages=9, num_back_pages=3):
    """
    page: 分页的页码对象；在views.py中创建的；
    num_total_pages：预定义整个分页器展示10个页码；
    num_back_pages：预定义，当前页码后面少于4个页码的时候，分页器开始滚动，最后无法滚动的除外。

    分页的情况：(默认展示10个分页按钮，并且保证当前点击的页码后面至少是4个页码)
    总页数如果没有超过10页，则页码全部展示，且没有滚动符...
    总页数超过10页的情况：
    1.从第一页到第6页，点击哪一个页码，这个页码被选中，并且整个分页器没有滚动，没有...省略符；
    2.从第7页到第36页，分页器滚动，所点击的页码始终位于中心位置，且出现...省略符；预定义当前选中页码前面是3个页码(不包含1和...)后面展示4个页码；
    3.从第37页开始往后，分页器不滚动，所点击的页码不位于中心位置；
    :return:

    """
    html = ''
    if page.paginator.num_pages == 1:
        # 如果只分一页，不显示分页
        return html
    elif page.paginator.num_pages <= num_total_pages:
        # 分页的总页数不超过10页，不考虑当前点击的页码是否是中心位置了：
        for x in range(1, page.paginator.num_pages + 1):
            html += '<a href="?page=%s"><button type="button" class="PagButton PaginationButton">%s</button></a>' % (x, x)
        return html
    elif page.number <= num_total_pages - num_back_pages:
        for x in range(1, num_total_pages + 1):
            html += '<a href="?page=%s"><button type="button" class="PagButton PaginationButton">%s</button></a>' % (x, x)
        return html
    # (num_total_pages - num_back_pages - 3):预定义当前选中页码前面是3个页码(不包含1和...)
    elif num_total_pages - (
            num_total_pages - num_back_pages - 3) <= page.number <= page.paginator.num_pages - num_back_pages:
        html += '''
        <a href="?page=1"><button type="button" class="PagButton PaginationButton">1</button></a>
        <a href="?page=%s"><button disabled type="button" class="PagButton PaginationButton">...</button></a>
        '''
        # 1...2 3 4 5 6 7 8 9
        for x in range(page.number - (num_total_pages - num_back_pages - 3), page.number + num_back_pages + 1):
            html += '<a href="?page=%s"><button type="button" class="PagButton PaginationButton">%s</button></a>' % (x, x)
        return html
    else:
        # 最后无法滚动的部分
        html += '''
        <a href="?page=1"><button type="button" class="PagButton PaginationButton">1</button></a>
        <a href="?page=%s"><button disabled type="button" class="PagButton PaginationButton">...</button></a>
        '''
        for x in range(page.paginator.num_pages - (num_total_pages - num_back_pages - 3) - num_back_pages,
                       page.paginator.num_pages + 1):
            html += '<a href="?page=%s"><button type="button" class="PagButton PaginationButton">%s</button></a>' % (x, x)
        return html
