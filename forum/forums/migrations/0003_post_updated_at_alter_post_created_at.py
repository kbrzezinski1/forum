# Generated by Django 4.2.7 on 2023-11-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_topic_updated_at_alter_topic_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
