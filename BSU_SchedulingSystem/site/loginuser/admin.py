
from django import forms
from django.contrib import admin
from .models import LoginUser
from .forms import LoginUserAdminForm

class LoginUserAdmin(admin.ModelAdmin):
    form = LoginUserAdminForm

admin.site.register(LoginUser, LoginUserAdmin)