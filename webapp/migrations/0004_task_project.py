# Generated by Django 5.0 on 2023-12-23 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_project_alter_task_description_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='webapp.project', verbose_name='Проект'),
        ),
    ]
