from django.urls import path

from .views import ToDoCreateView, ToDoDetaliView, ToDoDestroyView, ToDoListView, ToDoUpdateView


app_name = 'todo'

urlpatterns = [
    path('todolist/', ToDoListView.as_view(), name='todo-list'),
    path('tododetail/<slug:slug>/', ToDoDetaliView.as_view(), name='todo-detail'),
    path('todoupdate/<slug:slug>/', ToDoUpdateView.as_view(), name='todo-update'),
    path('todocreate/', ToDoCreateView.as_view(), name='todo-create'),
    path('tododelete/<slug:slug>/', ToDoDestroyView.as_view(), name='todo-delete'),
]
