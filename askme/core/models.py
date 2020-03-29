from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileManager(models.Manager):

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, **kwargs):
        if kwargs.get('created', True) and not kwargs.get('raw', False):
            Profile.objects.create(user=instance)
        instance.profile.save()

    def to_json(self):
        return {
            'nickname': self.nickname,
            'avatar_url': self.avatar.url,
        }


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    nickname = models.CharField(max_length=15, default=None, null=True, unique=True)
    avatar = models.ImageField(upload_to="profile/avatars", blank=False, null=True)
    has_question = models.BooleanField(default=False)

    objects = ProfileManager()

    def __str__(self):
        return 'Profile {}' .format(self.user)
