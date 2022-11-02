from django import forms
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', "description", 'unit')

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')