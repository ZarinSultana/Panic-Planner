from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):

     if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']

         user = User.objects.create_user(
             username=username,
             password=password
         )

         user.save()

         return redirect('login')

     return render(request, 'accounts/signup.html')