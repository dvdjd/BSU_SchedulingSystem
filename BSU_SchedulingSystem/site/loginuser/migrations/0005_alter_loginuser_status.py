# Generated by Django 4.1.6 on 2023-02-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginuser', '0004_loginuser_status_alter_loginuser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='status',
            field=models.CharField(choices=[('regular', 'Regular'), ('irregular', 'Irregular')], default='Select Status', max_length=20),
        ),
    ]
