from django import forms
from .models import newsComment
#from captcha.fields import CaptchaField


class newsCommentForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = newsComment
        fields =  ['news','name','email','subject' ,'message']