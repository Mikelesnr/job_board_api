# Generated by Django 5.1.6 on 2025-03-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='experience_level',
            field=models.CharField(choices=[('Entry', 'Entry Level'), ('Mid', 'Mid Level'), ('Senior', 'Senior Level')], default='entry', max_length=20),
            preserve_default=False,
        ),
    ]
