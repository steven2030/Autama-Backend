from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    sex = models.IntegerField(verbose_name="gender", choices=((0, 'male'), (1, 'female')), default=0)
    phone = models.CharField(verbose_name="phone", null=True, max_length=11)
    address = models.CharField(verbose_name="address", null=True, max_length=255)
    interest = models.CharField(max_length=255, null=True)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)


class RobotModel(models.Model):

    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)
    fname = models.CharField(max_length=255, verbose_name="firstname")
    lname = models.CharField(max_length=255, verbose_name="lastname")
    owner = models.CharField(max_length=255, verbose_name="onwer")
    year = models.IntegerField(verbose_name="age")
    interest = models.CharField(max_length=255, null=True, verbose_name="hobby")
    match_number = models.IntegerField(verbose_name="number_of_matches", default=0)
    creator = models.CharField(verbose_name="creator", max_length=100, null=True)

