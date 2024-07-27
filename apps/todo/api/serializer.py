from rest_framework.serializers import ModelSerializer

from apps.todo.models import ToDo


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'is_done',
            'updated_at',
            'created_at',
            'slug',
            'description',
            'priority',
            'image',
            'additional',
            "date_started",
            "date_ended",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "updated_at": {"read_only": True},
            "created_at": {"read_only": True},
        }
        