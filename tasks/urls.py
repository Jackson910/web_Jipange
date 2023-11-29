from django.urls import path
from . import views
from .views import signin_view
from .views import login_view
from .views import MyTodoView
from .views import tododetails_view

urlpatterns = [
    path('', views.home, name='home'),
    path('task_list', views.task_list, name='task_list'),
    path('registration/index2.html/', views.index, name='index2'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('task/update/<int:task_id>/', views.task_update, name='task_update'),
    path('pages/tododetails/<int:id>/', views.tododetails_view, name='tododetails'),
    path('registration/login.html/', signin_view, name='signin'),
    path('pages/register.html', login_view, name='login'),
    path('pages/mytodo.html/', MyTodoView.as_view(), name='mytodo'),
    # path('pages/tododetails.html', views.tododetails_view, name='tododetails'),
    path('pages/freetemplates.html', views.freetemplates_view, name='freetemplates'),
    path('pages/userprofile1/', views.userprofile1_view, name='userprofile1')


]
