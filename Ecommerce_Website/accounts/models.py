from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pancard_name = models.CharField(max_length=255, null=True, blank=True)
    pancard_number = models.CharField(max_length=255, null=True, blank=True)
    aadharcard_name = models.CharField(max_length=255, null=True, blank=True)
    aadharcard_number = models.CharField(max_length=255, null=True, blank=True)
    user_contact_number = models.CharField(max_length=20, null=True, blank=True)
    user_sex = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.__str__()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=255, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    alternate_no = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='child')
    child_name = models.CharField(max_length=255, null=True, blank=True)
    child_birth_date = models.DateField()

    def __str__(self):
        return self.child_name

    def __repr__(self):
        return self.__str__()








