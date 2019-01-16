from django import forms;

class Register(forms.Form):
    username = forms.CharField(max_length=20,min_length=5)
    password = forms.CharField(min_length=3,widget=forms.PasswordInput(attrs={'placeholder':'密码'}))
    re_password = forms.CharField(min_length=3,widget=forms.PasswordInput())
    email = forms.EmailField()