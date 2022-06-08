from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary import CloudinaryImage
# Create your models here.
class Image(models.Model):
    image = CloudinaryImage('posts',null=True)
    caption = models.CharField(max_length=300,blank=True)
    date_posted = models.DateTimeField(default=datetime.now)
    name=models.CharField(max_length=100,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    location = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.image
