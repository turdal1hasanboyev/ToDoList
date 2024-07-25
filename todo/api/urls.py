from django.urls import path

from todo.api.views import ToDoCreateView, ToDoDetaliView, ToDoDestroyView, ToDoListView, ToDoUpdateView


app_name = 'todo'


urlpatterns = [
    path('todolist/', ToDoListView.as_view(), name='todo-list'),
    path('tododetail/<int:pk>/', ToDoDetaliView.as_view(), name='todo-detail'),
    path('todoupdate/<int:pk>/update/', ToDoUpdateView.as_view(), name='todo-update'),
    path('todocreate/', ToDoCreateView.as_view(), name='todo-create'),
    path('tododelete/<int:pk>/', ToDoDestroyView.as_view(), name='todo-delete'),
]
