# Generated by Django 3.1.3 on 2021-02-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210220_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_color',
            field=models.CharField(default='8d0de1', max_length=20),
        ),
    ]
