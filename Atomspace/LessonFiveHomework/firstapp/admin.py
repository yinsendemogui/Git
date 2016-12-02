from django.contrib import admin

# Register your models here.
from firstapp.models import Article, Comment,UserProfile,Topic,Question

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Question)