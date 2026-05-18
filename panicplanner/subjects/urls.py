from django.urls import path
from.import views

urlpatterns=[
    path('',views.subject_list,name='subject_list'),

path ('add/',views.subject_create,name='subject_create'),
]