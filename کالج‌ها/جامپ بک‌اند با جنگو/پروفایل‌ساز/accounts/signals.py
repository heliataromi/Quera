# TODO : Complete Signals Account
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile, Website


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(m2m_changed, sender=Website.users.through)
def edit_bio(sender, instance, **kwargs):
    # if kwargs['reverse']:
    #     bio = []
    #     for website in Website.objects.filter(users=instance):
    #         bio.append(website.url)
    #     bio_str = '\n'.join(bio)
    #     instance.bio = bio_str
    #     instance.save()

    if not kwargs['reverse']:
        for user in instance.users:
            profile = Profile.objects.get(user=user)
            if instance.url not in profile.bio:
                profile.bio += f'\n{instance.url}'
