from django import forms
from .models import Subject
from .models import Exam
from .models import Topic

class SubjectForm(forms.ModelForm):
    class  Meta:
        model=Subject
        fields=['name','description','exam_date']

        class ExamForm(forms.ModelForm):
            model=Exam
            fields=['title','exam_date','total_marks']



            class TopicForm(forms.ModelForm):
                class Meta:
                    model=Topic

                    fields=['topic_name','completed']
                    