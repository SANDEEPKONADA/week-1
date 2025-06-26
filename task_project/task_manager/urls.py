# task_manager/urls.py

from django.urls import path
from .views import task_list, delete_task_view

urlpatterns = [
    path('', task_list, name='task_list'),
    path('delete/<int:task_index>/', delete_task_view, name='delete_task'),
]
