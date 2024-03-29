# Generated by Django 4.2.7 on 2023-11-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_post_updated_at_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]
