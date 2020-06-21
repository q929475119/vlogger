from django.shortcuts import render,redirect
import os
from django.http import HttpResponse
# Create your views here.
from .models import Post, File, Block, User, Topic, Comment, TopPost
import json
from django.db.models import Q



def index(request, blockid=None, childblock=None):
    # 获取登录用户user，用于主页显示登录的头像
    user = None
    if request.session.get('is_login', None):
        user = User.objects.get(account=request.session["user_account"])

    # 存评论0楼
    topic_all = Topic.objects.all()
    topic_all_list = []
    for topic in topic_all:
        topic_all_list.append({"title": topic.title})

    # 左导航栏部分
    block0 = []
    block1 = []
    block2 = []
    block3 = []
    block = Block.objects.filter(parent=1)
    for i in block:
        block0.append(i.name)
    block = Block.objects.filter(parent=2)
    for i in block:
        block1.append(i.name)
    block = Block.objects.filter(parent=3)
    for i in block:
        block2.append(i.name)
    block = Block.objects.filter(parent=4)
    for i in block:
        block3.append(i.name)
    if len(block0) == 0:
        block0 = "None"
    if len(block1) == 0:
        block1 = "None"
    if len(block2) == 0:
        block2 = "None"
    if len(block3) == 0:
        block3 = "None"

    # 搜索
    result = []
    if request.method == 'POST':
        content = request.POST.get('content')
        if content != None and len(content) > 0:
            results1 = Post.objects.filter(title__contains=content)
            for i in results1:
                result.append(i.id)
            topic_id = Topic.objects.filter(title__contains=content)
            if len(topic_id) > 0:
                for i in topic_id:
                    results2 = Post.objects.filter(topic=i)
                for i in results2:
                    result.append(i.id)
        else:  # 无搜索内容则返回热门帖子id
            topposts = TopPost.objects.all()
            if len(topposts) > 0:
                for i in topposts:
                    result.append(i.post_id)
            topposts = Post.objects.order_by('-time')
            if len(topposts) > 0:
                for i in topposts:
                    result.append(i.id)
    elif blockid != None:
        childblockid = Block.objects.get(Q(parent=int(blockid) + 1) & Q(name=childblock))
        result2 = Post.objects.filter(block=childblockid)
        for i in result2:
            result.append(i.id)
    else:  # 返回主页帖子id
        for i in TopPost.objects.all():
            result.append(i.post_id)
        topposts = Post.objects.order_by('-time')
        if len(topposts) > 0:
            for i in topposts:
                result.append(i.id)
    block_all = {'block0': block0, 'block1': block1, 'block2': block2, 'block3': block3}
    context = {'block0': block0, 'block1': block1, 'block2': block2, 'block3': block3,
               'result': result, 'topic_all': json.dumps(topic_all_list), 'block_all': json.dumps(block_all)}

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
    context = {'block0': block0, 'block1': block1, 'block2': block2, 'block3': block3,
               'result': result, 'topic_all': json.dumps(topic_all_list), 'block_all': json.dumps(block_all),
               'top_posts': top_posts, "user": user
               }
    return render(request, 'index.html', context)

def createpost(request):
    # 发布帖子
    if request.method == "POST":
        file_obj = request.FILES.get('file')
        upload_file = None

        post_title = request.POST.get("title", '')
        topic_name = request.POST.get("topic_select", "")
        post_comment = request.POST.get("post_text", "")
        block = request.POST.get('block', '')
        login_user = request.POST.get('login_user', '')
        post_message = Post()
        user_message = User.objects.get(account=login_user)
        topic_message = Topic()
        block_message = Block.objects.get(name=block)
        comment_message = Comment()
        topic_find = Topic.objects.filter(title=topic_name)
        if topic_find:
            pass
        else:
            topic_message.title = topic_name
            topic_message.block = block_message
            topic_message.save()  # 存新话题
        topic_find2 = Topic.objects.get(title=topic_name)
        post_message.initiator = user_message
        post_message.topic = topic_find2
        post_message.title = post_title
        post_message.block = block_message
        post_message.save()  # 存帖子信息
        comment_message.post = post_message
        comment_message.owner = user_message
        comment_message.floor_number = 0
        comment_message.discussion = post_comment
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
            comment_message.img ='/'+upload_file
            comment_message.save()
    return redirect('/index/')