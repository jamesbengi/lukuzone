# Generated by Django 4.0.6 on 2022-07-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_likes_post_no_of_likes_alter_likepost_post_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
