# Generated by Django 4.0.1 on 2022-02-26 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_classroomreport_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroomreport',
            name='report_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
