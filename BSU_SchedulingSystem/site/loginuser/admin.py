
from django import forms
from django.contrib import admin
from .models import LoginUser
from .forms import LoginUserAdminForm

class MyModelAdmin(admin.ModelAdmin):
    form = LoginUserAdminForm

admin.site.register(LoginUser, MyModelAdmin)