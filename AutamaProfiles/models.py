from django.db import models

# Create your models here.


class AutamaProfile(models.Model):
    autamaid = models.CharField(max_length=100, default="0")
    creator = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='Images', blank=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    nummatches = models.CharField(max_length=100, default='0000000', editable=False)
    owner = models.CharField(max_length=100, default='FREE')
    pickle = models.CharField(max_length=100, default='PICKLE')
    interests = models.CharField(max_length=100)

    def __str__(self):
        return self.autamaid
