# Generated by Django 4.1.6 on 2023-03-18 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_rename_studentschedule_studentschedulemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentschedulemodel',
            name='instructor_id',
        ),
    ]