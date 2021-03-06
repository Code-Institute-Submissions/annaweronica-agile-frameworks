from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):

    """ A user profile model for mantaining keeping
    login data, purchase history and review CRUD """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_country = CountryField(max_length=40, null=False, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    """ Create or update the user profil """
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
