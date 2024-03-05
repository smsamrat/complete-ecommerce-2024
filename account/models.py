from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):

    CHOICE_GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user_profile")
    full_name = models.CharField(max_length=30,blank=True, null=True)
    phone_number = models.CharField(max_length=30,blank=True, null=True)
    address = models.CharField(max_length=30,blank=True, null=True)
    gender = models.CharField(max_length=16,choices=CHOICE_GENDER)
    created = models.DateTimeField(default=timezone.now)

    @receiver(post_save, sender=User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)



class Size(models.Model):
    name = models.CharField(max_length=30,blank=True, null=True)


