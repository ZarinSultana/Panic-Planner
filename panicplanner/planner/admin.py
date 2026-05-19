from django.contrib import admin
from .models import StudyTask, StudySchedule, Reminder, PlannerSettings

admin.site.register(StudyTask)
admin.site.register(StudySchedule)
admin.site.register(Reminder)
admin.site.register(PlannerSettings)