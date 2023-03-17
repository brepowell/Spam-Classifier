from django.db import models

# USERS
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone - PROFILE EXAMPLE
# https://docs.djangoproject.com/en/4.1/ref/contrib/auth/ - DJANGO'S DEFAULT USER
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    emailCount = models.IntegerField(default=0)
    spamCount = models.IntegerField(default=0)
    emails = models.ManyToManyField('Email', blank=True) #One profile has many Email objects
    is_active = models.BooleanField()

class Email(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=80) # gmail's max length is 70, but set to 80 just in case
    fullText = models.FileField() # includes the header details of the email and body of email - raw txt file
    isSpam = models.BooleanField(default = False)
    dateReceived = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return "Header:\n" + self.header + "\nDate:"  # TODO: CHECK WITH TEAM ABOUT WHAT TO RETURN

@receiver(post_save, sender=Email)
def flag_email(sender, instance, created, **kwargs):
    if created:
        Email.objects.update() # TODO: FINISH THIS!


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

