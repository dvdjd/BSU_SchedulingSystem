# Generated by Django 4.1.6 on 2023-03-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0016_alter_academicprogrammodel_program_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicprogrammodel',
            name='program_description',
            field=models.CharField(default='', max_length=100),
        ),
    ]