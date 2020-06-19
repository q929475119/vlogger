import os
from django.shortcuts import render
from django.views.generic.base import View  # 基于类实现需要继承的view


# from apps.message.models import User, Post


class UserCenterView(View):
    # def get(self, request):
    #     id = 1
    #     post = Post.objects.get(id=id)
    #     account = User.objects.get(account=post.initiator)
    #     return render(request, "UserCenter-base.html", {
    #         'profilepicture': account.profilepicture, 'account': post.initiator, 'title': post.title,
    #         'time': post.time
    #     })
    def get(self, request):
        return render(request, "UserCenter-base.html", {

        })


class UserCenterAnswerView(View):
    def get(self, request):
        return render(request, "UserCenter-answer.html", {

        })


class UserCenterPostView(View):
    def get(self, request):
        return render(request, "UserCenter-post.html", {

        })


##########################################################################
import os
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.utils import timezone
from .models import Post, File


def getcreate_post(request):
	#更改
    if request.method == "POST":
        file_obj = request.FILES.get('file')
        upload_file = None
        if file_obj:
            accessory_dir = "media"
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
        post_txt = request.POST.get("title", '')
        post_list = post_txt.split("#")
        topic_name = post_list[1]
        post_text = post_list[-1]
        post_t_list = post_text.split("】")
        post_comment = post_t_list[-1]
        post_title = post_t_list[0].split("【")[-1]
        block = request.POST.get('block', '')
        print(block)
        post_message = Post()
        user_message = User.objects.get(nickname='zhangsan')
        topic_message = Topic()
        block_message = Post.objects.get(name=block)
        comment_message = Comment()
        topic_find = Topic.objects.filter(title=topic_name)
        if topic_find:
            pass
        else:
            topic_message.title = topic_name
            block_get = Block.objects.get(id=int(block))
            topic_message.block = block_get
            topic_message.save()  # 存新话题
        topic_find2 = Topic.objects.get(title=topic_name)
        post_message.initiator = user_message
        post_message.topic = topic_name
        post_message.title = post_title
        post_message.block = block_message
        post_message.topic = topic_find2
        post_message.save()  # 存帖子信息
        comment_message.post = post_message
        comment_message.owner = user_message
        comment_message.floor_number = 0
        comment_message.discussion = post_comment
        comment_message.save()  # 存评论0楼

    return render(request, "create_post.html")
