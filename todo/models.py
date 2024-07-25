from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
