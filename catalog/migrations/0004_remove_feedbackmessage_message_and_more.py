# Generated by Django 5.1.1 on 2024-09-24 23:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_feedbackmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackmessage',
            name='message',
        ),
        migrations.AddField(
            model_name='feedbackmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Time of creation'),
            preserve_default=False,
        ),
    ]
