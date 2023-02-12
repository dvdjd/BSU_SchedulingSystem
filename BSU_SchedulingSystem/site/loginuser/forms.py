from django.forms import forms
from .models import LoginUser

class LoginUserForm(forms.ModelForm):
    
    class Meta:
        model = LoginUser
        fields = ['userid', 'username', 'password', 'firstname', 'middlename', 'lastname', 'usertype']
        widgets = {
            'password': forms.PasswordInput()
        }
    