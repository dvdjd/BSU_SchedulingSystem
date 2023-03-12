# Generated by Django 4.1.6 on 2023-03-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0010_alter_subjectmodel_section_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculummodel',
            name='period',
            field=models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', 'Midterm')], max_length=20),
        ),
    ]
