# Generated by Django 3.2.9 on 2021-11-20 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0002_alter_game_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='owner',
            field=models.JSONField(default='mystery'),
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='describe your game')),
                ('onLoan', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardgames.game')),
            ],
        ),
    ]
