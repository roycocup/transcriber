from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.dispatch import receiver

class Uploads(models.Model):
    filename = models.CharField(max_length=254)
    bucket = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


class User_Ext(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session = models.CharField(max_length=254, null=True)


# @receiver(pre_save, sender=User)
# def user_save(sender, instance, **kwargs):
#     try:
#         user = User.objects.get(username='anonymous')
#         ext, created = User_Ext.objects.create(user=user)
#     except Exception as e:
#         print(instance, kwargs, e)


# @receiver(post_save, sender=User)
# def user_save(sender, instance, **kwargs):
#     try:
#         ext, created = User_Ext.objects.get_or_create(user=sender)
#     except Exception as e:
#         print(instance, kwargs, e)

