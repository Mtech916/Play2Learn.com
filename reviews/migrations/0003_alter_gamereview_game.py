# Generated by Django 4.2.5 on 2023-10-19 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_gamereview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='game',
            field=models.CharField(choices=[('ANAGRAM', 'Anagram Hunt'), ('MATH', 'Math Facts Practice')], max_length=20),
        ),
    ]
