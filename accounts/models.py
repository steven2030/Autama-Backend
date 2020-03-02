from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(primary_key=True)
    first = models.CharField(max_length=40)
    last = models.CharField(max_length=40)
    picture = models.FilePathField()
    interests1 = models.TextField()
    interests2 = models.TextField()
    interests3 = models.TextField()
    interests4 = models.TextField()
    interests5 = models.TextField()