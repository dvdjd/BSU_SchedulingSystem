# Generated by Django 4.1.6 on 2023-03-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginuser', '0006_remove_loginuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='usertype',
            field=models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor'), ('admin', 'Administrator')], default='Select User Type', max_length=20),
        ),
    ]
