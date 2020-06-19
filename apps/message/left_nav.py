from django.shortcuts import render
from django.http import HttpResponse
from apps.message.models import Post, User, Comment, Like, Oppose, Collect, Block, TopPost
from django.db.models import Q


def gettopposts(request,loginuser=""):
    posts = []
    topposts = TopPost.objects.all()
    if len(topposts) > 0:
        for i in topposts:
            posts.append(i.post.id)
        return HttpResponse(posts)
    else:
        return HttpResponse("None")


def getlikes(request, loginuser):
    user = User.objects.get(account=loginuser)
    likes = Like.objects.filter(useraccount=user)
    post = []
    if len(likes) > 0:
        for i in likes:
            post.append(i.post.id)
        return HttpResponse(post)
    else:
        return HttpResponse("None")


def getcollect(request, loginuser):
    user = User.objects.get(account=loginuser)
    collect = Collect.objects.filter(useraccount=user)
    post = []
    if len(collect) > 0:
        for i in collect:
            post.append(i.post.id)
        return HttpResponse(post)
    else:
        return HttpResponse("None")


def getblock(request, blockid):
    posts = Post.objects.filter(block=blockid)
    post = []
    if len(posts) > 0:
        for i in posts:
            post.append(i.id)
        return HttpResponse(post)
    else:
        return HttpResponse("None")
