from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

#User Form with available fields for User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

#User Profile Info Form with few additional fields
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
