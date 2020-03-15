from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex = models.IntegerField(verbose_name="gender", choices=((0, 'male'), (1, 'female')), default=0)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)
    interests1 = models.TextField()
    interests2 = models.TextField()
    interests3 = models.TextField()
    interests4 = models.TextField()
    interests5 = models.TextField()