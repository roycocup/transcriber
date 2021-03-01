from django.db import models
from django.contrib.auth.models import User

class Uploads(models.Model):
    filename = models.CharField(max_length=254)
    bucket = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

