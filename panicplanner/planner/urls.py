from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner_home, name='planner_home'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('generate-plan/', views.generate_plan, name='generate_plan'),
    path('reschedule/<int:task_id>/', views.reschedule_task, name='reschedule_task'),


]