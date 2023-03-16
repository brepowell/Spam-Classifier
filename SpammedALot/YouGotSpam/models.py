from django.db import models

# USERS
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    emailCount = models.IntegerField(default=0)
    spamCount = models.IntegerField(default=0)
    emails = models.ManyToManyField('Email', blank=True)

class Email(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    body = models.TextField()
    isSpam = models.BooleanField(default = False)

    def __str__(self) -> str:
        return "Header:\n" + self.header
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()