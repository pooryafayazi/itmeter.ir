# Generated by Django 4.2 on 2024-12-15 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_news_newscomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
