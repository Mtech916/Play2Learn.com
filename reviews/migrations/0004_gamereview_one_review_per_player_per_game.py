# Generated by Django 4.2.5 on 2023-11-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_gamereview_game'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='gamereview',
            constraint=models.UniqueConstraint(fields=('user', 'game'), name='One_review_per_player_per_game'),
        ),
    ]
