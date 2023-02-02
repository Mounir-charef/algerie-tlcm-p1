from django import forms
from .models import User
from captcha.fields import ReCaptchaField


class UserForm(forms.ModelForm):

    captcha = ReCaptchaField(label='')

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
