from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView


@login_required
def home(request):
    return render(request, 'index.html')


def task_list(request):
    tasks = Task.objects.filter(assigned_user=request.user)
    return render(request, 'pages/mytodo.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_user=request.user)
    return render(request, 'index2.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_user = request.user
            task.save()
            return redirect('pages')
    else:
        form = TaskForm()
    return render(request, 'pages/mytodo.html', {'form': form})


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tododetails', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'pages/tododetails.html', {'form': form})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_user=request.user)
    task.delete()
    return redirect('task_list')


def signin_view(request):
    return render(request, 'registration/login.html')


def login_view(request):
    return render(request, 'pages/register.html')


def tododetails_view(request):
    # Extract the 'id' parameter from the query string
    task_id = request.GET.get('id')

    # Perform any additional logic to fetch data based on the task_id if needed

    # Pass the task_id to the template
    return render(request, 'pages/tododetails.html', {'task_id': task_id})


#
# def get_dynamic_task_id():
#     global task_counter
#     current_task_id = task_counter
#     task_counter += 1
#     return current_task_id


def userprofile1_view(request):
    return render(request, 'pages/userprofile1.html')


def index(request):
    return render(request, 'index2.html')


def freetemplates_view(request):
    return render(request, 'pages/freetemplates.html')


class MyTodoView(View):
    template_name = 'pages/mytodo.html'

    def get(self, request, *args, **kwargs):
        user_tasks = Task.objects.filter(assigned_user=request.user)
        context = {'user_tasks': user_tasks}

        return render(request, self.template_name, context)


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
