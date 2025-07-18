# Generated by Django 5.2.3 on 2025-06-21 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prize', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deadline', models.DateTimeField()),
                ('brief', models.TextField()),
                ('inspiration', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('live', 'Live'), ('closed', 'Closed'), ('judging', 'Judging'), ('completed', 'Completed')], default='upcoming', max_length=20)),
                ('region', models.CharField(blank=True, max_length=100)),
                ('language', models.CharField(default='English', max_length=50)),
                ('max_entries', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(limit_choices_to={'role': 'brand'}, on_delete=django.db.models.deletion.CASCADE, related_name='created_contests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_file', models.FileField(upload_to='contest_videos/')),
                ('thumbnail', models.ImageField(blank=True, upload_to='submission_thumbnails/')),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('under_review', 'Under Review'), ('finalist', 'Finalist'), ('won', 'Won'), ('not_selected', 'Not Selected')], default='submitted', max_length=20)),
                ('feedback', models.TextField(blank=True)),
                ('tags', models.JSONField(blank=True, default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='contests.contest')),
                ('creator', models.ForeignKey(limit_choices_to={'role': 'creator'}, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
