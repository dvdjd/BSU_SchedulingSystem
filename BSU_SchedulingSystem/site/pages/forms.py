from django import forms
from .models import FacultyModel

DAYS_OF_WEEK = (
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
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