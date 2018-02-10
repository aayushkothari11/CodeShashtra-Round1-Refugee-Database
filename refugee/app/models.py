from django.db import models
from django.contrib.auth.models import User


class NGO(models.Model):
    user = models.OneToOneField(User, related_name="ngos")
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    international = models.BooleanField(default=False)
    ngo_id = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
