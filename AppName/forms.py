from django.forms import *
from .models import SignUp,Login

class SignUpForm(ModelForm):
    class Meta:
        model=SignUp
        fields=('__all__')

class LoginForm(ModelForm):
    email=CharField(error_messages={'required':'email is required','blacnk':'email is required'})
    password=CharField(error_messages={'required':'password is required','blacnk':'password is required'})
    class Meta:
        model=Login
        fields=('email','password')


