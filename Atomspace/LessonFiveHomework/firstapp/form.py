from django import forms
from django.core.exceptions import ValidationError


def words_validators(comment):
    if len(comment) < 4 :
        raise ValidationError('not enough words!')



def comment_validators(comment):
    if '发票' in comment or '钱' in comment:
        raise ValidationError('You comment contains invalid words,please check it again.')


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'requied': 'please write something'
        },
        validators=[comment_validators,words_validators]
    )

