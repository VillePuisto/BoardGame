# Generated by Django 3.2.9 on 2021-11-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
