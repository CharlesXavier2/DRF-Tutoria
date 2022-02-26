# Generated by Django 4.0.1 on 2022-02-26 14:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0005_rename_number_chapter_chapter_number'),
        ('student', '0003_alter_student_daypart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoomReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('homework_percentage', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('percentage_finished', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('is_notes_done', models.BooleanField(default=False)),
                ('is_qna_done', models.BooleanField(default=False)),
                ('is_memorized', models.BooleanField(default=False)),
                ('is_test_done', models.BooleanField(default=False)),
                ('last_modified', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='section.chapter')),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='section.classname')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='student.classroom')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='section.subject')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
