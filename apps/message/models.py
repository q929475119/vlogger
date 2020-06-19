# _*_ coding:utf-8 _*_
from django.db import models


# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=15, verbose_name="账号", primary_key="true")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.EmailField(max_length=30, verbose_name="邮箱")
    nickname=models.CharField(max_length=10,verbose_name='昵称',default='')
    ProfilePicture = models.FilePathField(max_length=80, verbose_name="ProfilePicture", default='')
    authority = models.IntegerField(verbose_name="权限",default='1')

    class Meta:
        verbose_name = "user info"

    def __str__(self):
        return self.account


class Post(models.Model):
    id = models.AutoField(verbose_name='帖子id', primary_key="true")
    title = models.CharField(max_length=30, verbose_name='帖子题目', default='')
    initiator = models.ForeignKey('User',on_delete=models.CASCADE)
    time = models.DateField(verbose_name='发帖时间',auto_now_add = True)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, default='')
    topic=models.ForeignKey('Topic',on_delete=models.CASCADE,null=True)
    sort_num=models.IntegerField(verbose_name='浏览量',default=0)
    def __str__(self):
        return self.title


class File(models.Model):
    id = models.AutoField(verbose_name='文件id', primary_key="true")
    name = models.CharField(max_length=20, verbose_name="文件名")
    address = models.CharField(max_length=80, verbose_name="文件地址")

    def __str__(self):
        return self.name



class Block(models.Model):
    id = models.AutoField(verbose_name='板块id', primary_key="true")
    name = models.CharField(verbose_name="板块名称", max_length=20)
    # parent=1,学术性板块
    # parent=2,资料分享板块
    # parent=3,功能性板块
    # parent=4，娱乐生活板块
    parent=models.SmallIntegerField(verbose_name='父板块',default=0)
    def __str__(self):
        return self.name

class Topic(models.Model):
    id=models.AutoField(verbose_name='话题id', primary_key="true")
    title=models.CharField(verbose_name='话题id',max_length=20)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(verbose_name='评论id', primary_key="true")
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    discussion = models.CharField(max_length=1000, verbose_name='帖子内容')
    time = models.DateField(verbose_name='帖子发出时间',auto_now_add=True)
    floor_number = models.IntegerField(verbose_name='楼层号')
    img=models.FilePathField(max_length=80,verbose_name='图片',default='')

    def __str__(self):
        return '帖子id' + str(self.post.id) + '  ' + '第几层评论' + str(self.floor_number)


class Reply(models.Model):
    id = models.AutoField(verbose_name='回复id', primary_key="true")
    post = models.ForeignKey('Post', on_delete=models.CASCADE,default='')
    owner = models.ForeignKey("User", on_delete=models.CASCADE,default='')
    discussion = models.CharField(max_length=1000, verbose_name='回复内容',default='')
    img=models.FilePathField(max_length=80,verbose_name='图片',default='')
    time = models.DateField(verbose_name='回复发出时间',default='')
    floor_number = models.IntegerField(verbose_name='楼层号',default=-1)
    comment = models.ForeignKey('Comment', verbose_name='被回复的comment', on_delete=models.CASCADE)

class Like(models.Model):
    useraccount=models.ForeignKey('User',on_delete=models.CASCADE,default='')
    post=models.ForeignKey('Post',on_delete=models.CASCADE,default='')

class LikeComment(models.Model):
    useraccount = models.ForeignKey('User', on_delete=models.CASCADE, default='')
    comment=models.ForeignKey('Comment',on_delete=models.CASCADE,default='')

class Collect(models.Model):
    useraccount = models.ForeignKey('User', on_delete=models.CASCADE, default='')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default='')

class CollectComment(models.Model):
    useraccount = models.ForeignKey('User', on_delete=models.CASCADE, default='')
    comment=models.ForeignKey('Comment',on_delete=models.CASCADE,default='')

class Oppose(models.Model):
    useraccount = models.ForeignKey('User', on_delete=models.CASCADE, default='')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default='')

class OpposeComment(models.Model):
    useraccount = models.ForeignKey('User', on_delete=models.CASCADE, default='')
    comment=models.ForeignKey('Comment',on_delete=models.CASCADE,default='')

class Friend(models.Model):
    friend1=models.ForeignKey('User',on_delete=models.CASCADE,related_name='friend1',default='')
    friend2 = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friend2', default='')

class ExcellentPost(models.Model):
    post=models.ForeignKey('Post',on_delete=models.CASCADE,default='')

class TopPost(models.Model):
    post=models.ForeignKey('Post',on_delete=models.CASCADE,default='')
