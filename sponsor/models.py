from django.db import models
from django.forms import CharField
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

fs = FileSystemStorage(location='/media/sponsor_photos')

class Profile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=140)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=140)
    postal_code = models.CharField(max_length=140)
    country = CountryField()
    occupation = models.CharField(max_length=140)
    website = models.CharField(max_length=100)
    purpose = models.CharField(max_length=140)
    about = models.CharField(max_length=140)
    status = models.IntegerField(choices=((1, ("Public")),
                                          (2, ("Private"))),
                                 default=1)
    profile_picture = models.ImageField(upload_to='sponsor_photos', blank=True, null=True)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

