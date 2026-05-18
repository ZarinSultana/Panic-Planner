from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import StudyTask
from .forms import StudyTaskForm


def planner_home(request):
    tasks = StudyTask.objects.all()
    return render(request, 'planner/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = StudyTaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = User.objects.first()
            task.save()
            return redirect('planner_home')

    else:
        form = StudyTaskForm()

    return render(request, 'planner/add_task.html', {'form': form})


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


def delete_task(request, task_id):
    task = get_object_or_404(StudyTask, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('planner_home')

    return render(request, 'planner/delete_task.html', {'task': task})


def complete_task(request, task_id):
    task = get_object_or_404(StudyTask, id=task_id)
    task.is_completed = True
    task.save()

    return redirect('planner_home')