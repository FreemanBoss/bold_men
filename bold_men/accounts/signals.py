from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile, Individual, Client, Employee

User = get_user_model()
# superuser profile creation
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
# employee 
@receiver(post_save, sender=Employee)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Employee)
def save_employee_profile(sender, instance, **kwargs):
    instance.profile.save()
    
# individual    
@receiver(post_save, sender=Individual)
def create_individual_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Individual)
def save_individual_profile(sender, instance, **kwargs):
    instance.profile.save()

# client    
@receiver(post_save, sender=Client)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Client)
def save_client_profile(sender, instance, **kwargs):
    instance.profile.save()
    
