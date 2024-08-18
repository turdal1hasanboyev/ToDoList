from django.db import models

from ckeditor.fields import RichTextField

from django.template.defaultfilters import slugify

from apps.common.models import BaseModel


class ToDo(BaseModel):

    PRIORITY = (
        ("None", ("None")),
        ("Low", ("Low")),
        ("Medium", ('Medium')),
        ("High", ("High")),
    )

    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='Images/', null=True, blank=True)
    priority = models.CharField(default=None, choices=PRIORITY, null=True, blank=True, max_length=225)
    additional = models.CharField(max_length=225, null=True, blank=True)
    date_started = models.DateField(null=True, blank=True)
    date_ended = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"
