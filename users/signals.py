from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .models import Profile

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        my_group = Group.objects.get(name='Free') 
        my_group.user_set.add(user)
        profile = Profile(user=user)
        profile.nama = user.username
        profile.email = user.email
        profile.save()
