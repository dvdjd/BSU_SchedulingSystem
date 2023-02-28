from django import forms
from .models import CurriculumModel

class CurriculumAdminForm(forms.ModelForm):
    program_code = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = CurriculumModel
        fields = '__all__'