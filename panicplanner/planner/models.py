from django.db import models
from django.contrib.auth.models import User


class StudyTask(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    study_date = models.DateField()
    duration = models.IntegerField(help_text="Study duration in minutes")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudySchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    total_tasks = models.IntegerField(default=0)

    def __str__(self):
        return self.schedule_name

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_text = models.CharField(max_length=255)
    reminder_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.reminder_text
