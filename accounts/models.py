from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex = models.IntegerField(verbose_name="gender", choices=((0, 'male'), (1, 'female'), (2, 'non-binary')), default=0)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)
    interests1 = models.TextField()
    interests2 = models.TextField()
    interests3 = models.TextField()
    interests4 = models.TextField()
    interests5 = models.TextField()
    interests6 = models.TextField()
    currentAutama = models.IntegerField()  # Used for find matches stack tracing.
    nextAutama = models.IntegerField()
    my_Autama = models.IntegerField(default=0) # Use for tracking the amount of Autamas the user created
    last_page = models.CharField(max_length=100, default='/MyMatches/') # Tracks the page used to get to chat page


class Claims(models.Model):
    autamaID = models.OneToOneField('AutamaProfiles.AutamaProfile', on_delete=models.CASCADE)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)

    
class Messages(models.Model):
    # Constants used for enum in sender
    USER = 'User'
    AUTAMA = 'Autama'
    SENDER_CHOICES = [
        (USER, 'User'),
        (AUTAMA, 'Autama'),
    ]

    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    autamaID = models.ForeignKey('AutamaProfiles.AutamaProfile', on_delete=models.CASCADE)
    sender = models.CharField(max_length=6, choices=SENDER_CHOICES)

    def __str__(self):
        return '{userID} {autamaID}'.format(userID=self.userID, autamaID=self.autamaID)


class Matches(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    autamaID = models.ForeignKey('AutamaProfiles.AutamaProfile', on_delete=models.CASCADE)
