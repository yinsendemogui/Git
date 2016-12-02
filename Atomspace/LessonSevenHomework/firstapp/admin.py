from django.contrib import admin

# Register your models here.
from firstapp.models import Article,UserProfile,Ticket

admin.site.register(Article)
admin.site.register(UserProfile)
admin.site.register(Ticket)
