# Generated by Django 4.1.6 on 2023-02-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0006_subjectmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='program_code',
            field=models.CharField(max_length=20),
        ),
    ]
