# Generated by Django 4.1.2 on 2022-10-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_comment_delete_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_comment',
            field=models.CharField(default='oya', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='media/post_images/martinez.jpeg', null=True, upload_to='post_images'),
        ),
    ]