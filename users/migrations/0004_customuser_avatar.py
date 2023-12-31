# Generated by Django 4.2.5 on 2023-10-14 21:45

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Image must be 200px by 200px.', upload_to='avatars/', validators=[users.models.validate_avatar]),
        ),
    ]
