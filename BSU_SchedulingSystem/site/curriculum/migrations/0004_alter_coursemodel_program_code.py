# Generated by Django 4.1.6 on 2023-02-25 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_coursemodel_program_code_alter_curriculummodel_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='program_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.academicprogrammodel'),
        ),
    ]