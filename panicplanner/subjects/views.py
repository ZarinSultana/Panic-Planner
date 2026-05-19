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


def subject_update(request,pk):
    subject=get_object_or_404(Subject,pk=pk,user=request.user)
    if request.method =='POST':
        form=SubjectForm(request.POST,instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        else:
            form=SubjectForm(instance=subject)
            context={'form':form}
            return render(request,'subjectss/subject_form.html',context)


def  subject_delete(request,pk)
    subject=get_object_or_404(Subject,pk=pk,user=request.user)
    if request.method=='POST':
        subject.delete()
        return redirect('subject_list')
      context={'subject':subject}
    return render(request,'subjects/subject_delete.html',context)

