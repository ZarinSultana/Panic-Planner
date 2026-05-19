from django import forms
from .models import StudyTask , PlannerSettings

class StudyTaskForm(forms.ModelForm):
    class Meta:
        model = StudyTask
        fields = ['title', 'description', 'study_date', 'duration', 'priority']

        widgets = {
            'study_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PlannerSettingsForm(forms.ModelForm):
    class Meta:
        model = PlannerSettings
        fields = ['daily_study_hours','exam_date','total_chapters']

        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
        }