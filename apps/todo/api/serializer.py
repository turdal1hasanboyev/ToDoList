from rest_framework.serializers import ModelSerializer

from apps.todo.models import ToDo


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'is_done',
            'slug',
            'description',
            'priority',
            'image',
            'additional',
            "date_started",
            "date_ended",
            "created_at",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        