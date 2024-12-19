from django import forms
from blog.models import PostComment
from captcha.fields import CaptchaField


class PostCommentForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = PostComment
        fields =  ['post','name','email','subject' ,'message']