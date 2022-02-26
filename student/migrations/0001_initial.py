# Generated by Django 4.0.1 on 2022-02-07 21:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('section', '0005_rename_number_chapter_chapter_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('aadhar', models.CharField(blank=True, max_length=12, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('daypart', models.CharField(blank=True, max_length=20)),
                ('timeslot_min', models.TimeField(default=django.utils.timezone.now)),
                ('timeslot_max', models.TimeField(default=django.utils.timezone.now)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='section.classname')),
            ],
        ),
    ]
