# Generated by Django 4.2 on 2024-12-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_news_topic_news_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.URLField(),
        ),
    ]