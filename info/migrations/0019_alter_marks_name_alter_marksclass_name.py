# Generated by Django 4.2.1 on 2023-05-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_student_email_id_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
    ]
