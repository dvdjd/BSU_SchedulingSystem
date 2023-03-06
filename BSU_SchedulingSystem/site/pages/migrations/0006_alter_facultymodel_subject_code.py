# Generated by Django 4.1.6 on 2023-02-25 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0007_alter_subjectmodel_program_code'),
        ('pages', '0005_remove_facultymodel_course_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultymodel',
            name='subject_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subjectmodel'),
        ),
    ]