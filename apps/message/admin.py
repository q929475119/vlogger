from django.contrib import admin
from apps.message import models


class UserAdmin(admin.ModelAdmin):
    # 不知道是不是我这电脑的原因，如果是默认注册的话，会[WinError 3] 系统找不到指定的路径。: ''
    # 后来排查加上"ProfilePicture"字段，应该与FilePathField字段有关，不知道怎么解决
    fields = ["account", "password", "email", "nickname", "authority"]


class CommentAdmin(admin.ModelAdmin):
    fields = ["post", "owner", "discussion", "floor_number"]


class ReplyAdmin(admin.ModelAdmin):
    fields = ["post", "owner", "discussion", "floor_number", "comment"]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Post)
admin.site.register(models.File)
admin.site.register(models.Block)
admin.site.register(models.Topic)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Reply, ReplyAdmin)
admin.site.register(models.Like)
admin.site.register(models.LikeComment)
admin.site.register(models.Collect)
admin.site.register(models.CollectComment)
admin.site.register(models.Oppose)
admin.site.register(models.OpposeComment)
admin.site.register(models.Friend)
admin.site.register(models.ExcellentPost)
admin.site.register(models.TopPost)
