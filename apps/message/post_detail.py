from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.message.models import Post, User, Comment, Like, Oppose, Collect, Block,Reply,LikeComment,CollectComment,OpposeComment
import json
def post_detail(request,post_id):
    if request.session.get('is_login', None):
        user_id=request.session['user_account']
    else:
        user_id=''
    post = Post.objects.get(id=post_id)
    block_name = post.block.name
    title = post.title
    post_time = post.time
    # 获取楼层号为0的comment，也就是帖子正文内容
    post_con = Comment.objects.filter(post__id=post_id)
    post_content=post_con.filter(floor_number=0)[0].discussion
    if Like.objects.filter(post_id=post_id,useraccount_id=user_id):
        like=1
    else:
        like=0
    if Collect.objects.filter(post_id=post_id,useraccount_id=user_id):
        collect=1
    else:
        collect=0
    if Oppose.objects.filter(post_id=post_id,useraccount_id=user_id):
        dislike=1
    else:
        dislike=0
    comments = []
    for comment in post_con.filter(floor_number__gt=0):
        tmp = {}
        tmp['comment_id']=comment.id
        tmp['floor_num']=comment.floor_number
        tmp['comment_time']=str(comment.time)
        tmp['user_img']=comment.owner.ProfilePicture
        tmp['user_name']=comment.owner.nickname
        tmp['comment_con']=comment.discussion
        tmp['reply_num']=Reply.objects.filter(comment=comment).count()
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

        tmp['reply_items']=[]
        for item in Reply.objects.filter(comment=comment):
            tmp2={}
            tmp2['user_img']=item.owner.ProfilePicture
            tmp2['user_name']=item.owner.nickname
            tmp2['floor_num']=item.floor_number
            tmp2['reply_time']=str(item.time)
            tmp2['reply_con']=item.discussion
            tmp['reply_items'].append(tmp2)
        comments.append(tmp)

    return render(request, 'test_component.html',
                  {'post_id': post_id,'block_name': block_name, 'title': title, 'post_time': post_time, 'post_content': post_content,
                   'like_post':like,'collect_post':collect,'dislike_post':dislike,'comments': json.dumps(comments)})

@csrf_exempt
def like(request):
    if request.method=='POST':
        if request.session.get('is_login', None):
            user_id = request.session['user_account']
        else:
            user_id = ''
        con=json.loads(request.body,encoding="utf-8")
        #关于post的like,collect,dislike
        if con['method']=='like_post' and con['post_id'] and con['value'] > 0:
            if Like.objects.create(useraccount_id=user_id,post_id=con['post_id']):
                return JsonResponse({'result':1})
        elif con['method']=='collect_post' and con['post_id'] and con['value'] > 0:
            if Collect.objects.create(useraccount_id=user_id,post_id=con['post_id']):
                return JsonResponse({'result':1})
        elif con['method']=='dislike_post' and con['post_id'] and con['value'] > 0:
            if Oppose.objects.create(useraccount_id=user_id,post_id=con['post_id']):
                return JsonResponse({'result':1})
        elif con['method']=='like_post' and con['post_id'] and con['value'] == 0:
            Like.objects.filter(post_id=con['post_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result':1})
        elif con['method']=='collect_post' and con['post_id'] and con['value'] == 0:
            Collect.objects.filter(post_id=con['post_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result':1})
        elif con['method'] == 'dislike_post' and con['post_id'] and con['value'] == 0:
            Oppose.objects.filter(post_id=con['post_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result':1})
        #关于comment的like，collect，dislike
        elif con['method']=='like_comment' and con['comment_id'] and con['value']>0:
            if LikeComment.objects.create(useraccount_id=user_id,comment_id=con['comment_id']):
                return JsonResponse({'result':1})
        elif con['method']=='like_comment' and con['comment_id'] and con['value']==0:
            LikeComment.objects.filter(comment_id=con['comment_id']).filter(useraccount_id=user_id).delete()
            return JsonResponse({'result':1})
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
        return JsonResponse({'result':0})
    return JsonResponse({'result':0})