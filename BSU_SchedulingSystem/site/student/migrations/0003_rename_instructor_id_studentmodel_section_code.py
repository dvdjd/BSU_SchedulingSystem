# Generated by Django 4.1.6 on 2023-03-12 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_days_studentmodel_instructor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='instructor_id',
            new_name='section_code',
        ),
    ]