# Generated by Django 3.2.9 on 2021-12-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0006_game_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loaner',
            field=models.CharField(default='write your name', max_length=50),
        ),
    ]
