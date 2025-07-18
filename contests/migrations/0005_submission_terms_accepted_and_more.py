# Generated by Django 5.2.3 on 2025-06-25 15:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_submission_view_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='terms_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='terms_accepted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('pending_approval', 'Pending Approval'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('under_review', 'Under Review'), ('finalist', 'Finalist'), ('won', 'Won'), ('not_selected', 'Not Selected')], default='pending_approval', max_length=20),
        ),
        migrations.CreateModel(
            name='ContestApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('terms_accepted', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, help_text='Creator notes or admin feedback')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='contests.contest')),
                ('creator', models.ForeignKey(limit_choices_to={'role': 'creator'}, on_delete=django.db.models.deletion.CASCADE, related_name='contest_applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('contest', 'creator')},
            },
        ),
    ]
