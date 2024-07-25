from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from todo.api.serializer import ToDoSerializer
from todo.models import ToDo


class ToDoListView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetaliView(RetrieveAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoCreateView(CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoUpdateView(UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDestroyView(DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
