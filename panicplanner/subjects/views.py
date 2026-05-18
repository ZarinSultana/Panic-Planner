from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm


def subject_list(request):
    subjects = Subject.objects.filter(user=request.user)

    return render(request, 'subjects/subject_list.html', {
        'subjects': subjects
    })


def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()

            return redirect('subject_list')
    else:
        form = SubjectForm()

    return render(request, 'subjects/subject_form.html', {
        'form': form
    })