# Generated by Django 4.1.6 on 2023-03-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_exammodel_instructor_id_alter_exammodel_course_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='instructor_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='room',
            field=models.CharField(max_length=20),
        ),
    ]
