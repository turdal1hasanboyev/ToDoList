from rest_framework.serializers import ModelSerializer

from todo.models import ToDo


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = [
            'id',
            'name',
            'description',
        ]

        extra_kwargs = {
            "id": {"read_only": True},
        }
        