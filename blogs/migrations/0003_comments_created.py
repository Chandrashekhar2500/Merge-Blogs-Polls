# Generated by Django 4.0.3 on 2022-04-05 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_comments_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
