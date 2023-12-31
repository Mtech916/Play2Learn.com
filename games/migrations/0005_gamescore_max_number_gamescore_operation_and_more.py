# Generated by Django 4.2.5 on 2023-10-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_gamescore_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='max_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='operation',
            field=models.CharField(blank=True, choices=[('+', 'Addition'), ('-', 'Subtraction'), ('x', 'Multiplication'), ('/', 'Division')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='total_words',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='word_length',
            field=models.CharField(blank=True, choices=[('3', '3 letter words'), ('4', '4 letter words'), ('5', '5 letter words'), ('6', '6 letter words'), ('7', '7 letter words'), ('8', '8 letter words')], max_length=20, null=True),
        ),
    ]
