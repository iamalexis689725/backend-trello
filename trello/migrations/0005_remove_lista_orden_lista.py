# Generated by Django 5.1.1 on 2024-09-24 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0004_tarea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='orden_lista',
        ),
    ]
