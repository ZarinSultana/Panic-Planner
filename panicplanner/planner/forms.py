from django import forms
from .models import StudyTask


class StudyTaskForm(forms.ModelForm):
    class Meta:
        model = StudyTask
        fields = ['title', 'description', 'study_date', 'duration', 'priority']

        widgets = {
            'study_date': forms.DateInput(attrs={'type': 'date'}),
        }