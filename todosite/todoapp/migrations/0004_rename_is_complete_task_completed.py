# Generated by Django 4.0.4 on 2022-04-14 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_task_is_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_complete',
            new_name='completed',
        ),
    ]