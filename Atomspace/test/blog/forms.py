from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re

def email_validator(comment):
    '''
    邮箱验证器
    author：陈思齐
    :param comment:
    :return:
    '''
    if not '@' in comment:
        raise ValidationError(u"邮箱格式错误")


def password_validator(comment):
    '''
    密码验证器
    author：陈思齐
    :param comment:
    :return:
    '''
    text = comment
    text = re.sub(u'\d+','',text)
    text = re.sub(u'[A-Za-z]+','',text)
    if len(comment) <= 6:
        raise ValidationError(u"密码不少于6位！")
    if len(text) != 0:
        raise ValidationError(u'密码只能包含英文和数字！')


def name_validator(comment):
    '''
    姓名验证器
    author：陈思齐
    :param comment:
    :return:
    '''
    text = comment
    text = re.sub(u'[\u4e00-\u9fa5]+', '', text)
    text = re.sub(u'[A-Za-z]', '', text)
    if len(comment) >= 14:
        raise ValidationError(u"用户名要小于14个字符！")
    if len(text) != 0:
        raise ValidationError(u"用户名只能包含中文和英文！")


def title_validator(comment):
    '''
    问题题目验证器
    author：陈思齐
    :param comment:
    :return:
    '''
    if len(comment) >= 50:
        raise ValidationError(u'请输入50个字符以内的问题')


def desc_validator(comment):
    '''
    问题内容验证器
    author：陈思齐
    :param comment:
    :return:
    '''
    if len(comment) >= 1000:
        raise ValidationError(u'请输入1000个字符以内的问题')


def topic_validator(comment):
    '''
    话题题目验证器
    author：陈思齐
    :param comment:
    :return:
    '''
    print (len(comment))
    if len(comment) >= 14:
        raise ValidationError(u'请输入14个字符以内的话题')


class LoginForm(forms.Form):
    '''
    登陆页表单
    author：陈思齐
    '''
    # 用户邮箱
    email = forms.CharField(
        required=True,
        # validators=[email_validator],
        widget=forms.TextInput(attrs={'type': 'email', 'placeholder': '邮箱'})
    )

    # 用户密码
    password = forms.CharField(
        error_messages = {
            "required": u'密码不能为空'
            },
        validators = [password_validator],
        widget=forms.TextInput(attrs={'type': 'password', 'placeholder': '密码'})
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        data_email = cleaned_data.get('email')
        data_password = cleaned_data.get('password')

        exist_email = User.objects.filter(username=data_email).exists()
        # exist_password = User.objects.filter(username = data_email,password = data_password).exists
        user = authenticate(username=data_email, password=data_password)


        if exist_email == False:
            raise forms.ValidationError(u'您输入的邮箱地址有误！')
        if user:
            return cleaned_data
        else:
            raise  forms.ValidationError(u'您输入的密码有误！')





class RegisterForm(forms.Form):
    '''
    注册页表单
    author：陈思齐
    '''
    # 用户名

    name = forms.CharField(
        required=True,
        validators=[name_validator],
        widget=forms.TextInput(attrs={'type': 'name', 'placeholder': '姓名'})
    )

    # 用户邮箱
    email = forms.EmailField(
        required=True,
        validators=[email_validator],
        widget=forms.TextInput(attrs={'type': 'email', 'placeholder': '邮箱'})
    )

    # 用户密码
    password = forms.CharField(        
        error_messages = {
            "required": u'密码不能为空'
            },
        validators = [password_validator],
        widget = forms.TextInput(attrs={'type': 'password', 'placeholder': '密码（不少于6位）'})
        )


class ProfileForm(forms.Form):
    # 用户头像
    # avatar = forms.ImageField(upload_to="avatars")
    avatar = forms.ImageField()

    # 用户描述
    # desc = forms.CharField(null=True, blank=True, default=u"这个用户很懒，还没有描述信息")
    desc = forms.CharField(max_length=100)




class QuestionForm(forms.Form):
    '''
    提问页表单
    author：陈思齐
    '''
    # 问题题目
    title = forms.CharField(
        max_length=100,
        error_messages={
            "required": u'问题标题不能为空'
        },
        validators=[title_validator],
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': '写下你的问题'})
    )

    # 问题说明（描述）
    desc = forms.CharField(
        max_length=1000,
        error_messages={
            "required": u'问题内容不能为空'
        },
        validators=[desc_validator],
        # widget=forms.TextInput(attrs={'type': 'title', 'placeholder': '问题背景、相关代码及截图等详细信息'})
        widget=forms.Textarea(attrs={'rows':"8",'placeholder':"问题背景、相关代码及截图等详细信息"})
    )
    # 话题题目
    topic = forms.CharField(
        max_length=100,
        error_messages={
            "required": u'话题题目不能为空'
        },
        validators=[topic_validator],
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': '话题之间空格隔开'})
    )

