# Generated by Django 4.1.6 on 2023-03-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_exammodel_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodel',
            name='course_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='section_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='room',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='subject_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
