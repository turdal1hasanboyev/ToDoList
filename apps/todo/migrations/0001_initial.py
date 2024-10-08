# Generated by Django 4.2.14 on 2024-08-17 03:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(blank=True, default=False, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('slug', models.SlugField(blank=True, max_length=225, null=True, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('priority', models.CharField(blank=True, choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default=None, max_length=225, null=True)),
                ('additional', models.CharField(blank=True, max_length=225, null=True)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_ended', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
