from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# one of them we need to create is UserFrom which is kind of the base form which inherits ModelForms.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # if i want to , I could about that add that in.
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
