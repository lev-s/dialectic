# Generated by Django 3.1.4 on 2020-12-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialecticapp', '0002_auto_20201207_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialecticapp',
            name='night',
            field=models.CharField(max_length=50),
        ),
    ]
