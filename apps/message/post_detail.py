import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.message.models import Post, User, Comment, Like, Oppose, Collect, Block, Reply, LikeComment, CollectComment, \
    OpposeComment, File
import json


def post_detail(request, post_id):
    if request.session.get('is_login', None):
        user_id = request.session['user_account']
        user = User.objects.get(account=user_id)
    else:
        user_id = ''
        user = None
    post = Post.objects.get(id=post_id)
    post.sort_num = post.sort_num + 1
    post.save()
    block_name = post.block.name
    block_parent = post.block.parent - 1
    title = post.title
    post_time = post.time
    # 获取楼层号为0的comment，也就是帖子正文内容
    post_con = Comment.objects.filter(post__id=post_id)
    post_content = post_con.filter(floor_number=0)[0].discussion
    post_img = post_con.filter(floor_number=0)[0].img
    if Like.objects.filter(post_id=post_id, useraccount_id=user_id):
        like = 1
    else:
        like = 0
    if Collect.objects.filter(post_id=post_id, useraccount_id=user_id):
        collect = 1
    else:
        collect = 0
    if Oppose.objects.filter(post_id=post_id, useraccount_id=user_id):
        dislike = 1
    else:
        dislike = 0
    comments = []
    for comment in post_con.filter(floor_number__gt=0):
        tmp = {}
        tmp['comment_id'] = comment.id
        tmp['floor_num'] = comment.floor_number
        tmp['comment_time'] = str(comment.time)
        tmp['user_img'] = comment.owner.ProfilePicture
        tmp['user_name'] = comment.owner.nickname
        tmp['comment_con'] = comment.discussion
        tmp['comment_img'] = comment.img
        tmp['reply_num'] = Reply.objects.filter(comment=comment).count()
        if LikeComment.objects.filter(comment_id=comment.id, useraccount_id=user_id):
            tmp['like'] = 1
        else:
            tmp['like'] = 0
        if CollectComment.objects.filter(comment_id=comment.id, useraccount_id=user_id):
            tmp['collect'] = 1
        else:
            tmp['collect'] = 0
        if OpposeComment.objects.filter(comment_id=comment.id, useraccount_id=user_id):
            tmp['dislike'] = 1
        else:
            tmp['dislike'] = 0

        tmp['reply_items'] = []
        for item in Reply.objects.filter(comment=comment):
            tmp2 = {}
            tmp2['user_img'] = item.owner.ProfilePicture
            tmp2['user_name'] = item.owner.nickname
            tmp2['floor_num'] = item.floor_number
            tmp2['reply_time'] = str(item.time)
            tmp2['reply_con'] = item.discussion
            tmp2['reply_img'] = item.img
            tmp['reply_items'].append(tmp2)
        comments.append(tmp)

    return render(request, 'test_component.html',
                  {'post_id': post_id, 'block_name': block_name, 'block_parent': block_parent, 'title': title,
                   'post_time': post_time, 'post_content': post_content,
                   'post_img': post_img, 'user': user,
                   'like_post': like, 'collect_post': collect, 'dislike_post': dislike,
                   'comments': json.dumps(comments)})


@csrf_exempt
def like(request):
    if request.method == 'POST':
        if request.session.get('is_login', None):
            user_id = request.session['user_account']
        else:
            user_id = ''
        con = json.loads(request.body, encoding="utf-8")
        # 关于post的like,collect,dislike
        if con['method'] == 'like_post' and con['post_id'] and con['value'] > 0:
            if Like.objects.create(useraccount_id=user_id, post_id=con['post_id']):
                return JsonResponse({'result': 1})
        elif con['method'] == 'collect_post' and con['post_id'] and con['value'] > 0:
            if Collect.objects.create(useraccount_id=user_id, post_id=con['post_id']):
                return JsonResponse({'result': 1})
        elif con['method'] == 'dislike_post' and con['post_id'] and con['value'] > 0:
            if Oppose.objects.create(useraccount_id=user_id, post_id=con['post_id']):
                return JsonResponse({'result': 1})
        elif con['method'] == 'like_post' and con['post_id'] and con['value'] == 0:
            Like.objects.filter(post_id=con['post_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result': 1})
        elif con['method'] == 'collect_post' and con['post_id'] and con['value'] == 0:
            Collect.objects.filter(post_id=con['post_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result': 1})
        elif con['method'] == 'dislike_post' and con['post_id'] and con['value'] == 0:
            Oppose.objects.filter(post_id=con['post_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result': 1})
        # 关于comment的like，collect，dislike
        elif con['method'] == 'like_comment' and con['comment_id'] and con['value'] > 0:
            if LikeComment.objects.create(useraccount_id=user_id, comment_id=con['comment_id']):
                return JsonResponse({'result': 1})
        elif con['method'] == 'like_comment' and con['comment_id'] and con['value'] == 0:
            LikeComment.objects.filter(comment_id=con['comment_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result': 1})
        elif con['method'] == 'collect_comment' and con['comment_id'] and con['value'] > 0:
            if CollectComment.objects.create(useraccount_id=user_id, comment_id=con['comment_id']):
                return JsonResponse({'result': 1})
        elif con['method'] == 'collect_comment' and con['comment_id'] and con['value'] == 0:
            CollectComment.objects.filter(comment_id=con['comment_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result': 1})
        elif con['method'] == 'dislike_comment' and con['comment_id'] and con['value'] > 0:
            if OpposeComment.objects.create(useraccount_id=user_id, comment_id=con['comment_id']):
                return JsonResponse({'result': 1})
        elif con['method'] == 'dislike_comment' and con['comment_id'] and con['value'] == 0:
            OpposeComment.objects.filter(comment_id=con['comment_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result': 1})
        return JsonResponse({'result': 0})
    return JsonResponse({'result': 0})


@csrf_exempt
def put_post(request):
    # 右侧导航栏
    top_posts = []
    top_fetch = Post.objects.order_by('-sort_num')
    if len(top_fetch) < 10:
        limit = len(top_fetch)
    else:
        limit = 10
    for i in range(0, limit):
        item = {}
        item['id'] = top_fetch[i].id
        item['title'] = top_fetch[i].title
        item['num'] = top_fetch[i].sort_num
        top_posts.append(item)
    return JsonResponse({'top_posts': top_posts})

@csrf_exempt
def createcomment(request):
    if request.method == "POST":
        if request.session.get('is_login', None):
            owner = request.session['user_account']
            owner=User.objects.get(account=owner)
        else:
            return JsonResponse('error',safe=False)
        file_obj = request.FILES.get('file')
        con=request.GET
        if (int(con['comment_id'])== 0):
            comment_message = Comment()
            comment_message.post = Post.objects.get(id=int(con['post_id']))
            comment_message.floor_number = Comment.objects.filter(post=comment_message.post).count()
            comment_message.discussion = con['post_text']
            comment_message.owner=owner
            comment_message.save()
            if file_obj:
                accessory_dir = "media/c" + str(comment_message.id)
                if not os.path.isdir(accessory_dir):
                    os.mkdir(accessory_dir)
                upload_file = "%s/%s" % (accessory_dir, file_obj.name)
                with open(upload_file, 'wb') as new_file:
                    for chunk in file_obj.chunks():
                        new_file.write(chunk)
                file_message = File()
                file_message.name = file_obj.name
                file_message.address = upload_file
                file_message.save()  # 存文件
                comment_message.img = '/' + upload_file
                comment_message.save()
        else:
            reply_message = Reply()
            reply_message.post = Post.objects.get(id=int(con['post_id']))
            reply_message.comment = Comment.objects.get(id=int(con['comment_id']))
            reply_message.floor_number = Reply.objects.filter(comment=reply_message.comment).count()
            reply_message.discussion =con['post_text']
            reply_message.owner=owner
            reply_message.save()
            if file_obj:
                accessory_dir = "media/r" + str(reply_message.id)
                if not os.path.isdir(accessory_dir):
                    os.mkdir(accessory_dir)
                upload_file = "%s/%s" % (accessory_dir, file_obj.name)
                with open(upload_file, 'wb') as new_file:
                    for chunk in file_obj.chunks():
                        new_file.write(chunk)
                file_message = File()
                file_message.name = file_obj.name
                file_message.address = upload_file
                file_message.save()  # 存文件
                reply_message.img = '/' + upload_file
                reply_message.save()
        return JsonResponse('success',safe=False)
