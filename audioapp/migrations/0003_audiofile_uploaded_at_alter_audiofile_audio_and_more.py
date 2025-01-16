# Generated by Django 5.0.2 on 2024-07-15 15:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0002_remove_audiofile_created_at_alter_audiofile_audio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='audio',
            field=models.FileField(upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='transcript',
            field=models.TextField(blank=True, null=True),
        ),
    ]
