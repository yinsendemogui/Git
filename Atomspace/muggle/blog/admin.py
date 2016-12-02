#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.contrib import admin
from blog.models import UserProfile, Topic, Question, Answer, Comment,Ticket
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'



class TicketInline(admin.StackedInline):
    model = Ticket
    can_delete = False
    verbose_name_plural = 'Ticket'



class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,TicketInline )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Ticket)

# 超级管理员账号密码: Admin/Admin123456
