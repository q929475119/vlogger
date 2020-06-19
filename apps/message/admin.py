from django.contrib import admin
from apps.message import models

admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.File)
admin.site.register(models.Block)
admin.site.register(models.Topic)
admin.site.register(models.Comment)
admin.site.register(models.Reply)
admin.site.register(models.Like)
admin.site.register(models.LikeComment)
admin.site.register(models.Collect)
admin.site.register(models.CollectComment)
admin.site.register(models.Oppose)
admin.site.register(models.OpposeComment)
admin.site.register(models.Friend)
admin.site.register(models.ExcellentPost)
admin.site.register(models.TopPost)
