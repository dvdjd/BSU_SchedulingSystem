# Generated by Django 4.1.6 on 2023-03-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_studentmodel_subject_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_id', models.CharField(max_length=20)),
                ('student_id', models.CharField(max_length=20)),
                ('faculty_schedule_id', models.CharField(max_length=20)),
            ],
        ),
    ]