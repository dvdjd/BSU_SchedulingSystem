from django import forms
from .models import LoginUser

class LoginUserAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = LoginUser
        fields = '__all__'
