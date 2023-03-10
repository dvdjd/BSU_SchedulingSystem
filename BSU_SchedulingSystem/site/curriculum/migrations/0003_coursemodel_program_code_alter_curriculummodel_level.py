# Generated by Django 4.1.6 on 2023-02-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_remove_curriculummodel_course_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='program_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='curriculummodel',
            name='level',
            field=models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], max_length=20),
        ),
    ]
