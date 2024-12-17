from django import forms
from .models import Contact,newsComment,Newsletter
#from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = Contact
        fields =  '__all__'
class newsCommentForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = newsComment
        fields =  ['news','name','email','subject' ,'message']