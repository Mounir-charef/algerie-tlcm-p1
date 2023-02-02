from django import forms
from .models import User
from captcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()
