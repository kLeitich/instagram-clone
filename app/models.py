from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to ='postimage')
    caption = models.CharField(max_length=300,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_image')
    

    def __str__(self):
        return f'{self.user} post_image'

    class Meta:
        ordering = ["-pk"]

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()
    
    @classmethod
    def get_profile_posts(cls,profile):
        posts = Image.objects.filter(profile__pk= profile)
        return posts
    @classmethod
    def update_post_caption(cls,id,caption):
        update =cls.objects.filter(id=id).update(caption=caption)
        return update

class Profile(models.Model):
    ppic=models.ImageField(upload_to ='ppic') 
    bio=models.TextField(max_length=600, default="Bio")
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return f'{self.user.username} insta-profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following',null=True)
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers',null=True)

    def __str__(self):
        return f'{self.follower} Follow'
           

            
    def save_follow(self):
        self.save()

    def delete_follow(self):
        self.delete()