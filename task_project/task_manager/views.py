from django.shortcuts import render, redirect
from .task_manager import get_tasks, add_task, delete_task

def task_list(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            add_task(task)
        return redirect('task_list')

    return render(request, "task_manager/task_list.html", {"tasks": get_tasks()})

def delete_task_view(request, task_index):
    delete_task(task_index)
    return redirect('task_list')
