# Generated by Django 4.0.1 on 2022-02-02 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_rename_subject_teachable_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
