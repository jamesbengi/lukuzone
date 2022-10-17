from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.
User=get_user_model()
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=TRUE)
    profileimg=models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.user.username
class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images',blank=True,null=True,default='media/post_images/martinez.jpeg')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)
    def __str__(self):
        return self.user
class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    def __str__(self):
        return self.username
class FollowersCount(models.Model):
    follower=models.CharField(max_length=200)
    user=models.CharField(max_length=100)
    def __str__(self):
        return self.user
class Comment(models.Model):
    comment=models.CharField(max_length=200)
    user_comment=models.CharField(max_length=100,blank=False,default='oya')
    time_msg=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.comment













































        