# Generated by Django 4.2.5 on 2023-10-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
    ]