from django.contrib import admin

from mainpage.models import Article, Comment, LikeList

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeList)
# Register your models here.
