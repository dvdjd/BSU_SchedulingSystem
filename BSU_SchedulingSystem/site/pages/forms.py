from django import forms
from .models import FacultyModel

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

class FacultyAdminForm(forms.ModelForm):
    days = forms.MultipleChoiceField(
        choices=DAYS_OF_WEEK,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = FacultyModel
        fields = '__all__'
        
    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        days = self.cleaned_data['days']
        # Convert the list of selected days into a comma-separated string
        instance.days = ','.join(days)
        instance.save()
        return instance