# Generated by Django 3.2 on 2022-11-27 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20221127_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweetlike',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
