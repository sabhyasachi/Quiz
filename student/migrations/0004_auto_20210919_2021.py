# Generated by Django 3.0.8 on 2021-09-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210919_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(default=1, max_length=40, unique=True),
        ),
    ]
