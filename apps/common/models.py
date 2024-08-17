from django.db import models


class BaseModel(models.Model):
    is_done = models.BooleanField(default=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
