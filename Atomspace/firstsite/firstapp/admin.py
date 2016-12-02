from django.contrib import admin
from firstapp.models import People
from firstapp.models import Aritcle
from firstapp.models import Comment
# Register your models here.

admin.site.register(People)
admin.site.register(Aritcle)
admin.site.register(Comment)


