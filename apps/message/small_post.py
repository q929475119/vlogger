from django.shortcuts import render
from django.http import HttpResponse
from apps.message.models import Post, User, Comment, Like, Oppose, Collect, Block, TopPost
from django.db.models import Q


def like(request):
    user = request.POST.get("loginuser")
    post_id = request.POST.get("post_id")
    record = Like.objects.filter(Q(useraccount=user) & Q(post=post_id))
    record_dislike=Oppose.objects.filter(Q(useraccount=user) & Q(post=post_id))
    if record:
        record.delete()
        return HttpResponse("取消点赞")
    else:
        if record_dislike:
            record_dislike.delete()#如果已反对，则取消反对
        likes = Like()
        likes.useraccount = User.objects.get(account=user)
        likes.post = Post.objects.get(id=post_id)
        likes.save()
        return HttpResponse("点赞成功")


def oppose(request):
    user = request.POST.get("loginuser")
    post_id = request.POST.get("post_id")
    record = Oppose.objects.filter(Q(useraccount=user) & Q(post=post_id))
    record_like = Like.objects.filter(Q(useraccount=user) & Q(post=post_id))
    if record:
        record.delete()
        return HttpResponse("取消反对")
    else:
        if record_like:
            record_like.delete()#如果已点赞，则取消点赞
        dislikes = Oppose()
        dislikes.useraccount = User.objects.get(account=user)
        dislikes.post = Post.objects.get(id=post_id)
        dislikes.save()
        return HttpResponse("反对成功")


def collect(request):
    loginuser = request.POST.get("loginuser")
    user = User.objects.get(account=loginuser)
    post_id = request.POST.get("post_id")
    post = Post.objects.get(id=post_id)
    record = Collect.objects.filter(Q(useraccount=user) & Q(post=post))
    if record:
        record.delete()
        return HttpResponse("取消收藏")
    else:
        collect = Collect()
        collect.useraccount = User.objects.get(account=loginuser)
        collect.post = Post.objects.get(id=post_id)
        collect.save()
        return HttpResponse("收藏成功")


def small_post(request, id, loginuser=""):
    post = Post.objects.get(id=id)  # 通过帖子id找到帖子
    account = User.objects.get(account=post.initiator)  # 找到帖子发起者
    if loginuser=="":
        likecolor = "#808080"
        dislikecolor = "#808080"
        collectcolor = "#808080"
        dislike_icon = "fa fa-thumbs-o-down"
        like_icon = "fa fa-thumbs-o-up"
        collect_icon = "fa fa-star-o"
        content = Comment.objects.get(Q(post=post) & Q(floor_number=0))
    else:
        user = User.objects.get(account=loginuser)
        content = Comment.objects.get(Q(post=post) & Q(floor_number=0))
        likedone = Like.objects.filter(Q(post=post) & Q(useraccount=user))
        dislikedone = Oppose.objects.filter(Q(post=post) & Q(useraccount=user))
        collectdone = Collect.objects.filter(Q(post=post) & Q(useraccount=user))
        if len(likedone) == 0:
            likecolor = "#808080"
            like_icon="fa fa-thumbs-o-up"
        else:
            likecolor = "#eb7350"
            like_icon = "fa fa-thumbs-up"
        if len(dislikedone) == 0:
            dislikecolor = "#808080"
            dislike_icon = "fa fa-thumbs-o-down"
        else:
            dislikecolor = "#eb7350"
            dislike_icon = "fa fa-thumbs-down"
        if len(collectdone) == 0:
            collectcolor = "#808080"
            collect_icon = "fa fa-star-o"
        else:
            collectcolor = "#eb7350"
            collect_icon = "fa fa-star"

    context = {'profilepicture': account.ProfilePicture, 'post': post, 'content': content.discussion,
               'likecolor': likecolor, 'like_icon':like_icon, 'dislikecolor': dislikecolor, 'dislike_icon':dislike_icon,
               'collectcolor': collectcolor, 'collect_icon':collect_icon, 'loginuser':loginuser}
    return render(request, 'small_post.html', context)
