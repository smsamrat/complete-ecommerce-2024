from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user','created')
