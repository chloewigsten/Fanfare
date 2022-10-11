from email.message import Message
from django.contrib import admin
from .models import Celeb, Photo, BlindItem, Article, Video, MessageBoard, PhotoComments, VideoComment, ArticleComment, BlindItemComment, MessageBoardComment

admin.site.register(Celeb)
admin.site.register(Photo)
admin.site.register(BlindItem)
admin.site.register(Article)
admin.site.register(Video)
admin.site.register(MessageBoard)
admin.site.register(PhotoComments)
admin.site.register(VideoComment)
admin.site.register(ArticleComment)
admin.site.register(BlindItemComment)
admin.site.register(MessageBoardComment)
