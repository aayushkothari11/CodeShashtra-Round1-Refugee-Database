from django.db import models
from django.contrib.auth.models import User
import datetime


class NGO(models.Model):
    user = models.OneToOneField(User, related_name="ngo", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    international = models.BooleanField(default=False)
    ngo_id = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Refugee(models.Model):
    refugee = models.OneToOneField(User, on_delete=models.CASCADE, related_name="refugee")
    ngo = models.ForeignKey(NGO, blank=True, null=True, on_delete=models.SET_NULL, related_name="ngo")
    country = models.CharField(max_length=50)
    photo = models.FileField(blank=True)
    bio = models.CharField(max_length=200, blank=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    mobileNo = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    passport = models.FileField(blank=True)
    passport_id = models.CharField(max_length=50, blank=True, null=True)
    registered_on = models.DateField(("Date"), default=datetime.date.today, blank=True)

    def __str__(self):
        return str(self.refugee.username)
