from django.urls import path
from apps.message.UserCenter_Views import UserCenterCommentView, UserCenterPostView, \
    UserCenterReplyView, UploadAvatarView, ChangePasswordView
from apps.message.UserCenter_Views import posts_by_votes, posts_by_votes_collect

urlpatterns = [
    path('<loginuser>', UserCenterPostView.as_view(), name='center'),  # 设置主页显示就是发起的帖子页面
    path('posts/by_votes_collect/<loginuser>', posts_by_votes_collect, name='posts_votes_collect'),
    path('posts/by_votes/<loginuser>', posts_by_votes, name='posts_votes'),
    path('posts/<loginuser>', UserCenterPostView.as_view(), name='post'),
    # path('comments/by_votes/<loginuser>', comments_by_votes, name='comments_votes'),
    path('comments/<loginuser>', UserCenterCommentView.as_view(), name='comment'),
    # path('replies/by_votes/<loginuser>', replies_by_votes, name='replies_votes'),
    path('replies/<loginuser>', UserCenterReplyView.as_view(), name='reply'),
    path('upload/avatar/<loginuser>', UploadAvatarView.as_view(), name='upload_avatar'),  # 上传图片的路由配置
    path('change/password/<loginuser>', ChangePasswordView.as_view(), name='change_update'),  # 修改密码
]
