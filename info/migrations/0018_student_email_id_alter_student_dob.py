# Generated by Django 4.1.7 on 2023-05-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_alter_assigntime_period_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email_id',
            field=models.EmailField(default='', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(default='2002-01-01'),
        ),
    ]
