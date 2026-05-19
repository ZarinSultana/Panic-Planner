from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import StudyTask
from .forms import StudyTaskForm

from datetime import date, timedelta
from .models import PlannerSettings
from .forms import PlannerSettingsForm

@login_required
def planner_home(request):
    tasks = StudyTask.objects.filter(user=request.user)
    return render(request, 'planner/home.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = StudyTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('planner_home')

    else:
        form = StudyTaskForm()

    return render(request, 'planner/add_task.html', {'form': form})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(StudyTask, id=task_id)

    if request.method == 'POST':
        form = StudyTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('planner_home')

    else:
        form = StudyTaskForm(instance=task)

    return render(request, 'planner/update_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(StudyTask, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('planner_home')

    return render(request, 'planner/delete_task.html', {'task': task})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(StudyTask, id=task_id)
    task.is_completed = True
    task.save()

    return redirect('planner_home')

@login_required
def generate_plan(request):

    if request.method == 'POST':
        form = PlannerSettingsForm(request.POST)

        if form.is_valid():
            planner = form.save(commit=False)
            planner.user = request.user
            planner.save()

            exam_date = planner.exam_date
            total_chapters = planner.total_chapters

            today = date.today()

            days_left = (exam_date - today).days

            if days_left <= 0:
                return redirect('planner_home')

            chapter_gap = max(1, days_left // total_chapters)

            for i in range(total_chapters):

                study_day = today + timedelta(days=i * chapter_gap)

                priority = 'Medium'

                if days_left <= 3:
                    priority = 'High'

                elif days_left >= 10:
                    priority = 'Low'

                StudyTask.objects.create(
                    user=planner.user,
                    title=f'Chapter {i+1} Study Session',
                    description=f'Study Chapter {i+1}',
                    study_date=study_day,
                    duration=planner.daily_study_hours * 60,
                    priority=priority
                )

            return redirect('planner_home')

    else:
        form = PlannerSettingsForm()

    return render(request, 'planner/generate_plan.html', {'form': form})

@login_required
def reschedule_task(request, task_id):

    task = get_object_or_404(StudyTask, id=task_id)

    new_date = task.study_date + timedelta(days=1)

    task.study_date = new_date
    task.priority = 'High'

    task.save()

    return redirect('planner_home')