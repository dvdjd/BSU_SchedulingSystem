from django import forms
from .models import StudentModel

class StudentAdminForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = '__all__'