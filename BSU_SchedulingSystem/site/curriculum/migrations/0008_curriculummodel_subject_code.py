# Generated by Django 4.1.6 on 2023-02-26 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0007_alter_subjectmodel_program_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculummodel',
            name='subject_code',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='curriculum.subjectmodel'),
        ),
    ]
