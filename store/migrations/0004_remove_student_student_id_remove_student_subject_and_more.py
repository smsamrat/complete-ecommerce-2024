# Generated by Django 4.0 on 2024-02-17 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_school_student_student_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentId',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
