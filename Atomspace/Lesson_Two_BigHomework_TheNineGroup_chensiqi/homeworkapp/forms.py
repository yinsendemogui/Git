#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from homeworkapp.models import UserProfile

def word_validator(comment):
    if len(comment) < 4:
        raise ValidationError("not enough words")

def comment_validator(comment):
    keywords = [u"发票", u"钱"]
    for keyword in keywords:
        if keyword in comment:
            raise ValidationError("Your comment contains invalid words,please check it again.")

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages = {
            "required": 'wow, such words'
            },
        validators = [word_validator, comment_validator]
        )

class ProfileForm(ModelForm):

    # name = forms.CharField(max_length=50)
    # CHOICE = (
    #     ('性别', '性别'),
    #     ('男', '男'),
    #     ('女', '女')
    # )
    # sex = forms.ChoiceField(choices=CHOICE)
    # password = forms.CharField(max_length=50)
    # avatar_img = forms.ImageField()
    class Meta:
        model = UserProfile
        fields = ('name','sex','password','avatar_img')