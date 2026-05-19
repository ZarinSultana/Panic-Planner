from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date, timedelta

@login_required
def dashboard(request):

    context = {
        "study_hours": 3.5,
        "syllabus_percent": 68,
        "pending_tasks": 5,
        "next_exam_days": 3,

        "today_tasks": [
            {"title": "Data Structures - Trees", "time": "10:00 AM"},
            {"title": "OOP Practice", "time": "12:00 PM"},
        ],

        "subjects": [
            {"name": "CSE303", "progress": 80},
            {"name": "Math", "progress": 55},
            {"name": "Physics", "progress": 60},
        ],

        "motivation_text": "Small progress every day leads to big success in exams."
    }

    return render(request, "dashboard/dashboard.html", context)