# Generated by Django 4.1.6 on 2023-02-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultymodel',
            name='level',
        ),
    ]
