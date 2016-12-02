#!/usr/bin/python
# -*- coding: utf-8 -*-


from django import forms
from django.core.exceptions import ValidationError


def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('字数不足')

def comment_validator(comment):
    if 'a' in comment:
        raise ValidationError('不能用a字符')



class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required':'不能为空！'
        },
        validators=[words_validator,comment_validator]
    )
