# Generated by Django 4.2 on 2024-12-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defaultPost.jpg', upload_to='blog/% Y/% m/% D/'),
        ),
    ]
