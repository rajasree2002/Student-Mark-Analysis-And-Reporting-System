# Generated by Django 4.2.1 on 2023-05-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0021_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email_id',
            field=models.EmailField(default='', editable=False, max_length=30),
        ),
    ]