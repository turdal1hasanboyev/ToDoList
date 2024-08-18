from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .serializer import ToDoSerializer
from apps.todo.models import ToDo


class ToDoListView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return self.queryset.filter(is_done=False)


class ToDoDetaliView(RetrieveAPIView):
    queryset = ToDo.objects.filter(is_done=False)
    serializer_class = ToDoSerializer
    lookup_field = 'slug'


class ToDoCreateView(CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoUpdateView(UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return ToDo.objects.filter(is_done=False)


class ToDoDestroyView(DestroyAPIView):
    queryset = ToDo.objects.filter(is_done=False)
    serializer_class = ToDoSerializer
    lookup_field = "slug"

    def perform_destroy(self, instance):
        instance.is_done = True
        
        instance.save()
