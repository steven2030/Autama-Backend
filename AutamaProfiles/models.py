from django.db import models

# Create your models here.


class AutamaProfile(models.Model):
    autamaid = models.CharField(max_length=100, primary_key=True)
    creator = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='Images', blank=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    nummatches = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    #pickle
    #interests

    def __str__(self):
        return self.autamaid
