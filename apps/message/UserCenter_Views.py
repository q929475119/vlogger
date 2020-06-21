# 在这里编写视图函数，就不用views.py的类了，避免合并冲突
import os
import json
import hashlib

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View  # 基于类实现需要继承的view
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage  # 引入django自带的分页功能

from apps.message import models
from apps.message import forms


class UserCenterPostView(View):
    # 获取当前登录用户的所有帖子  显示的缩略图是帖子题目和该帖子楼层为0的内容

    def get(self, request, loginuser):
        user = get_object_or_404(models.User, account=loginuser)

        user_account_session = None
        try:
            user_account_session = request.session['user_account']
        except:
            is_same_user = False
        is_same_user = (user_account_session == user.account)

        # 先根据用户获取楼层号为1的回复，进而在模板中通过外键获取所属的帖子
        first_comments = models.Comment.objects.filter(floor_number=0, owner=user).order_by("-time")
        posts_counts = first_comments.count()

        # 分页
        paginator = Paginator(first_comments, 6)
        page_num = request.GET.get('page', '1')
        try:
            page = paginator.page(page_num)
        except(PageNotAnInteger, EmptyPage, InvalidPage):  # 不合法的分页到第一页
            page = paginator.page('1')

        posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)

        is_active_post = True
        return render(request, "UserCenter-post.html", {
            "user": user, "is_same_user": is_same_user,
            "posts_counts": posts_counts, "posts_like_counts": posts_like_counts,
            "posts_collect_counts": posts_collect_counts, "posts_liked_counts": posts_liked_counts,
            "posts_collected_counts": posts_collected_counts, "is_active_post": is_active_post,
            "page_num": page_num, "page": page
        })


def posts_by_votes(request, loginuser):
    user = get_object_or_404(models.User, account=loginuser)

    user_account_session = None
    try:
        user_account_session = request.session['user_account']
    except:
        is_same_user = False
    is_same_user = (user_account_session == user.account)

    posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)

    first_comments = models.Comment.objects.filter(floor_number=0, owner=user)  # 获取0层评论，即帖子正文(对齐点赞相当于对帖子点赞？)
    posts_counts = first_comments.count()

    post2like = {}
    # 获取帖子的赞数和帖子id的字典
    for first_comment in first_comments:
        post = first_comment.post
        post_id = first_comment.post.id
        likes = post.like_set.count()  # 获取该帖子的所有喜欢数
        post2like[post_id] = likes

    # 根据字典的值(也就是赞同数)降序排序
    post2like_sorted = sorted(post2like.items(), key=lambda x: x[1], reverse=True)  # 转化成了排序后的列表套元组
    first_comments = []  # 重置原列表，根据排序后帖子的id重新获取第一个回复
    for post_id, _ in post2like_sorted:  # 只取第一个参数帖子id
        first_comment = models.Comment.objects.get(post__id=post_id, floor_number=0)
        first_comments.append(first_comment)

    # 分页
    paginator = Paginator(first_comments, 6)
    page_num = request.GET.get('page', '1')
    try:
        page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):  # 不合法的分页到第一页
        page = paginator.page('1')

    is_active_post = True

    return render(request, "UserCenter-post.html", {
        "user": user, "is_same_user": is_same_user,
        "posts_counts": posts_counts, "posts_like_counts": posts_like_counts,
        "posts_collect_counts": posts_collect_counts, "posts_liked_counts": posts_liked_counts,
        "posts_collected_counts": posts_collected_counts, "is_active_post": is_active_post,
        "page_num": page_num, "page": page
    })


def posts_by_votes_collect(request, loginuser):
    user = get_object_or_404(models.User, account=loginuser)

    user_account_session = None
    try:
        user_account_session = request.session['user_account']
    except:
        is_same_user = False
    is_same_user = (user_account_session == user.account)

    posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)

    first_comments = models.Comment.objects.filter(floor_number=0, owner=user)  # 获取0层评论，即帖子正文(对齐点赞相当于对帖子点赞？)
    posts_counts = first_comments.count()

    post2collect = {}
    # 获取帖子的赞数和帖子id的字典
    for first_comment in first_comments:
        post = first_comment.post
        post_id = first_comment.post.id
        collects = post.collect_set.count()  # 获取该帖子的所有喜欢数
        post2collect[post_id] = collects

    # 根据字典的值(也就是赞同数)降序排序
    post2collect_sorted = sorted(post2collect.items(), key=lambda x: x[1], reverse=True)  # 转化成了排序后的列表套元组
    first_comments = []  # 重置原列表，根据排序后帖子的id重新获取第一个回复
    for post_id, _ in post2collect_sorted:  # 只取第一个参数帖子id
        first_comment = models.Comment.objects.get(post__id=post_id, floor_number=0)
        first_comments.append(first_comment)

    is_active_post = True

    # 分页
    paginator = Paginator(first_comments, 6)
    page_num = request.GET.get('page', '1')
    try:
        page = paginator.page(page_num)
    except(PageNotAnInteger, EmptyPage, InvalidPage):  # 不合法的分页到第一页
        page = paginator.page('1')

    return render(request, "UserCenter-post.html", {
        "user": user, "is_same_user": is_same_user,
        "posts_counts": posts_counts, "posts_like_counts": posts_like_counts,
        "posts_collect_counts": posts_collect_counts, "posts_liked_counts": posts_liked_counts,
        "posts_collected_counts": posts_collected_counts, "is_active_post": is_active_post,
        "page_num": page_num, "page": page
    })


class UserCenterCommentView(View):
    # 获取当前登录用户的所有评论(Comment，不包括reply)，但不包括楼层号为0的评论
    # 显示的缩略图是帖子题目和评论内容

    # 获取所有是当前用户的评论，然后在模板中根据评论的外键获取帖子
    def get(self, request, loginuser):
        user = get_object_or_404(models.User, account=loginuser)

        user_account_session = None
        try:
            user_account_session = request.session['user_account']
        except:
            is_same_user = False

        is_same_user = (user_account_session == user.account)

        posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)

        # 按照时间降序排列，即最新的先显示
        comments = models.Comment.objects.filter(owner=user).filter(~Q(floor_number=0)).order_by("-time")
        comments_counts = comments.count()

        # 分页
        paginator = Paginator(comments, 6)
        page_num = request.GET.get('page', '1')
        try:
            page = paginator.page(page_num)
        except(PageNotAnInteger, EmptyPage, InvalidPage):  # 不合法的分页到第一页
            page = paginator.page('1')

        is_active_comment = True
        return render(request, "UserCenter-comment.html", {
            "user": user, "is_same_user": is_same_user, "posts_like_counts": posts_like_counts,
            "posts_collect_counts": posts_collect_counts, "posts_liked_counts": posts_liked_counts,
            "posts_collected_counts": posts_collected_counts, "comments_counts": comments_counts,
            "is_active_comment": is_active_comment, "page_num": page_num, "page": page
        })


# def comments_by_votes(request, loginuser):
#     """TODO: 对评论点赞、反对、收藏未实现，否则无法进行排序"""
#     user = get_object_or_404(models.User, account=loginuser)
#
#     user_account_session = None
#     try:
#         user_account_session = request.session['user_account']
#     except:
#         is_same_user = False
#     is_same_user = (user_account_session == user.account)
#
#     posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)
#
#     is_active_comment = True
#     return render(request, "UserCenter-comment.html", locals())


class UserCenterReplyView(View):
    # 获取当前登录用户的所有回复(仅包括reply)
    # 显示的缩略图是帖子题目和回复内容

    # 获取所有是当前用户的回复，然后在模板中根据评论的外键获取帖子
    def get(self, request, loginuser):
        user = get_object_or_404(models.User, account=loginuser)

        user_account_session = None
        try:
            user_account_session = request.session['user_account']
        except:
            is_same_user = False
        is_same_user = (user_account_session == user.account)

        posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)

        # 按照时间降序排列，即最新的先显示
        replies = models.Reply.objects.filter(owner=user).order_by("-time")
        replies_counts = replies.count()
        is_active_reply = True

        # 分页
        paginator = Paginator(replies, 6)
        page_num = request.GET.get('page', '1')
        try:
            page = paginator.page(page_num)
        except(PageNotAnInteger, EmptyPage, InvalidPage):  # 不合法的分页到第一页
            page = paginator.page('1')

        return render(request, "UserCenter-reply.html", {
            "user": user, "is_same_user": is_same_user, "posts_like_counts": posts_like_counts,
            "posts_collect_counts": posts_collect_counts, "posts_liked_counts": posts_liked_counts,
            "posts_collected_counts": posts_collected_counts, "is_active_reply": is_active_reply,
            "replies_counts": replies_counts, "page_num": page_num, "page": page
        })


# def replies_by_votes(request, loginuser):
#     """TODO: 对回复点赞、反对、收藏未实现，否则无法进行排序"""
#     user = get_object_or_404(models.User, account=loginuser)
#
#     user_account_session = None
#     try:
#         user_account_session = request.session['user_account']
#     except:
#         is_same_user = False
#     is_same_user = (user_account_session == user.account)
#
#     posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts = counts(user)
#
#     is_active_reply = True
#     return render(request, "UserCenter-reply.html", locals())


class UploadAvatarView(View):
    # 修改用户头像

    def get(self, request, loginuser):
        user = get_object_or_404(models.User, account=loginuser)
        is_active_post = True
        return render(request, "UserCenter-post.html", locals())

    def post(self, request, loginuser):
        upload_avatar = store_avatar = None

        avatar = request.FILES.get('ProfilePicture')
        user = models.User.objects.get(account=loginuser)

        # TODO：甲方需求：未显示上传的进度
        if avatar:  # 将图片保存到本地
            accessory_dir = "media/avatar/" + user.account
            if not os.path.isdir(accessory_dir):
                os.makedirs(accessory_dir)  # 创建多级目录

            upload_avatar = "%s/%s" % (accessory_dir, avatar.name)  # 存储到本地的路径
            with open(upload_avatar, 'wb') as new_file:
                for chunk in avatar.chunks():
                    new_file.write(chunk)

        user.ProfilePicture = '/' + upload_avatar
        user.save()
        request.session['ProfilePicture'] = user.ProfilePicture
        return HttpResponse('OK') # 上传头像F12控制台有:Refused to display 'http://127.0.0.1:8000/usercenter/upload/avatar/zhangsan' in a frame because it set 'X-Frame-Options' to 'deny'.


class ChangePasswordView(View):
    def get(self, request, loginuser):
        user = get_object_or_404(models.User, account=loginuser)
        is_active_post = True
        return render(request, "UserCenter-post.html", locals())

    def post(self, request, loginuser):
        user = models.User.objects.get(account=loginuser)
        password_form = forms.PasswordForm(request.POST)
        data = {
            "message": "请检查密码的长度!",
            "status": "fail"
        }

        if password_form.is_valid():  # 数据长度合法。从cleaned_data中获取数据
            password0 = password_form.cleaned_data['password0']
            password1 = password_form.cleaned_data['password1']
            password2 = password_form.cleaned_data['password2']

            if hash_password(password0) != user.password:  # 原密码和数据库存储的用户密码不同
                data["message"] = "原密码输入错误！"
                return HttpResponse(json.dumps(data), content_type='application/json')  # 返回json数据，由前端ajax的回调函数解析

            elif password1 != password2:  # 判断两次密码是否相同
                data["message"] = "两次输入密码不一致！"
                return HttpResponse(json.dumps(data), content_type='application/json')

            else:
                user.password = hash_password(password2)  # 可以考虑数据库中存储加密后的密码，这样需要改变密码长度
                user.save()
                data["status"] = "success"
                request.session.flush()  # 清除会话
                return HttpResponse(json.dumps(data), content_type='application/json')

        else:  # 验证数据失败说明密码长度不够
            return HttpResponse(json.dumps(data), content_type='application/json')


def hash_password(string, salt='vlogger'):  # 加点盐
    # Hash加密，返回64位十六进制数
    h = hashlib.sha256()
    string += salt
    h.update(string.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def counts(user: models.User):
    """用来根据传入的用户，返回该用户的点赞、收藏以及被点赞、被收藏数"""
    # 获取该用户所有点赞的帖子数
    posts_like_counts = models.Like.objects.filter(useraccount=user).count()
    # 获取该用户所有收藏
    posts_collect_counts = models.Collect.objects.filter(useraccount=user).count()
    # 获取该用户发起所有帖子的点赞数/收藏数
    posts_liked_counts = 0
    posts_collected_counts = 0

    posts = models.Post.objects.filter(initiator=user)  # 获取loginuser的所有帖子
    for post in posts:
        post_likes = post.like_set.count()
        post_collects = post.collect_set.count()
        posts_liked_counts += post_likes
        posts_collected_counts += post_collects

    return posts_like_counts, posts_collect_counts, posts_liked_counts, posts_collected_counts
