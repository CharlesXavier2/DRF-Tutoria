# Generated by Django 4.0.1 on 2022-01-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_chapter'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
