from django import forms;

class Register(forms.Form):
    username = forms.CharField(max_length=10,min_length=5)
    password = forms.CharField(min_length=3,max_length=8,widget=forms.PasswordInput(attrs={'placeholder':'请输入密码'}))
    re_password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

class Login(forms.Form):
    username = forms.CharField(max_length=10,min_length=5)
    password = forms.CharField(widget=forms.PasswordInput())
